# 경기 데이터 드림

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
    category = driver.find_element_by_css_selector('body > div.layout_A > div.wrap_layout_flex > div.layout_flex_100 > div.layout_flex > div > div.detail_summary > div > strong').text

    # 데이터 정보
    info = driver.find_element_by_css_selector('body > div.layout_A > div.wrap_layout_flex > div.layout_flex_100 > div.layout_flex > div > div.detail_summary > div > span').text
    
    # 데이터 분류
    classification = driver.find_element_by_css_selector('#metaTbody > tr:nth-child(1) > th:nth-child(1)').text

    # 데이터 분류 내용
    classificationInfo = driver.find_element_by_css_selector('#metaTbody > tr:nth-child(1) > td:nth-child(2)').text
    
    # 데이터 제공기관
    provider = driver.find_element_by_css_selector('#metaTbody > tr:nth-child(3) > th:nth-child(1)').text

    # 데이터 제공기관 내용
    providerInfo = driver.find_element_by_css_selector('#metaTbody > tr:nth-child(3) > td:nth-child(2)').text

    # 데이터 제공부서
    providerdep = driver.find_element_by_css_selector('#metaTbody > tr:nth-child(4) > th:nth-child(1)').text

    # 데이터 제공부서 내용
    providerdepInfo = driver.find_element_by_css_selector('#metaTbody > tr:nth-child(4) > td:nth-child(2)').text

    # 데이터 이용 범위
    rangeuse = driver.find_element_by_css_selector('#metaTbody > tr:nth-child(5) > th:nth-child(1)').text

    # 데이터 이용 범위 내용
    rangeuseInfo = driver.find_element_by_css_selector('#metaTbody > tr:nth-child(5) > td:nth-child(2)').text

    # 데이터 등록
    enrollment = driver.find_element_by_css_selector('#metaTbody > tr:nth-child(1) > th:nth-child(3)').text

    # 데이터 등록 내용
    enrollmentInfo = driver.find_element_by_css_selector('#metaTbody > tr:nth-child(1) > td:nth-child(4)').text

    # 데이터 수정
    modify = driver.find_element_by_css_selector('#metaTbody > tr:nth-child(2) > th:nth-child(3)').text

    # 데이터 수정 내용
    modifyInfo = driver.find_element_by_css_selector('#metaTbody > tr:nth-child(2) > td:nth-child(4)').text

    print('-'*50)

    # DB 연결
    conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='mysql',db='microservicedb')
    # DB 연결 확인을 위해 사용
    print('연결완료')

    # 커서 생성
    cursor = conn.cursor()

    # 테이블 생성
    cursor.execute('''create table if not exists ggdatadb(category text,info text,classification text, classificationInfo text, provider text, providerInfo text, providerdep text, providerdepInfo text, rangeuse text,
        rangeuseInfo text, enrollment text, enrollmentInfo text, modify text, modifyInfo text);''')

    # DB 반영
    conn.commit()

    # 레코드 삽입
    try:
        cursor.execute('''insert into ggdatadb (category,info,classification, classificationInfo, provider, providerInfo, providerdep, providerdepInfo, rangeuse,
        rangeuseInfo, enrollment, enrollmentInfo, modify, modifyInfo) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''', (category,info,classification, classificationInfo, provider, providerInfo, providerdep, providerdepInfo, rangeuse,
        rangeuseInfo, enrollment, enrollmentInfo, modify, modifyInfo))
        # DB 반영
        conn.commit()
    except Exception as e:
        print('err========', e)
        pass

    conn.close()

    
homepage = [
'https://data.gg.go.kr/portal/data/service/selectServicePage.do?page=1&rows=10&sortColumn=&sortDirection=&infId=11LHDXODQMC7T9J2IVLD29925089&infSeq=1&order=&srvCd=F',
'https://data.gg.go.kr/portal/data/service/selectServicePage.do?page=1&rows=50&sortColumn=&sortDirection=&infId=U6LZ83TORFHFRS89I5VI29831630&infSeq=1&order=&srvCd=F',
'https://data.gg.go.kr/portal/data/service/selectServicePage.do?page=1&rows=10&sortColumn=&sortDirection=&infId=JWYIFGNEOZ5WXZYTIU1829824589&infSeq=1&order=&srvCd=F',
'https://data.gg.go.kr/portal/data/service/selectServicePage.do?page=1&rows=10&sortColumn=&sortDirection=&infId=D4JTYVX2H8YIRO3MZJOG29815746&infSeq=1&order=&srvCd=F',
'https://data.gg.go.kr/portal/data/service/selectServicePage.do?page=1&rows=10&sortColumn=&sortDirection=&infId=3NPA52LBMO36CQEQ1GMY28894927&infSeq=1&order=&srvCd=F',
'https://data.gg.go.kr/portal/data/service/selectServicePage.do?page=1&rows=10&sortColumn=&sortDirection=&infId=LJ9Z18Z5KLJ1M32VO1BK27178834&infSeq=1&order=&srvCd=F',
'https://data.gg.go.kr/portal/data/service/selectServicePage.do?page=1&rows=10&sortColumn=&sortDirection=&infId=6OCWFQQYK6U2PD0FKSMV27162290&infSeq=1&order=&srvCd=F',
'https://data.gg.go.kr/portal/data/service/selectServicePage.do?page=1&rows=10&sortColumn=&sortDirection=&infId=F05BMWU0UTSQP6PKWLAC27185478&infSeq=1&order=&srvCd=F',
'https://data.gg.go.kr/portal/data/service/selectServicePage.do?page=1&rows=10&sortColumn=&sortDirection=&infId=7M4X3RD0DASA6C1DZO6727155107&infSeq=1&order=&srvCd=F',
'https://data.gg.go.kr/portal/data/service/selectServicePage.do?page=1&rows=10&sortColumn=&sortDirection=&infId=458YRRY04VI3BBMI6Q8326869752&infSeq=1&order=&srvCd=F',

'https://data.gg.go.kr/portal/data/service/selectServicePage.do?page=2&rows=10&sortColumn=&sortDirection=&infId=E5RTWGNKKYKBO2GI67KF24613201&infSeq=1&order=&srvCd=F',
'https://data.gg.go.kr/portal/data/service/selectServicePage.do?page=2&rows=10&sortColumn=&sortDirection=&infId=GE0DUHTX3VX0GL4R0LUS26448884&infSeq=1&order=&srvCd=F',
'https://data.gg.go.kr/portal/data/service/selectServicePage.do?page=2&rows=10&sortColumn=&sortDirection=&infId=3FDL33MCKWEK0QSUBZEX26385664&infSeq=1&order=&srvCd=F',
'https://data.gg.go.kr/portal/data/service/selectServicePage.do?page=2&rows=10&sortColumn=&sortDirection=&infId=40N2ILE9CI9755NV2HCQ26377202&infSeq=1&order=&srvCd=F',
'https://data.gg.go.kr/portal/data/service/selectServicePage.do?page=2&rows=10&sortColumn=&sortDirection=&infId=MKZXCAMJLSQN29LYQP1026363567&infSeq=1&order=&srvCd=F',
'https://data.gg.go.kr/portal/data/service/selectServicePage.do?page=2&rows=10&sortColumn=&sortDirection=&infId=NZKDUBX2CW4PU52T04P526356080&infSeq=1&order=&srvCd=F',
'https://data.gg.go.kr/portal/data/service/selectServicePage.do?page=2&rows=10&sortColumn=&sortDirection=&infId=VQNTNO356OS2N9YGQR2W26347730&infSeq=1&order=&srvCd=F',
'https://data.gg.go.kr/portal/data/service/selectServicePage.do?page=2&rows=10&sortColumn=&sortDirection=&infId=FTUQ6VY3G70RT32NIYB824437081&infSeq=1&order=&srvCd=F',
'https://data.gg.go.kr/portal/data/service/selectServicePage.do?page=2&rows=10&sortColumn=&sortDirection=&infId=JBTU5JH49NBV11K1CFVL24468331&infSeq=1&order=&srvCd=F',
'https://data.gg.go.kr/portal/data/service/selectServicePage.do?page=2&rows=10&sortColumn=&sortDirection=&infId=VORGL6BO90JZ56XJ3ZAR24489943&infSeq=1&order=&srvCd=F',

'https://data.gg.go.kr/portal/data/service/selectServicePage.do?page=3&rows=10&sortColumn=&sortDirection=&infId=7GZ08I0JWSNPY5NVMLLG24313533&infSeq=1&order=&srvCd=F',
'https://data.gg.go.kr/portal/data/service/selectServicePage.do?page=3&rows=10&sortColumn=&sortDirection=&infId=A8F378W1HRG03Q4GJHT423038583&infSeq=1&order=&srvCd=F',
'https://data.gg.go.kr/portal/data/service/selectServicePage.do?page=3&rows=10&sortColumn=&sortDirection=&infId=Q5FEF7YLDX69L0Z9A1PL25845033&infSeq=1&order=&srvCd=F',
'https://data.gg.go.kr/portal/data/service/selectServicePage.do?page=3&rows=10&sortColumn=&sortDirection=&infId=WCKQVVNWL0D0HPPI738V21581030&infSeq=1&order=&srvCd=F',
'https://data.gg.go.kr/portal/data/service/selectServicePage.do?page=3&rows=10&sortColumn=&sortDirection=&infId=SE00GA6F273B8PIJ9N8412495661&infSeq=1&order=&srvCd=F',
'https://data.gg.go.kr/portal/data/service/selectServicePage.do?page=3&rows=10&sortColumn=&sortDirection=&infId=A91URXA8A9FY540F466112483728&infSeq=1&order=&srvCd=F',
'https://data.gg.go.kr/portal/data/service/selectServicePage.do?page=3&rows=10&sortColumn=&sortDirection=&infId=LOQBL0HZKV2285NJW2742364178&infSeq=1&order=&srvCd=F',
'https://data.gg.go.kr/portal/data/service/selectServicePage.do?page=3&rows=10&sortColumn=&sortDirection=&infId=18SI9BJ6M874FNBOOOTU23125858&infSeq=2&order=&srvCd=F',
'https://data.gg.go.kr/portal/data/service/selectServicePage.do?page=3&rows=10&sortColumn=&sortDirection=&infId=9QE9R7J9FUO2M9B61RSK23165883&infSeq=2&order=&srvCd=F',
'https://data.gg.go.kr/portal/data/service/selectServicePage.do?page=3&rows=10&sortColumn=&sortDirection=&infId=T1GIZXW138UFEI37C4VT23081025&infSeq=2&order=&srvCd=F',

'https://data.gg.go.kr/portal/data/service/selectServicePage.do?page=4&rows=10&sortColumn=&sortDirection=&infId=GDJLQPFFEO8ZDSBGLHUH23174624&infSeq=2&order=&srvCd=F',
'https://data.gg.go.kr/portal/data/service/selectServicePage.do?page=4&rows=10&sortColumn=&sortDirection=&infId=4MLBJ5U38EIFORNSGMVX30253465&infSeq=1&order=&srvCd=F',
'https://data.gg.go.kr/portal/data/service/selectServicePage.do?page=4&rows=10&sortColumn=&sortDirection=&infId=0NNBZ7DDRNF06QNHASNG30219902&infSeq=1&order=&srvCd=F',
'https://data.gg.go.kr/portal/data/service/selectServicePage.do?page=4&rows=10&sortColumn=&sortDirection=&infId=RSJ4YZM6B2QXOZHCLRW530118642&infSeq=2&order=&srvCd=F',
'https://data.gg.go.kr/portal/data/service/selectServicePage.do?page=4&rows=10&sortColumn=&sortDirection=&infId=VJQJ8GTYST96VK2HMBV228914540&infSeq=1&order=&srvCd=F',
'https://data.gg.go.kr/portal/data/service/selectServicePage.do?page=4&rows=10&sortColumn=&sortDirection=&infId=0KLYKG5LQB1QH2KFDZXB28764697&infSeq=1&order=&srvCd=F',
'https://data.gg.go.kr/portal/data/service/selectServicePage.do?page=4&rows=10&sortColumn=&sortDirection=&infId=WH7U7BE9K607ILDYY9M728653227&infSeq=1&order=&srvCd=F',
'https://data.gg.go.kr/portal/data/service/selectServicePage.do?page=4&rows=10&sortColumn=&sortDirection=&infId=8K0GGR6DK66K0CI0EBQM27782533&infSeq=1&order=&srvCd=F',
'https://data.gg.go.kr/portal/data/service/selectServicePage.do?page=4&rows=10&sortColumn=&sortDirection=&infId=DOHJI4WO89HA199ID7O327322770&infSeq=1&order=&srvCd=F',
'https://data.gg.go.kr/portal/data/service/selectServicePage.do?page=4&rows=10&sortColumn=&sortDirection=&infId=ANVATTK0JI5D7QWAIAJ727293595&infSeq=1&order=&srvCd=F',

'https://data.gg.go.kr/portal/data/service/selectServicePage.do?page=5&rows=10&sortColumn=&sortDirection=&infId=STUW1T3URZZTNPBOQTKJ27288772&infSeq=1&order=&srvCd=F',
'https://data.gg.go.kr/portal/data/service/selectServicePage.do?page=5&rows=10&sortColumn=&sortDirection=&infId=HB6LHUQLCTOGO4V4DR2O27113514&infSeq=1&order=&srvCd=F',
'https://data.gg.go.kr/portal/data/service/selectServicePage.do?page=5&rows=10&sortColumn=&sortDirection=&infId=T9IVBG3L4HZPG9NAIG1A27097727&infSeq=1&order=&srvCd=F',
'https://data.gg.go.kr/portal/data/service/selectServicePage.do?page=5&rows=10&sortColumn=&sortDirection=&infId=XDNLMTHN9F17MOPZ2V1A27054880&infSeq=1&order=&srvCd=F',
'https://data.gg.go.kr/portal/data/service/selectServicePage.do?page=5&rows=10&sortColumn=&sortDirection=&infId=AQ5AMMLCM6G1FYUQEHMD26742491&infSeq=1&order=&srvCd=F',
'https://data.gg.go.kr/portal/data/service/selectServicePage.do?page=5&rows=10&sortColumn=&sortDirection=&infId=6R9LFCJNIO5I0WOM1GCV26738542&infSeq=1&order=&srvCd=F',
'https://data.gg.go.kr/portal/data/service/selectServicePage.do?page=5&rows=10&sortColumn=&sortDirection=&infId=DFEVT4P0BE3GU17D50I526724122&infSeq=1&order=&srvCd=F',
'https://data.gg.go.kr/portal/data/service/selectServicePage.do?page=5&rows=10&sortColumn=&sortDirection=&infId=0VICG0GQTW429HLUHU9926712535&infSeq=1&order=&srvCd=F',
'https://data.gg.go.kr/portal/data/service/selectServicePage.do?page=5&rows=10&sortColumn=&sortDirection=&infId=PQCO9P873ISZLUOD8IS326706494&infSeq=1&order=&srvCd=F',
'https://data.gg.go.kr/portal/data/service/selectServicePage.do?page=5&rows=10&sortColumn=&sortDirection=&infId=SB49M5REDTJ7FV678S3L26693970&infSeq=1&order=&srvCd=F'
]

for i in homepage:
    siteviewAddress(i)

driver.quit()