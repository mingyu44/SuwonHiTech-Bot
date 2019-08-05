from bs4 import BeautifulSoup
import requests
from datetime import date
import re

# cleanning function
def clean_text(text):
    cleaned_text = re.sub('[a-zA-GI-Z]', '', text)
    cleaned_text = re.sub('[H]', '\n', cleaned_text)
    cleaned_text = re.sub('[\{\}\[\]\/?,.;|\)~`!^\-_+<>@\#$%&\\\=\(\'\"" "]', '', cleaned_text)
    cleaned_text = re.sub('[0-9]', '', cleaned_text)
    return cleaned_text

def the_day_before_yesterday_food_list(self, update):
    today = date.today()  # 오늘의 년, 월, 일을 호출
    today.year, today.month, today.day  # 오늘의 년, 월, 일을 저장
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
    addr = 'http://sht.hs.kr/?_page=41&_action=view&_view=view&yy='+str(today.year)+'&mm='+str(today.month)+'&dd='+str(today.day-2)
    self.addr = addr
    food = requests.get(self.addr, headers = header)
    soup = BeautifulSoup(food.text, 'html.parser')

    titles = soup.select('div > dl')
    day: str = "수원하이텍고등학교\n"+str(today.year)+"년 "+str(today.month)+"월 "+str(today.day-2)+"일 식단"
    update.message.reply_text(day)
    for n in titles:
        update.message.reply_text(clean_text(n.get_text()))

def yesterday_food_list(self, update):
    today = date.today()  # 오늘의 년, 월, 일을 호출
    today.year, today.month, today.day  # 오늘의 년, 월, 일을 저장
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
    addr = 'http://sht.hs.kr/?_page=41&_action=view&_view=view&yy='+str(today.year)+'&mm='+str(today.month)+'&dd='+str(today.day-1)
    self.addr = addr
    food = requests.get(self.addr, headers = header)
    soup = BeautifulSoup(food.text, 'html.parser')

    titles = soup.select('div > dl')
    day: str = "수원하이텍고등학교\n"+str(today.year)+"년 "+str(today.month)+"월 "+str(today.day-1)+"일 식단"
    update.message.reply_text(day)
    for n in titles:
        update.message.reply_text(clean_text(n.get_text()))

def today_food_list(self, update):
    today = date.today()  # 오늘의 년, 월, 일을 호출
    today.year, today.month, today.day  # 오늘의 년, 월, 일을 저장
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
    addr = 'http://sht.hs.kr/?_page=41&_action=view&_view=view&yy='+str(today.year)+'&mm='+str(today.month)+'&dd='+str(today.day)
    self.addr = addr
    food = requests.get(self.addr, headers = header)
    soup = BeautifulSoup(food.text, 'html.parser')

    titles = soup.select('div > dl')
    day: str = "수원하이텍고등학교\n"+str(today.year)+"년 "+str(today.month)+"월 "+str(today.day)+"일 식단"
    update.message.reply_text(day)
    for n in titles:
        update.message.reply_text(clean_text(n.get_text()))

def tomorrow_food_list(self, update):
    today = date.today()  # 오늘의 년, 월, 일을 호출
    today.year, today.month, today.day  # 오늘의 년, 월, 일을 저장
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
    addr = 'http://sht.hs.kr/?_page=41&_action=view&_view=view&yy='+str(today.year)+'&mm='+str(today.month)+'&dd='+str(today.day+1)
    self.addr = addr
    food = requests.get(self.addr, headers = header)
    soup = BeautifulSoup(food.text, 'html.parser')

    titles = soup.select('div > dl')
    day: str = "수원하이텍고등학교\n"+str(today.year)+"년 "+str(today.month)+"월 "+str(today.day+1)+"일 식단"
    update.message.reply_text(day)
    for n in titles:
        update.message.reply_text(clean_text(n.get_text()))

def the_day_after_tomorrow_food_list(self, update):
    today = date.today()  # 오늘의 년, 월, 일을 호출
    today.year, today.month, today.day  # 오늘의 년, 월, 일을 저장
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
    addr = 'http://sht.hs.kr/?_page=41&_action=view&_view=view&yy='+str(today.year)+'&mm='+str(today.month)+'&dd='+str(today.day+2)
    self.addr = addr
    food = requests.get(self.addr, headers = header)
    soup = BeautifulSoup(food.text, 'html.parser')

    titles = soup.select('div > dl')
    day: str = "수원하이텍고등학교\n"+str(today.year)+"년 "+str(today.month)+"월 "+str(today.day+2)+"일 식단"
    update.message.reply_text(day)
    for n in titles:
        update.message.reply_text(clean_text(n.get_text()))