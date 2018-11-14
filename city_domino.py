# -*- coding: utf-8 -*-
from pypinyin import lazy_pinyin
from collections import defaultdict
import random

def loadCityList(txt):
    '''
    记载存储于txt文件中的城市列表。
    :param txt: 存储有城市列表的txt文件
    :return cities: 城市名称集合
    '''
    with open(txt, 'r') as f:
        cities = f.readlines()
    cities = [city.strip() for city in cities]
    cities = set(cities) # 去重
    return cities

def getCityDict(city_list):
    '''
    得到一个键为拼音，键值为城市列表的字典，用于接龙查询。
    :param city_list: 包含城市名称的列表/元组/集合等
    :PY2city_dict: 形式为{'hai':['海淀']}的字典
    '''
    PY2city_dict = defaultdict(list)
    for city in city_list:
        pinyin = lazy_pinyin(city[0])[0]
        PY2city_dict[pinyin].append(city)
    return PY2city_dict
   
def findNextCity(city):
    '''
    根据城市名称最后一个字的拼音查询下一个接龙的城市
    :param city: 要查询的城市
    :return next_city: 接龙的下一个城市；若无，则返回None 
    '''
    pinyin = lazy_pinyin(city[-1])[0]
    if pinyin not in pinyin_keys:
        return None
    city_list = PY2city_dict[pinyin]
    next_city = random.choice(city_list)
    return next_city

def cityDomino(max_epoch=20):
    '''
    在一个带有最大次数的while循环中，进行城市接龙，直至遇到None终止。
    :param max_epoch: 最大接龙的次数
    :return None:
    '''
    city = input('请输入首先要接龙的城市:')
    index = 0
    while True:
        if index > max_epoch: # 接龙次数检查
            print('达到最大接龙次数，最大接龙次数为：%d' % max_epoch)
            break
        city = findNextCity(city)
        if city is None:
            print('黔驴技穷，下面没有城市了。')
            break
        print('下一个城市是：%s' % city)
        index += 1




if __name__ == '__main__':
    max_epoch = 20       
    txt = 'city_list.txt'
    city_list = loadCityList(txt)
    PY2city_dict = getCityDict(city_list)
    pinyin_keys = PY2city_dict.keys() # 减少keys()的调用次数
    cityDomino(max_epoch)
