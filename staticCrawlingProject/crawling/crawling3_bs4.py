# path : crawling\crawling3_bs4.py
# 네이버 개봉 영화 정보 페이지 크롤링 분석 테스트

import urllib.request, bs4

web_page = urllib.request.urlopen("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%84%A4%EC%9D%B4%EB%B2%84+%EC%98%81%ED%99%94")
result_code = bs4.BeautifulSoup(web_page, 'html.parser')

# 개봉영화 정보가 기록된 태그 앨리먼트 찾기
# 찾아진 태그 앨리먼트 안의 값을 추출 : find() 함수 사용 => 찾은 첫번째 앨리먼트만 리턴함
# find(찾을 텍스트가 기록된 태그명, 태그속성_= '속성값')
# find(태그속성_='속성값')

data_box = result_code.findAll('div', attrs={'class':'data_box'})
# movie_title = data_box.find("a", attrs={'class': 'this_text'})
# 영화 제목만 추출하기
# print("하나만 추출 => ", movie_title.get_text())

# 영화 타이틀 뽑기
# list2 = result_code.findAll('a', attrs={'class':'this_text'})
# print(len(list))
# for l in list2:
#     print(l.get_text())
movie_list = list()     # 항목 데이터 추가
movie = result_code.find_all("div", {"class": "data_box"})


# 영화제목, 개봉일, 장르, 별점, 링크

for idx in range(len(movie)):
    each_movie = dict()
    each_movie["title"] = movie[idx].find("a", {"class": "this_text _text"}).text
    each_movie["release_date"] = movie[idx].find("dl", {"class": "info_group type_visible"}).find("dd").text
    each_movie["genre"] = movie[idx].find("dl", {"class": "info_group"}).find("dd").text
    each_movie["star_point"] = movie[idx].find("span", {"class": "num"}).text
    each_movie["link"] = "https://search.naver.com/search.naver" + movie[idx].find("a", {"class": "this_text"}).attrs[
        'href']
    movie_list.append(each_movie)

print(movie_list)

# for l in list:
#     print(l.get_text())

sort_list = sorted(movie_list, key=lambda x : x['star_point'], reverse=True)

# 정렬 후 등수 추가 확인
for idx in range(len(sort_list)):
    sort_list[idx]['rank'] = idx + 1
    print(sort_list[idx])

# 오라클 db Movie 테이블에 기록 처리
import cx_Oracle
import common.dbConnectTemplate as dbtemp

# 오라클 드라이버 설정
dbtemp.oracle_init()
conn = dbtemp.connect()

# 크롤링한 결과 db 에 기록 처리 : insert 문 사용
query = "insert into MOViE values (:1, :2, :3, :4, :5, :6)"

# 리스트에 저장된 딕셔너리를 튜플로 변환해서 쿼리문에 적용해서 실행 처리함
for movie in movie_list:
    tp_value = (movie['rank'], movie['title'], movie['star_point'], movie['release_date'], movie['genre'], movie['link'])
    cursor = conn.cursor()
    try:
        cursor.execute(query, tp_value)
        dbtemp.commit(conn)
    except:
        dbtemp.rollback(conn)
    finally:
        cursor.close()