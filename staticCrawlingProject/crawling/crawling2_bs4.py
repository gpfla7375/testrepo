# path : crawling\crawling2_bs4.py
# module : crawling.crawling2_bs4
# url 을 키보드로 입력받아서 크롤링 테스트
import bs4, urllib.request


# url 은 웹상의 자원까지의 경로를 의미함
# 프로토콜://도메인명/폴더명/파일명?이름=값&이름=값
# 쿼리스트링 : 서버측의 대상 파일로 전달되는 값들을 표현한 것
#               ?이름=값&이름=값

result_code = bs4.BeautifulSoup(urllib.request.urlopen(input('접속할 url 오픈 : ')), 'html.parser')
print(result_code)
# https://search.naver.com/search.naver?where=news&ie=utf8&sm=nws_hty&query=%EC%98%81%ED%99%94
# https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&ssc=tab.nx.all&query=%EB%84%A4%EC%9D%B4%EB%B2%84%EC%98%81%ED%99%94&oquery=%EC%8A%88%EA%B0%80%E2%94%82%EC%96%B4%EA%B1%B0%EC%8A%A4%ED%8A%B8+%EB%94%94+%ED%88%AC%EC%96%B4+%E2%80%98%EB%94%94-%EB%8D%B0%EC%9D%B4%E2%80%99+%EB%8D%94+%EB%AC%B4%EB%B9%84&tqi=iBeQXdqVOZossckFN68sssssszN-287698