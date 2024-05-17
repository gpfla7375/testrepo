# path : model\\tour_model.py
# module : model.tour_model
# 오라클 db에 TourInfo 객체 정보를 CRUD 처리하는 클래스 정의 스크립트
import cx_Oracle
import common.dbConnectTemplate as dbtemp

class TourModel:
    # field
    __conn = ''

    # constructor
    def __init__(self):
        dbtemp.oracle_init()   # 드라이버 등록 : 딱 한번 실행
    
    # destructor
    def __del__(self):
        try:
            if self.__conn != '': # 연결상태라면
                dbtemp.close(self.__conn)   # db 연결 해제
        except Exception as msg:
            print('소멸자 오류 : ', msg)

    # method
    # insert method
    def insert_tour(self, tp_tour):
        query = 'insert into tour values (:1, :2, :3, :4)'
        self.__conn = dbtemp.connect()
        try:
            # 자동 close 되게 처리 : with resource 문 이용
            with self.__conn.cursor() as cur:
                cur.execute(query, tp_tour)
            dbtemp.commit(self.__conn)
        except Exception as msg:
            dbtemp.rollback(self.__conn)
            print('insert_tour 실패 : ', msg)
        finally:
            dbtemp.close(self.__conn)

    # delete all method
    def delete_all(self):
        query = 'delete from tour'
        self.__conn = dbtemp.connect()
        try:
            # 자동 close 되게 처리 : with resource 문 이용
            with self.__conn.cursor() as cur:
                cur.execute(query)
            dbtemp.commit(self.__conn)
        except Exception as msg:
            dbtemp.rollback(self.__conn)
            print('delete_all 실패 : ', msg)
        finally:
            dbtemp.close(self.__conn)

    # select all method
    def select_all(self):
        query = 'select * from tour'
        self.__conn = dbtemp.connect()
        try:
            # 자동 close 되게 처리 : with resource 문 이용
            with self.__conn.cursor() as cur:
                cur.execute(query)
                return cur.fetchall()
        except Exception as msg:
            print('select_all 실패 : ', msg)
        finally:
            dbtemp.close(self.__conn)

    def select_one(self, tp_tour):
        query = 'select * from tour where rank = :1'
        self.__conn = dbtemp.connect()
        try:
            # 자동 close 되게 처리 : with resource 문 이용
            with self.__conn.cursor() as cur:
                cur.execute(query, tp_tour)
                return cur.fetchone()
        except Exception as msg:
            print('select_one 실패 : ', msg)
        finally:
            dbtemp.close(self.__conn)

# TourModel ---------------------------------------------------
