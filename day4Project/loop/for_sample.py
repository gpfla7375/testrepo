# loop/for_sample.py
# loop.for_sample
# 파이썬에서의 for 문 사용 테스트 스크립트
'''
for 문 작성형식 1 :
for 변수 in 리스트 | 튜플 | 딕셔너리 | 집합 | 문자열:
    반복실행할 구문들 작성 (들여쓰기)
주의사항 : in 오른쪽에 값하나(리터럴) 사용 못 함
for 변수 in 값: => TypeError 발생함
'''

def test_for1():
    for i in [10, 20, 30]:  # list 사용
        print(f'{i}는 5의 배수이다')

        # for k in 10:
        #     print(k)
    for t in (11, 22, 33):    # tuple 사용
        print(f'{t} 는 짝수이다.' if t % 2 == 0 else f'{t} 는 홀수다.')

    for s in {1, 2, 3, 4, 5, 6}:    # set 사용
        print(f'{s} 의 제곱은 {s**2}이다')
        
    for st in 'Python': # str 사용
        print(f'{st}문자의 유니코드는 {ord(st)}이다')


'''
for 문 작성형식 2 : range
range(시작값, 끝값) 또는 range(시작값, 끝값, 간격) 또는 range(끝값)
시작값 >= 0 | n, m > 끝값 간격은 생략시 기본 1임, 반드시 정수만 사용함
for 변수 in range(start, end): (콜론 주의)
    변수를 사용한 반복실행 구문 작성 (들여쓰기)
'''

# 1부터 100까지 정수들의 합계를 구해서 출력
def for_sum():
    sum = 0
    for n in range(1, 101):
        print(n, '+', end='')
        sum += n
    print()
    print(f'합계 : {sum}')

# --------------------------------------------------------------------------------------------
# import collections.iterable => deprecated : 버전 업하면서 사용이 중지됨
import collections.abc

def test_iterable():
    nlist = [1, 2, 3, 4]
    # iterable object: 리스트처럼 순차적으로 값을 가진 객체를 말함
    # isinstance() 함수 : 객체의 종류를 확인할 때 사용함 (자바의 instanceOf 연산자와 같음)
    print(isinstance(nlist, collections.abc.Iterable))  # Iterable 의 첫글자는 대문자임

def test_range():
    print(range(10)) # range(0, 10)

    lst = list(range(10))
    print(lst)

# for 문 작성형식 3 : range(len(리스트변수)) - 연속된 값을 인덱스로 처리
def for_indexing():
    # 리스트에 저장된 아이템 추출
    list1 = ['apple', 90, [1, 2, 3], ('A', 'B', 'C')]
    for item in list1:
        print(item)

    for idx in range(len(list1)):   # range(4) => range(0,4) => 0, 1, 2, 3
        print(list1[idx])

# 키보드로 구구단의 단수를 입력받아서, 해당 단의 구구단 출력

def print_gugudan():
    dan = int(input('숫자 입력 : '))
    for k in range(1, 10):
        # print(dan, ' * ', k, ' = ', dan * k)
        print(f'{dan} * {k} = {dan * k}')

# for 문 안에 for 문 사용
# 구구단 2단부터 9단까지 출력 처리
def doubleFor():
    for i in range(1, 10):
        for k in range(1, 10):
            print(f'{i} * {k} = {i * k}')
        print('-----------------------------------')

# 리스트 | 튜플 | 셋 안의 리스트 | 튜플 | 셋이 저장된 경우
# 첫번째 추출을 리스트(튜플, 셋) 안의 아이템(리스트, 튜플, 셋) 추출임
# 꺼낸 아이템이 리스트(튜플)일 경우, 해당 아이템 안의 값들을 하나씩 추출하려면
# 이중 for 문 사용이 필요함

# 리스트 안의 아이템 안에 값의 갯수가 동일할 경우에는 단순 for 문으로 해결 가능함
def list_in_list():
    fruit_list = [['apple', 10, 800], ['banana', 3, 250], ['orange', 15, 500]]

    for fname, famount, fprice in fruit_list:
        print(f'{fname} 의 단가는 {fprice} 원이고, 구매 수량은 {famount} 개, 구매가격은 {famount * fprice} 입니다.')

# 리스트 안의 아이템의 값 갯수나 기록형태가 제각각인 경우
# 아이템 안의 각 값들을 처리하려면 이중 for 문 사용
def list_in_list2():
    nlist = [['a', 'bb', 'cde'], [10, 20], [1.2, 3.4, 33, 89.09]]
    for i in nlist:
        print(i)
        for k in i:
            print(k)
        print('-----------------------')

# 위의 리스트를 인덱스로 처리한다면
def list_in_list3():
    nlist = [['a', 'bb', 'cde'], [10, 20], [1.2, 3.4, 33, 89.09]]
    for i in range(len(nlist)):
        print(nlist[i])
        for k in range(len(nlist[i])):
            print(nlist[i][k])
        print('-----------------------')
