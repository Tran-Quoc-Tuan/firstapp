import scrapy
import os
import django
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Crawler.settings")
django.setup()

from crawler_story.models import Category, Story, Chaper


def build_content(list_content):
    content = ''
    for item in list_content:
        content = content+item+'<br>'
    return content


class CrawlSpider(scrapy.Spider):
    name = 'crawler'
    start_urls = [
        'https://webtruyen.com/all/',
    ]

    def parse(self, response):
        url = response.css('ul.pagination li a::attr(href)').getall()[2]
        number = int(url.split('/')[-2])

        while True:
            next_page = url.replace(str(number), str(number-1))
            story_list = response.css("li.story-list a.thumb::attr(href)").getall()

            for story in story_list:
                yield scrapy.Request(story, self.crawl_story)

            yield scrapy.Request(next_page, self.parse)

    def crawl_story(self, response):
        next_page = response.css('a.read-btn::attr(href)').get()
        title = response.css("h1.title::text").get()
        content_story = response.css("div.description").get()
        category = response.css("p.story_categories span a::attr(title)").getall()
        status = response.css("div.infos p::text").getall()[4]
        author = response.css("p.author span a::attr(title)").get()
        image = response.css('div.thumb img::attr(src)').get()
        time_refresh = response.css('div.infos p::text').getall()[5].strip()
        date_time = datetime.strptime(time_refresh, '%H:%M:%S %d/%m/%Y')
        create = Story.objects.create(
            name_story=title,
            content_story=content_story,
            status=status,
            author=author,
            image=image,
            date_refresh=date_time
        )

        for item in category:
            try:
                a = Category.objects.get(categorys=item)
            except ObjectDoesNotExist:
                a = Category.objects.create(categorys=item)
            create.categorys.add(a)

            yield scrapy.Request(next_page, self.chaper)

    def chaper(self, response):
        name_chap = response.css('h2.chapter-title::text').get()
        next_page = response.css('a.chap-nav::attr(href)').getall()[1]
        status = response.css("div#chapter-content::attr('data-vip')").get()

        if status == '1':
            content = ''
            url = response.url
        else:
            list_content = response.css("div#chapter-content::text").getall()
            content = build_content(list_content=list_content)
            url = ''

        name_story = response.css('p.story-title a::text').get().strip()
        author = response.css("header p::text").get().strip()
        truyen = Story.objects.get(name_story=name_story, author=author)
        create_date = response.css("header p::text").getall()[1].strip()
        date = datetime.strptime(create_date, '%d/%m/%Y').date()
        Chaper.objects.create(
            name_chap=name_chap,
            content=content,
            name_story=truyen,
            status=status,
            url=url,
            create_date=date
        )

        if next_page != '#':
            yield scrapy.Request(next_page, self.chaper)
