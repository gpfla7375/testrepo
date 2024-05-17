# path : testdb\\test_mysql.py

# 파이썬 외부 모듈(패키지) 설치와 사용
# 파이썬 외부 모듈은 프로젝트에 직접 설치해서 사용하는 방법이 있고 (venv)
# 아나콘다에 별도의 콘다환경을 준비해서 필요한 패키지를 따라 설치한 다음에 프로젝트에 가져다 사용하는 방법 (conda)이 있다.

# 프로젝트에 직접 설치하는 방법
# 방법 1 :
# 파이참 툴 왼쪽 아래의 'Python Packages' 탭을 클릭 > 뷰가 아래쪽에 보여짐
# 뷰의 왼쪽에 검색 영역에 설치할 패키지명을 입력
# 검색되면 패키지명을 클릭하면, 오른쪽에 패키지 정보가 표시됨
# 오른쪽 패키지 정보 위에 'Install package' 버튼 클릭함 > 설치가 완료되면, 버전 숫자 표시됨

# 만약, 설치가 실패하면 오류 메세지에서 에러 이유를 찾아내서 해결해야 됨
# 방법 2 :
# 모든 파이썬 개발툴에서 공통으로 사용하는 방법임
# 'Terminal' (터미널) 탭 (왼쪽 아래) 클릭
# (가상환경종류) 터미널종류 현재프로젝트경로> 프롬프트 표시됨
# 프롬프트에 설치 명령어를 직접 입력해서 설치함
# > pip install 설치할 패키지명
# 주의사항 : pip 버전을 먼저 upgrade 해야되는 경우가 있음
# > python -m pip install --upgrade pip
# > pip --version
# 패키지 설치와 pip 업그레이드 동시에 수행할 수도 있음
# > python -m pip install --upgrade 설치할패키지명

# 방법 3 :
# File 메뉴 > Settings.. > 왼쪽 항목에 Project:프로젝트명 표시찾음
# > 프로젝트명 부분을 확장시킴
# 오른쪽 아래에 'python interpreter' (파이썬 인터프리터) 선택
# => 현재 프로젝트에 설치된 패키지 모듈을 볼 수 있음
# > 위쪽의 '+' 클릭 > 새 창 열림
# 설치할 패키지 검색 > 검색한 패키지 이름 선택 > 아래쪽의 '설치' 버튼 클릭
# 설치 성공 메세지 확인하고 창 닫음

# 데이터베이스 연결에 필요한 파이썬 패키지 ---------------------------------------------------
# mysql db : pymysql 패키지 필요
# oracle db : cx-Oracle 패키지 필요 > 설치오류시 https://m.blog.naver.com/loonee14/223306460176 참조

# 1. 설치 후에 import 선언하고 사용함
import pymysql

# 2. 해당 데이터베이스에 연결하기 위한 코드 작성
# db 서버의 ip 주소(url), 포트번호, 사용자계정과 암호
dbURL = 'localhost' # dbURL = '192.168.120.34'
dbPORT = 3306
dbUSER = 'root'
dbPWD = '1234'
# 3. 데이터베이스 연결
# 임포트한 모듈에서 제공하는 메소드를 사용함 : pymysql.connect()
conn = pymysql.connect(host=dbURL, port=dbPORT, user=dbUSER, passwd=dbPWD, db='testweb', \
                       charset='utf-8', use_unicode=True)

# 연결이 실패하면 conn = null(None) 임
# 연결이 성공하면의 조건식 => if conn != null;

# 4. db 연결이 성공했다면, 필요한 쿼리문(C: insert, R: select, U: update, D: delete)
# 예 : select 쿼리문 작성해서 실행 처리
query = 'select * from sample'

cursor = conn.cursor()  # 자바의 Statement | PreparedStatement
cursor.execute(query)   # 쿼리문 보내서 실행
result = cursor.fetchall()  # 조회된 모든 결과를 받음, 반환 자료형은 tuple 임
# 이후 결과 매핑 처리 : 반복문으로 행의 컬럼값들을 vo (dto) 객체의 필드 (property) 에 저장 처리

# 5. 쿼리문이 dml 이면 트랜잭션 처리가 필수임
if result > 0:
    conn.commit()
else:
    conn.rollback()

# 6. db 사용이 끝나면 반드시 닫음
conn.close()

