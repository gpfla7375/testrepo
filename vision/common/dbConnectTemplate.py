# path : common\\dbConnectTemplate.py
# module : common.dbConnectTemplate
# 데이터베이스 연결 관리용 공통 모듈 정의 (변수와 함수만 정의)
# 1. 사용할 패키지(모듈) 임포트
import cx_Oracle
import os

# 오라클 연결을 위한 값들을 전역변수로 지정
url = 'localhost:1521/xe'
user = 'c##testweb'
passwd = 'testweb'

def oracle_init():  # 애플리케이션에서 딱 한번만 구동시킴
    cx_Oracle.init_oracle_client(lib_dir='D:\\instantclient_18_5')
    # Mac 에서는 필요없음



def connect():
    try:
        conn = cx_Oracle.connect(user, passwd, url)
        # Mac 에서는 아래 구문을 사용해야 함
        # conn = cx_Oracle.connect('c##testweb/testweb@localhost:1521/xe')
        conn.autocommit = False
        return conn
    except Exception as msg:
        print('오라클 연결 에러 : ', msg)

def close(conn):
    try:
        if conn:    # conn != null 가 같음 (True 이면)
            conn.close()
    except Exception as msg:
        print('오라클 닫기 실패 : ', msg)

def commit(conn):
    try:
        if conn:    # conn != null 가 같음 (True 이면)
            conn.commit()
    except Exception as msg:
        print('오라클 트랜잭션 커밋 실패 : ', msg)
        
        
def rollback(conn):
    try:
        if conn:    # conn != null 가 같음 (True 이면)
            conn.rollback()
    except Exception as msg:
        print('오라클 트랜잭션 롤백 실패 : ', msg)


# 4. 쿼리문 준비하기
# query = 'select * from c##testweb.member'
#
# # 5. 쿼리문 실행시키기 위한 객체 준비하고, 쿼리문 실행 처리
# # cursor : 준비된 쿼리문을 연결된 db로 전송해서 실행시키는 객체임
# cursor = conn.cursor()  # db 연결정보로 커서 객체를 생성함
# cursor.execute(query)   # 쿼리문을 db로 전송하고 실행한 결과를 받음
# 커서가 실행된 쿼리문의 결과를 받음
# select 쿼리문을 실행시켰다면, 결과집합(ResultSet)을 커서가 받음
# dml 문(insert, update, delete) 은 처리된 행갯수를 커서가 받음
# print('cursor : ', cursor)