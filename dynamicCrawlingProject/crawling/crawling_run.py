# crawling\\crawling_run.py

# 동적 웹 크롤링 구동하는 파이썬 스크립트

# 동적 웹 크롤링 : selenium 모듈 사용함 => 외부 패키지 이므로 설치해야 함
'''
selenium 모듈은 웹브라우저와 연동해서,
브라우저에 입력된 웹사이트와 이 사이트의 검색 필드의 검색 키워드를
파이썬을 통해서 입력받아서 해당 사이트로 전송해서
검색 필드 태그의 값으로 적용시켜서 검색을 실행하게 함

검색 결과 페이지가 브라우저에 출력되면, 파이썬에서 읽어와서 분석함
동적 웹 크롤링의 동작 :
브라우저 구동 => 사이트 접속 => 검색 필드 태그 찾음 => 검색 키워드 전송함
>> 브라우저 웹페이지에서 검색 적용 => 검색 실행 => 잠시 대기 => 브라우저에 검색 결과 출력
=> 파이썬에서 읽어옴 => 분석
'''
# import 방법
# import 모듈명 [as 줄임말] => 모듈이 가진 전체 내용이 임포트됨
# 모듈이 가진 일부 항목만 선택해서 임포트할 수 있음
# from 모듈명 import 선택항목명[, 선택항목, 선택항목, 하위모듈명, 함수명]
from selenium import webdriver as wd
from selenium.webdriver.chrome.service import service as cs, Service
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.by import By
# 명시적 대기를 위해 (waiting 을 명시함)
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
import time
from model.tour import TourInfo
from model.tour_model import TourModel

# selenium 와 연결할 브라우저 선택 : 크롬(chrome)
# 현재 설치 사용중인 크롬 브라우저의 버전 확인함
#   >> 브라우저 우측 상단 점3개 > 도움말 > Chrome 정보 > 버전정보 확인 : 124.0.6367.119 (최신 버전으로)
# 웹에서 '크롬 드라이버' 검색 > 확인된 버전과 같은 드라이버 zip 을 다운받음

import cx_Oracle
import common.dbConnectTemplate as dbtemp

# dbtemp.oracle_init()
# conn = dbtemp.connect()

def run():
    # 크롬드라이버 등록
    # Mac 용
    # driver = wd.Chrome('../chromedriver')
    driver = wd.Chrome(service=Service('./chromedriver.exe'))   # 크롬 브라우저 실행

    # 접속할 테스트 사이트 url 연결 확인 ---------------------------------------------
    # 키보드로 입력받아서 연결할 수도 있음
    # main_url = input('연결할 사이트 url 입력 : ')

    # 열린 브라우저로 사이트 접속
    driver.get('https://www.naver.com') # 실행확인
    # time.sleep(3) # 3초 대기
    # 해당 페이지의 검색 태그에 전달할 검색 키워드 정하기 : 입력을 통해서 정해도 됨
    keyword = '로마여행' # keyword = input('검색할 키워드 : ')
    
    # 검색 결과 저장할 리스트
    tour_list = []
    
    # 접속한 페이지의 검색입력필드 찾아서 검색 키워드 입력해서 실행되게 처리함
    # 검색 필드 태그(element)는 브라우저 '개발자도구' > 'Elements' 탭 에서 찾음
    # 찾은 앨리먼트 태그에서 마우스 우클릭 > copy > copy selector 선택함
    # #query
    input_tag = driver.find_element(By.ID, 'query')
    print(input_tag)
    input_tag.send_keys(keyword)
    # 해당 웹페이지 검색 input에 '로마여행' 자동 입력됨

    # 검색 버튼 클릭 작동
    # button 태그 선택자 복사해 옴 : #sform > fieldset > button
    # search-btn
    driver.find_element(By.CSS_SELECTOR, '#sform > fieldset > button').click()
    # driver.find_element(By.ID, 'search-btn').click()
    
    # 잠시 대기 => 검색 결과 페이지가 브라우저에 출력되고 나서 바로 데이터를 획득하는 행위는
    # 명시적으로 (코드상으로 표기) 대기시켜야 함
    # 획득할 데이터가 발견될 때까지 대기시킴
    # 대기 방법 : 명시적 대기와 암묵적 대기 2가지임
    
    # 명시적 대기 : 요구한 앨리먼트를 찾을 때까지 대기시킴
    # 로마 가볼만한 곳 : #nxTsOv > div > div.MainContainer._travel_header.MainContainer-vjtko > div.content-qIit7 > div.SummaryTopPoiContainer-qpzcR > div > div.head-xMGxp > div > h3
    try:
        element = wait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, \
            '#nxTsOv > div > div.MainContainer._travel_header.MainContainer-vjtko > div.content-qIit7 > div.SummaryTopPoiContainer-qpzcR > div > div.head-xMGxp > div > h3')))
    # 지정한 앨리먼트 위치를 확인하면 대기 종료됨
    except Exception as msg:
        print('대기 요청 타임아웃')

    # 암묵적 대기 :
    # DOM (Document Object Model : 태그 사용 계층 구조) 이 전부 다 브라우저에 로드될 때까지(모두 읽어 들일 때까지) 대기하게 하고
    # 먼저 로드되면 바로 태그 앨리먼트를 찾도록 진행함
    
    # 앨리먼트 찾을 시간(초) 지정하면, 지정 시간동안 DOM 풀링을 지시할 수 있음
    driver.implicitly_wait(10)
    
    # 절대적 대기 설정
    # time.sleep(10) # 10 초 대기
    # nxTsOv > div > div.MainContainer._travel_header.MainContainer-vjtko > div.PanelHeader-vpb6F > div.TabList-Erooo._scroll_wrapper > div.scroll-D9KKR._scroller > ul > li:nth-child(4) > a
    driver.find_element(By.CSS_SELECTOR, '#nxTsOv > div > div.MainContainer._travel_header.MainContainer-vjtko > div.PanelHeader-vpb6F > div.TabList-Erooo._scroll_wrapper > div.scroll-D9KKR._scroller > ul > li:nth-child(4) > a').click()
    time.sleep(3)

    # 해당 페이지 영역에서 데이터를 가져올 때, 혹시 로그인이 필요한 경우에는 로그인 세션 관리 필요함
    # 데이터가 많으면 세션 타임아웃에 의해 자동 로그아웃될 수 있으므로, 특정 단위별로 로그아웃하고,
    # 다시 로그인하는 처리가 필요함 => loop 문 돌려서 일괄적으로 접근 처리 필요함 : 메타 정보 획득
    
    # 가볼만한 곳 항목들 추출
    item_list = driver.find_elements(By.CLASS_NAME, 'TopPoiItem-MgXeO')
    print(len(item_list))

    # 가볼만한 곳 항목에서 데이터 추출하기
    # 추출할 값 : 순위(rank), 장소이름(name), 장소설명(description), 장소구분(category)

    tm = TourModel()
    for item in item_list:
        rank = item.find_element(By.CSS_SELECTOR, 'a > figure > span').text
        name = item.find_element(By.CSS_SELECTOR, 'a > div > span.subject-G1Fz6 > b.name-icVvV').text
        description = item.find_element(By.CSS_SELECTOR, 'a > div > span.desc-tw973').text
        category = item.find_element(By.CSS_SELECTOR, 'a > div > div > span').text

        # 튜플로 저장 처리
        tp_info = (rank, name, description, category)
        # db 에 저장 처리
        tm.insert_tour(tp_info)

    # for loop ------------------------------------------
    # db 에 저장된 정보 조회 출력 확인
    resultset = tm.select_all()
    # 리턴된 정보들을 한행씩 TourInfo 객체에 저장 처리 하고, 리스트에 추가
    tour_list = []
    for row in resultset:
        tourInfo = TourInfo(row[0], row[1], row[2], row[3])
        print(tourInfo)
        tour_list.append(tourInfo)
    print(tour_list)

    # 브라우저 종료
    driver.close() # 크롬 브라우저 닫기
    driver.quit()   # 드라이버 종료
    return  # 메인으로 리턴 : 프로세스 종료

# run -------------------------------
# 커밋 테스트
    











