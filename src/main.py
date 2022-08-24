"""
Created on Sun Jun 12 21:19:50 2022
@author: Michio Kim
"""
import requests
from bs4 import BeautifulSoup
import html2text
from dataclasses import dataclass
from datetime import datetime

base_url = 'http://www.trekkingclub.ru/zyvalinka/'
r = requests.get(base_url)


from parsers import datatime_parser, emoji_parser, page_parser


@dataclass
class NGKmassage:
    src_msg: str
    author: str
    parser_massage: str
    datetime: datetime

msg_list = []

for i in page_parser(r.text):
    parser_massage = html2text.html2text(html = str(i.select_one('div')))
    parser_massage = emoji_parser(parser_massage)
    cur_msg = NGKmassage(
        src_msg=i,
        author=i.select_one('b').text,
        parser_massage=parser_massage,
        datetime=datatime_parser(i.select_one('td[align=right]').text)
    )
    msg_list.append(cur_msg)


for i in msg_list:
    print(i.author)
    print(i.parser_massage)
