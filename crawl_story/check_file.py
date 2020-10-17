from datetime import date, datetime
import requests
from bs4 import BeautifulSoup
import django
from django.core.exceptions import ObjectDoesNotExist
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Crawler.settings')
django.setup()

from crawler_story.models import Category, Story, Chaper


def new_request(url):
    html_doc = requests.get(url=url).text
    data = BeautifulSoup(html_doc, 'html.parser')
    return data


def get_story(url):
    data = new_request(url)
    name_story = data.find('h1', class_='title').text
    author = data.find_all('span')[6].a.text
    infos = data.find('div', class_='infos').find_all('p')

    try:
        create = Story.objects.all().get(name_story=name_story, author=author)
        new = False
    except ObjectDoesNotExist:
        new = True

    if new:
        content_story = str(data.find('div', class_='description'))
        category = []
        content = data.find('p', class_='story_categories').span.find_all('a')

        for item in content:
            category.append(item.text.strip())

        status = infos[4].text.strip()
        image = data.find('div', class_='thumb').img['src']
        time_refresh = infos[5].text.strip()
        date_time = datetime.strptime(time_refresh, '%H:%M:%S %d/%m/%Y')

        create = Story(
            name_story=name_story,
            status=status,
            content_story=content_story,
            author=author,
            image=image,
            date_refresh=date_time
        )
        create.save()

        for item in category:
            try:
                a = Category.objects.get(categorys=item)
            except ObjectDoesNotExist:
                a = Category.objects.create(categorys=item)

            create.categorys.add(a)

        first_chap = data.find('a', class_='read-btn')['href']
    else:
        first_chap = data.find('ul', class_='chapters').find('li').find('a')['href']

    print((name_story, new))
    return create, first_chap, new


def check_day(day):
    return day == datetime.strftime(date.today(), '%d/%m/%Y')


def create_chaper(name_story, url_chap):
    data = new_request(url=url_chap)
    name_chap = data.find('h2', class_='chapter-title').text.strip()
    status = data.find('div', id='chapter-content')['data-vip']

    if status == '1':
        content = ''
        url = url_chap
    else:
        content = str(data.find('div', id='chapter-content'))
        url = ''

    create_date = data.find_all('header')[1].find_all('p')[2].text.strip().strip('"')
    date_create = datetime.strptime(create_date, '%d/%m/%Y').date()
    Chaper.objects.create(
        name_chap=name_chap,
        content=content,
        name_story=name_story,
        status=status,
        url=url,
        create_date=date_create
    )

    print(name_chap)


def crawl_chaper(create, first_chap, new):
    if new:
        data = new_request(first_chap)
        create_chaper(create, first_chap)

        while True:
            link = str(data.find_all('a', class_='chap-nav')[1]['href'])

            if link != '#':
                create_chaper(create, link)
                data = new_request(link)

    else:
        data = new_request(first_chap)
        list_url = []
        create_date = data.find_all('header')[1].find_all('p')[2].text.strip().strip('"')
        chap = Chaper.objects.all().filter(name_story=create)
        print(chap)
        print(create_date)

        while True:
            name_chap = data.find('h2', class_='chapter-title').text.strip()

            try:
                chap.get(name_chap=name_chap)
                break
            except ObjectDoesNotExist:
                list_url.append(first_chap)
                print(first_chap)

            first_chap = data.find_all('a', class_='chap-nav')[0]['href']

            if first_chap != '#':
                data = new_request(first_chap)

        list_url.reverse()

        for url in list_url:
            create_chaper(create, url)
