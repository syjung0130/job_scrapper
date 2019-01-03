#-*- coding:utf-8 -*-
from __future__ import unicode_literals
import sys
import urllib
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from urllib.request import urlopen
from bs4 import BeautifulSoup
import chardet

str_search_base = "http://www.saramin.co.kr/zf_user/search?search_area=main&search_done=y&search_optional_item=n&searchType=recently&searchword="
#"Linux C C++"
str_search_keyword = "Linux%20C%20C%2B%2B"
str_total_word = str_search_base+str_search_keyword

html = bytes('', encoding='utf-8')
str_html = ""
try:
    print('=== scrapper ===')
    str_total_word = str_search_base+str_search_keyword
    html = urlopen(str_total_word).read()
    print("success..")

    print('*** encoding type: {0}'.format(chardet.detect(html)))
    str_html = html.decode('utf-8', 'ignore')
    # print('type: {0}, html: \n{1}'.format(type(str_html), str_html))

except HTTPError as e:
    print("exception 1")
    print(e.code)
except URLError as e:
    print("exception 2")
    print(e.code)

# html = urlopen(str_total_word).read()
# # sys.stdout.buffer.write(html)

# print('*** encoding type: {0}'.format(chardet.detect(html)))
# str_html = html.decode('utf-8', 'ignore')
# print('type: {0}, html: \n{1}'.format(type(str_html), str_html))

# # BeautifulSoup으로 html소스를 python객체로 변환하기
# # 첫 인자는 html소스코드, 두 번째 인자는 어떤 parser를 이용할지 명시.
# # 이 글에서는 Python 내장 html.parser를 이용했다.
# soup = BeautifulSoup(html, 'html.parser')
# #recruit_info_list > ul > li:nth-child(1) > div > div > h2 > a

# # print(soup.h1)

# all_text = soup.findAll("a")
# # all_text = soup.find(id="recruit_info_list")
# # all_text = soup.findAll("a", href="recruit_info_list")
# # print(all_text)
# # print(len(all_text))
# print(type(all_text))

# print(all_text[4].get_text())

# title_list = []
# for text in all_text:
#     print(type(text))
#     # title = text.findAll("div", "sri_layer_tooltip") # text not all_text
#     # print(len(title))
#     # title_list.append(title)

# # print("========== recruit info list ==========")
# # for recruit_info in recruit_info_list:
# #     print(recruit_info.text)
# #     print(recruit_info.get('href'))


# # html = urlopen(str_total_word).read()
# # type(str_total_word)
# # type(html)
# # print(html)