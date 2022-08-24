from datetime import datetime
import re

from bs4 import BeautifulSoup

def page_parser(page_data: str) -> list:
    msg_re = 'table[align="center"]' # Основная регулярка для поиска отдельных сообщений
    soup = BeautifulSoup(page_data, 'lxml')
    return list(soup.select(msg_re))


def emoji_parser(massage_data: str) -> str:
    'Функция ищет все смайлики в сообщении и заменяет их на удобочитаемое'

    re_msg = '(\!\[\]\((.*?)\))'

    r = re.findall(pattern=re_msg, string=massage_data)    
 
    for i in r:        
        massage_data = massage_data.replace(i[0], i[1], 1)
        
    return massage_data

def datatime_parser(str_data: str) -> datetime:
    'Превращает дату в нормальный datatime'        
    
    mon = {
        'января': 1,
        'февраля': 2,
        'марта': 3,
        'апреля': 4,
        'мая': 5,
        'июня': 6,
        'июля': 7,
        'августа': 8,
        'сентября': 9,
        'октября': 10,
        'ноября': 11,
        'декабря': 12
    }    

    # Это костыль из split. Моих мозгов, желания и времени не хватило что бы переписать 
    # это на регулярные выражения, оно работает и бог с ним
    time = str_data.split(',')[-1].split()[-1]
    data_list = str_data.split(',')[-2].split()[:-1]
    data_list[-2] = mon[data_list[-2]]
    data_str = f'{data_list[0]}/{data_list[1]}/{data_list[2]} {time}'
    
    timestamp = datetime.strptime(data_str, "%d/%m/%Y %H:%M").timestamp()
    
    return  timestamp