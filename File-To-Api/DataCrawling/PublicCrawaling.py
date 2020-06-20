# 공공데이터

# 웹 스크래핑
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import pymysql
import time
import pandas as pd

driver = webdriver.Chrome('/Users/sku66/Anaconda3/driver/chromedriver.exe')
driver.implicitly_wait(2)

# 지속적 사용을 위해 함수로 정의
def siteviewAddress(web_address):
    # url에 접근한다,시간을 두어 서버 차단 방지
    time.sleep(2)
    driver.get(web_address)

    # 데이터 제목
    category = driver.find_element_by_css_selector('#contents > div.data-search-view > div.data-set-title > div.tit-area > p').text

    # 데이터 정보
    info = driver.find_element_by_css_selector('#contents > div.data-search-view > div.data-set-title > div.cont').text
    
    # 데이터 분류
    classification = driver.find_element_by_css_selector('#fileDetailTableArea > tbody > tr:nth-child(1) > td:nth-child(1) > div > div > div.th').text

    # 데이터 분류 내용
    classificationInfo = driver.find_element_by_css_selector('#fileDetailTableArea > tbody > tr:nth-child(1) > td:nth-child(1) > div > div > div.td').text
    
    # 데이터 제공기관
    provider = driver.find_element_by_css_selector('#fileDetailTableArea > tbody > tr:nth-child(1) > td:nth-child(2) > div > div > div.th').text

    # 데이터 제공기관 내용
    providerInfo = driver.find_element_by_css_selector('#fileDetailTableArea > tbody > tr:nth-child(1) > td:nth-child(2) > div > div > div.td').text

    # 데이터 제공부서
    providerdep = driver.find_element_by_css_selector('#fileDetailTableArea > tbody > tr:nth-child(2) > td:nth-child(1) > div > div > div.th').text

    # 데이터 제공부서 내용
    providerdepInfo = driver.find_element_by_css_selector('#fileDetailTableArea > tbody > tr:nth-child(2) > td:nth-child(1) > div > div > div.td').text

    # 데이터 이용 범위
    # rangeuse = driver.find_element_by_css_selector('#fileDetailTableArea > tbody > tr:nth-child(14) > td > div > div > div.th').text

    # 데이터 이용 범위 내용
    # rangeuse_info = driver.find_element_by_link_text('#fileDetailTableArea > tbody > tr:nth-child(14) > td > div > div > div.td > a').text

    # 데이터 등록
    enrollment = driver.find_element_by_css_selector('#fileDetailTableArea > tbody > tr:nth-child(8) > td:nth-child(1) > div > div > div.th').text

    # 데이터 등록 내용
    enrollmentInfo = driver.find_element_by_css_selector('#fileDetailTableArea > tbody > tr:nth-child(8) > td:nth-child(1) > div > div > div.td').text

    # 데이터 수정
    modify = driver.find_element_by_css_selector('#fileDetailTableArea > tbody > tr:nth-child(8) > td:nth-child(2) > div > div > div.th').text

    # 데이터 수정 내용
    modifyInfo = driver.find_element_by_css_selector('#fileDetailTableArea > tbody > tr:nth-child(8) > td:nth-child(2) > div > div > div.td').text

    print('-'*50)

    # DB 연결
    conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='mysql',db='microservicedb')
    # DB 연결 확인을 위해 사용
    print('연결완료')

    # 커서 생성
    cursor = conn.cursor()

    # 테이블 생성
    cursor.execute('''create table if not exists publicdatadb(category text,info text,classification text, classificationInfo text, provider text, providerInfo text, providerdep text, providerdepInfo text, enrollment text, enrollmentInfo text, modify text, modifyInfo text);''')

    # DB 반영
    conn.commit()

    # 레코드 삽입
    try:
        cursor.execute('''insert into publicdatadb (category,info,classification, classificationInfo, provider, providerInfo, providerdep, providerdepInfo, enrollment, enrollmentInfo, modify, modifyInfo) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''', (category,info,classification, classificationInfo, provider, providerInfo, providerdep, providerdepInfo, enrollment, enrollmentInfo, modify, modifyInfo))
        # DB 반영
        conn.commit()
    except Exception as e:
        print('err========', e)
        pass

    conn.close()

    
homepage = [
'https://www.data.go.kr/data/3078831/fileData.do',
'https://www.data.go.kr/data/15059928/fileData.do',
'https://www.data.go.kr/data/15059887/fileData.do',
'https://www.data.go.kr/data/3038104/fileData.do',
'https://www.data.go.kr/data/15036538/fileData.do',
'https://www.data.go.kr/data/15036538/fileData.do',
'https://www.data.go.kr/data/15059870/fileData.do',
'https://www.data.go.kr/data/15059869/fileData.do',
'https://www.data.go.kr/data/15059866/fileData.do',
'https://www.data.go.kr/data/3080242/fileData.do',
'https://www.data.go.kr/data/15055425/fileData.do',
'https://www.data.go.kr/data/15055426/fileData.do',
'https://www.data.go.kr/data/3046071/fileData.do',

'https://www.data.go.kr/data/15043191/fileData.do',
'https://www.data.go.kr/data/15059823/fileData.do',
'https://www.data.go.kr/data/15059694/fileData.do',
'https://www.data.go.kr/data/3054797/fileData.do',
'https://www.data.go.kr/data/15059843/fileData.do',
'https://www.data.go.kr/data/15059664/fileData.do',
'https://www.data.go.kr/data/15059837/fileData.do',

'https://www.data.go.kr/data/15059831/fileData.do',
'https://www.data.go.kr/data/15050700/fileData.do',
'https://www.data.go.kr/data/15036135/fileData.do',
'https://www.data.go.kr/data/15059828/fileData.do',
'https://www.data.go.kr/data/15059814/fileData.do',
'https://www.data.go.kr/data/3044165/fileData.do',
'https://www.data.go.kr/data/15059825/fileData.do',
'https://www.data.go.kr/data/15059824/fileData.do',
'https://www.data.go.kr/data/15059812/fileData.do',
'https://www.data.go.kr/data/15059813/fileData.do',

'https://www.data.go.kr/data/15059806/fileData.do',
'https://www.data.go.kr/data/15059803/fileData.do',
'https://www.data.go.kr/data/15059802/fileData.do',
'https://www.data.go.kr/data/15059787/fileData.do',
'https://www.data.go.kr/data/15059671/fileData.do',
'https://www.data.go.kr/data/15054782/fileData.do',
'https://www.data.go.kr/data/3061504/fileData.do',
'https://www.data.go.kr/data/15038456/fileData.do',
'https://www.data.go.kr/data/15059778/fileData.do',
'https://www.data.go.kr/data/15043247/fileData.do',

'https://www.data.go.kr/data/15059770/fileData.do',
'https://www.data.go.kr/data/15052872/fileData.do',
'https://www.data.go.kr/data/15037344/fileData.do',
'https://www.data.go.kr/data/15037345/fileData.do',
'https://www.data.go.kr/data/15005130/fileData.do',
'https://www.data.go.kr/data/3064789/fileData.do',
'https://www.data.go.kr/data/15035819/fileData.do',
'https://www.data.go.kr/data/15053509/fileData.do',
'https://www.data.go.kr/data/3055409/fileData.do',
'https://www.data.go.kr/data/3064792/fileData.do'
]

for i in homepage:
    siteviewAddress(i)

driver.quit()