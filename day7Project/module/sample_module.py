# path : module\\sample_module.py
# module : module.sample_module
# 파이썬에서 모듈 만들어서 사용하기

# 모듈(module) : 파이썬 소스 파일이다. (파일명.py)
# 파일명이 모듈명이 됨
# 모듈용 소스 파일에는 함수와 전역변수가 저장되면 됨
# 모듈이 제공하는 함수와 전역변수를 사용하려면, import 모듈명 으로 선언한 다음에
# 모듈명.함수명(), 모듈명.변수명으로 사용하면 됨

import keyword
# keyword.py 파일을 의미함
print(keyword.kwlist) # 예약어 리스트 출력됨

# 모듈은 다른 파이썬 파일에서 사용할 수 있도록 함수(기능)와 변수(값)들을 따로 저장해서
# 제공하는 목적의 소스 파일이다.

# 모듈 임포트시에 모듈명에 대한 줄임말을 같이 선언할 수도 있음
# import 모듈명 as 줄임말
import keyword as k

print(k.kwlist)
print(k.__file__)   # 해당 모듈(파일)의 위치가 출력됨
print('modules')    # 현재 설치되어 있는 모듈 확인

# 모듈 설명 참조
help('random')

# 파이썬이 제공하는 표준 모듈들 ------------------------------------------
import os   # 파일이나 디렉토리 관련 기능을 제공
print(os.getcwd())

import time     # 날짜와 시간 관련 기능 제공
print(time.localtime()) # 현재 날짜와 시간 정보 출력
time.sleep(1)   # 1초 멈춤
print(time.localtime())

import random   # 임의의 숫자를 발생시키는 기능을 제공
print(random.random)    # 0.0 <= random < 1.0
print(random.randint(1, 5)) # 1 <= random <= 5
print(random.randrange(1, 10, 2))   # 1 <= 2 간격의 정수 < 10

import math # 수학 계산 관련 기능 제공

print('원자율 : ', math.pi)
print('5! : ', math.factorial(5))

import calendar # 달력을 출력해서 날짜 지정 기능 제공
calendar.prmonth(2024, 5)

# __name__ : 현재 실행되고 있는 모듈이름 확인
print(__name__) # main 파일명 출력됨
# 프로그램을 실행하면 기본 파일은 main 모듈(파일)이 됨, 즉 main 만 실핼할 수 있다는 의미임

import mymodule as md
print('더하기 : ', md.sum(10, 20))
print('빼기 : ', md.sub(15, 27))
print('곱하기 : ', md.mul(1, 4))
print('나누기한 몫 : ', md.div(2, 4))
try:
    print('나누기한 나머지 : ', md.mod(5, 0))
except Exception as msg:
    print(msg)
    pass

print('가장 큰 값 : ', md.max())
print('가장 큰 값 : ', md.max(10))
print('가장 큰 값 : ', md.max(1, 2, 3, 4, 5, 6, 7, 8, 9))

print('가장 작은 값 : ', md.min())
print('가장 작은 값 : ', md.min(10))
print('가장 작은 값 : ', md.min(1, 2, 3, 4, 5, 6, 7, 8, 9))

print('글자 갯수 : ', md.strlen())
print('글자 갯수 : ', md.strlen('module test'))

print('원주율 : ', md.pi)
print('카운트 : ', md.count)

