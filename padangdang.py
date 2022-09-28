
import requests
import parsel
import csv
import time

f=open('数据.csv',mode='a',encoding='utf-8-sig',newline='')
csv_writer=csv.DictWriter(f,fieldnames=[
                                        '书名',
                                         '作者',
                                          '评价',
                                         '出版社',
                                        '出版日期',
                                         '原价',
                                         '售价',
                                         '电子书',
                                         '详情页'])
csv_writer.writeheader()


url='http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-recent7-0-0-1-1'
headers={
                 'user-Agent ':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70'
    }
response= requests.get(url=url,headers=headers)
selector=parsel.Selector(response.text)
list=selector.css(' ul.bang_list li')#是一个列表  每一个元素都表示一个selecor对象
for li in list:
        title=li.css('.name a::attr(title)').get()
        comment = li.css('.star a::text').get()
        writer = li.css('.publisher_info a::text').get()
        recommend = li.css('.tuijian a::text').get()
        public = li.css('div:nth-child(6) a::text').get() #出版社
        publicdate = li.css('div:nth-child(6) span::text').get()
        price_r=li.css('.price_r::text').get()#原价
        price_n = li.css('.price_n::text').get()  # 售价
        price_e = li.css('.price_e span::text').get()  # 电子书
        herf=li.css('.name a href::attr(href)').get()
        dic={
             '书名':title,
            '作者':writer,
            '评价':recommend,
            '出版社':public,
            '出版日期':publicdate,
            '原价':price_r,
            '售价': price_n,
            '电子书': price_e,
            '详情页':herf,
        }
        csv_writer.writerow(dic)
        print(dic)