from bs4 import BeautifulSoup as BS
import requests

# Поиск работы с work.ua по запросу "python developer" за последние сутки
# ВЕРСИЯ 2!!!

list = []


def find_work_ua():
    url = 'https://www.work.ua/ru/jobs-python+developer/?_pjax=%23pjax-job-list&days=122'
    r = requests.get(url)
    soup = BS(r.text, 'lxml')
    tag_h2 = soup.find_all('h2', attrs={'class': ''})
    for a in tag_h2:
        a_tag = a.find('a')
        try:
            title = a_tag['title']
            link = "https://www.work.ua" + a_tag['href']
            list.append(str(title + ' ' + link))
        except BaseException:
            TypeError
            break


find_work_ua()
