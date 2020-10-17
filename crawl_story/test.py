import os
import django
from check_file import new_request, get_story, check_day, create_chaper, crawl_chaper
from datetime import datetime, time
import time
from django.core.exceptions import ObjectDoesNotExist
import threading


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Crawler.settings")
django.setup()

from crawler_story.models import Category, Story, Chaper


def new_claw():
    url = "https://webtruyen.com/all/1/"

    while True:
        soup = new_request(url)
        number = int(url.split('/')[-2])
        url = url.replace(str(number), str(number+1))
        content = soup.find_all('li', class_='story-list')

        for item in content:
            time_stamp = int(item.find('i', class_='last-updated').text)
            time_delta = datetime.now() - datetime.fromtimestamp(time_stamp)
            sum_seconds = time_delta.total_seconds()

            if sum_seconds <= 62000:
                link_url = item.find("a", class_='thumb')['href']
                print(link_url)
                story = get_story(url=link_url)
                print(story)
                crawl_chaper(story[0], story[1], story[2])
                print('')


def old_crawl():
    while True:
        try:
            chap = Chaper.objects.all().filter(status='1')

            for link in chap.url:
                data = new_request(url=link)
                name_chap = data.find('h2', class_='chapter-title').text.strip()
                status = data.find('div', id='chapter-content')['data-vip']

                if status == '1':
                    content = ''
                    url = link
                else:
                    content = str(data.find('div', id='chapter-content'))
                    url = ''

                create_date = data.find_all('header')[1].find_all('p')[2].text.strip().strip('"')
                date_create = datetime.strptime(create_date, '%d/%m/%Y').date()
                Chaper.objects.create(
                    name_chap=name_chap,
                    content=content,
                    status=status,
                    url=url,
                    create_date=date_create
                )

                print(name_chap)
            time.sleep(604800)
        except ObjectDoesNotExist:
            time.sleep(604800)


threading.Thread(target=new_claw).start()
threading.Thread(target=old_crawl).start()
