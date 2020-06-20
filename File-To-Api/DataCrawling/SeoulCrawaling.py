# 서울 데이터

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
    category = driver.find_element_by_css_selector('#frm > div.box-base > h1').text

    # 데이터 정보
    info = driver.find_element_by_css_selector('#frm > div.box-base > div.main-content-txt > p').text
    
    # 데이터 분류
    classification = driver.find_element_by_css_selector('#frm > div:nth-child(10) > div.tbl-base-d.align-l.only-d2 > table > tbody > tr:nth-child(2) > th:nth-child(3)').text

    # 데이터 분류 내용
    classificationInfo = driver.find_element_by_css_selector('#frm > div:nth-child(10) > div.tbl-base-d.align-l.only-d2 > table > tbody > tr:nth-child(2) > td:nth-child(4)').text
    
    # 데이터 제공기관
    provider = driver.find_element_by_css_selector('#frm > div:nth-child(10) > div.tbl-base-d.align-l.only-d2 > table > tbody > tr:nth-child(4) > th:nth-child(1)').text

    # 데이터 제공기관 내용
    providerInfo = driver.find_element_by_css_selector('#frm > div:nth-child(10) > div.tbl-base-d.align-l.only-d2 > table > tbody > tr:nth-child(4) > td:nth-child(2)').text

    # 데이터 제공부서
    providerdep = driver.find_element_by_css_selector('#frm > div:nth-child(10) > div.tbl-base-d.align-l.only-d2 > table > tbody > tr:nth-child(4) > th:nth-child(3)').text

    # 데이터 제공부서 내용
    providerdepInfo = driver.find_element_by_css_selector('#frm > div:nth-child(10) > div.tbl-base-d.align-l.only-d2 > table > tbody > tr:nth-child(4) > td:nth-child(4)').text

    # 데이터 이용 범위
    rangeuse = driver.find_element_by_css_selector('#frm > div:nth-child(10) > div.tbl-base-d.align-l.only-d2 > table > tbody > tr:nth-child(7) > th').text

    # 데이터 이용 범위 내용
    rangeuseInfo = driver.find_element_by_css_selector('#frm > div:nth-child(10) > div.tbl-base-d.align-l.only-d2 > table > tbody > tr:nth-child(7) > td > div').text

    # 데이터 등록
    enrollment = driver.find_element_by_css_selector('#frm > div:nth-child(10) > div.tbl-base-d.align-l.only-d2 > table > tbody > tr:nth-child(1) > th:nth-child(1)').text

    # 데이터 등록 내용
    enrollmentInfo = driver.find_element_by_css_selector('#frm > div:nth-child(10) > div.tbl-base-d.align-l.only-d2 > table > tbody > tr:nth-child(1) > td:nth-child(2) > span').text

    # 데이터 수정
    modify = driver.find_element_by_css_selector('#frm > div:nth-child(10) > div.tbl-base-d.align-l.only-d2 > table > tbody > tr:nth-child(1) > th:nth-child(3)').text

    # 데이터 수정 내용
    modifyInfo = driver.find_element_by_css_selector('#frm > div:nth-child(10) > div.tbl-base-d.align-l.only-d2 > table > tbody > tr:nth-child(1) > td:nth-child(4) > span').text

    print('-'*50)

    # DB 연결
    conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='spring',db='microservicedb')
    # DB 연결 확인을 위해 사용
    print('연결완료')

    # 커서 생성
    cursor = conn.cursor()

    # 테이블 생성
    cursor.execute('''create table if not exists seouldatadb(category text,info text, classification text, classificationInfo text, provider text, providerInfo text, providerdep text, providerdepInfo text, rangeuse text,
        rangeuseInfo text, enrollment text, enrollmentInfo text, modify text, modifyInfo text);''')

    # DB 반영
    conn.commit()

    # 레코드 삽입
    try:
        cursor.execute('''insert into seouldatadb (category,info,classification, classificationInfo, provider, providerInfo, providerdep, providerdepInfo, rangeuse,
        rangeuseInfo, enrollment, enrollmentInfo, modify, modifyInfo) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''', (category,info, classification, classificationInfo, provider, providerInfo, providerdep, providerdepInfo, rangeuse,
        rangeuseInfo, enrollment, enrollmentInfo, modify, modifyInfo))
        # DB 반영
        conn.commit()
    except Exception as e:
        print('err========', e)
        pass

    conn.close()

    
homepage = [
# 보건
'https://data.seoul.go.kr/dataList/10668/S/2/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-365/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-1186/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-1370/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-13663/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15798/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-13452/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-2662/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-2723/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-14840/F/1/datasetView.do',

'https://data.seoul.go.kr/dataList/OA-15078/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15977/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15797/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-12068/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15044/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-13667/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-12967/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-13271/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15179/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-12069/S/1/datasetView.do',

'https://data.seoul.go.kr/dataList/OA-13232/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-13481/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-13640/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15203/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-13462/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-13469/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-12070/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15092/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-13666/F/1/datasetView.do',

# 일반행정
'https://data.seoul.go.kr/dataList/OA-14991/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-12838/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-14991/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-14992/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15989/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15979/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15964/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15964/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15956/F/1/datasetView.do'
'https://data.seoul.go.kr/dataList/OA-15959/S/1/datasetView.do',

'https://data.seoul.go.kr/dataList/OA-12868/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-12920/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-2742/C/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-13272/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-2743/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-11674/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-11680/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-12917/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15809/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15568/S/1/datasetView.do',

'https://data.seoul.go.kr/dataList/OA-15572/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15560/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15573/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15582/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-13284/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15565/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-13270/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-12649/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-13506/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15559/F/1/datasetView.do',

'https://data.seoul.go.kr/dataList/OA-15441/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15440/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15439/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15377/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15193/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-1162/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-13478/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-13465/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-12872/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-14982/F/1/datasetView.do',

'https://data.seoul.go.kr/dataList/OA-14983/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-14979/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-14980/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-14978/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-14981/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-12861/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-13226/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-13228/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-12799/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-1157/F/1/datasetView.do',

# 문화 관광
'https://data.seoul.go.kr/dataList/OA-12961/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-12943/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15768/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15767/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-1115/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15005/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15651/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15592/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15082/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15073/F/1/datasetView.do',

'https://data.seoul.go.kr/dataList/OA-15139/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15057/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15018/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15019/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-12988/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15378/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-13494/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-13665/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-13482/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-13472/F/1/datasetView.do',

'https://data.seoul.go.kr/dataList/OA-13497/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-13471/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-13466/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15464/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15462/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15463/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-2788/C/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-2790/C/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15556/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15555/F/1/datasetView.do',

'https://data.seoul.go.kr/dataList/OA-15524/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15112/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15031/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15030/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15087/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15272/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15254/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15097/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15369/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15098/S/1/datasetView.do',

'https://data.seoul.go.kr/dataList/OA-15164/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15100/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-13468/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-13470/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-13479/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-2251/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-12907/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-13684/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-13540/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-13536/S/1/datasetView.do',

# 복지
'https://data.seoul.go.kr/dataList/OA-15962/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15976/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15963/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-12942/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-11595/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OP-6/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-13276/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-242/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-240/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-13274/F/1/datasetView.do',

'https://data.seoul.go.kr/dataList/OA-12935/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15812/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15001/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15178/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15760/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-2792/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-14665/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-13476/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-13495/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-11564/F/1/datasetView.do',

'https://data.seoul.go.kr/dataList/OA-11565/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-12005/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-12003/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15166/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15525/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15024/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-13833/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15028/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15319/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15289/F/1/datasetView.do',

'https://data.seoul.go.kr/dataList/OA-15285/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15301/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15286/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15315/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15052/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15299/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15296/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15297/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-13695/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15302/F/1/datasetView.do',

'https://data.seoul.go.kr/dataList/OA-15294/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15291/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-13698/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-13756/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15287/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15316/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15318/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-13766/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15308/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-13753/F/1/datasetView.do',

# 환경
'https://data.seoul.go.kr/dataList/OA-2218/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-2221/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-2220/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-2501/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15968/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15975/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15974/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15966/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15969/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15960/S/1/datasetView.do',

'https://data.seoul.go.kr/dataList/OA-15971/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15978/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15982/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-11986/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15526/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-11987/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-11993/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-11985/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-11992/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-12000/S/1/datasetView.do',

'https://data.seoul.go.kr/dataList/OA-12002/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-11989/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-12001/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-11991/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-11994/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-11988/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-11999/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-13278/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15095/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15069/F/1/datasetView.do',

'https://data.seoul.go.kr/dataList/OA-15762/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15004/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15010/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15002/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15011/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-13491/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15635/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-13486/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-13464/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-13473/F/1/datasetView.do',

'https://data.seoul.go.kr/dataList/OA-13490/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-13493/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-394/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15473/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15040/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15140/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15386/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15146/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15068/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15084/S/1/datasetView.do',

# 교육
'https://data.seoul.go.kr/dataList/OA-11604/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-13279/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-13273/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-13280/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-13282/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-13488/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-2730/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-12875/F/1/datasetView.do',

# 안전
'https://data.seoul.go.kr/dataList/OA-15983/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15967/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15965/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15972/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15981/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15961/F/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-15958/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-14999/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-12811/S/1/datasetView.do',
'https://data.seoul.go.kr/dataList/OA-12812/S/1/datasetView.do',

'https://data.seoul.go.kr/dataList/OA-12813/S/1/datasetView.do',
'',
'',
'',
'',
'',
'',
'',
'',
'',

'',
'',
'',
'',
'',
'',
'',
'',
'',
'',

'',
'',
'',
'',
'',
'',
'',
'',
'',
'',
]

for i in homepage:
    siteviewAddress(i)

driver.quit()