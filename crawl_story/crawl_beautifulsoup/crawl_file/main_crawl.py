from bs4 import BeautifulSoup
import requests
from datetime import datetime, time
import time
from check_file import new_request, get_story, check_day, create_chaper, crawl_chaper
import django
import os
from django.core.exceptions import ObjectDoesNotExist


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Crawler.settings")
django.setup()

while True:
	# html_doc = requests.get(url=url).text
	soup = new_request(url)
	number = int(url.split('/')[-2])
	url = url.replace(str(number), str(number+1))
	content = soup.find_all('li', class_='story-list')
	for item in content:
		time_stamp = int(item.find('i', class_='last-updated').text)
		time_delta = datetime.now() - datetime.fromtimestamp(time_stamp)
		sum_seconds = time_delta.total_seconds()
		if (sum_seconds <= 5200):
			link_url = item.find("a", class_='thumb')['href']
			print(link_url)
		else:
			break
