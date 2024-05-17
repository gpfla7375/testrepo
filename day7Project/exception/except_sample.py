# path : exception\\exception_sample.py
# module : exception.exception_sample
# 파이썬에서의 예외처리 (Exception Handling)
'''
예외 : 소스 코드로 해결할 수 있는 에러
에러의 종류 :
    - 시스템 에러 : 소스 코드로 해결 못 하는 에러
                    메모리 부족, 하드디스크(저장장치) 용량 부족, 배터리 전원 부족 등
    - 구문(문법) 에러 : 잘못 작성된 경우의 에러임
                        개발툴 IDE 에서 자동 검사함. 구문 수정해서 해결함
    - 런타임 에러 : 실행시 발생하는 에러
                    에러 발생이 되면 코드를 수정해서 해결함 => 예외처리함

에러 처리 방법 :
    if 조건문으로 에러 상황을 예측해서 미리 조치함
    => 예외상황을 처리하는 별도의 구문이 있음 - 예외 처리 구문 사용을 권장함

'''

def test_error():
    '에러 발생 예 테스트 함수'
    # print('test_error' # SyntaxError: '(' was never closed => 구문 오류
    # a = 10
    # b = 0 # ZeroDivisionError: division by zero => 실행시 확인되는 에러 (Runtime error)
    # c = a / b

    # 4 + new * 3 # NameError: name 'new' is not defined
    lst = [1, 2]
    # print(lst[2]) # IndexError: list index out of range => Runtime error

    dct ={'a':100, 'b':200}
    # print(dct['c']) # KeyError: 'c' = Runtime error

# 런타임 에러 중에 사용자가 입력값을 잘못 입력하는 경우
def test_input_error():
    '입력 오류 관련 에러 테스트 함수'
    # num = int(input('정수를 입력하세요 : ')) # ValueError: invalid literal for int() with base 10:
    # if 문으로 처리할 수 없는 에러 발생 상황인 경우 => 예외 처리 구문으로 해결

    # 해결 방법 1 : 입력시 조건문 적용
    num = input('정수를 입력하세요 : ')
    if(num.isdecimal()): # 정수 10진수냐
        num = int (num)
        print(num, type(num))
    else:
        print('정수만 입력해야 합니다. 다시 입력하세요.')

# 예외처리 방법 : 예외처리 구문으로 작성
# try: 에러발생 가능성이 있는 구문 except: 해결구문 (try catch 문과 같음)
'''
try:
    에러 발생 가능성이 있는 구문 또는 일반 구문
except:
    에러가 발생했을 때 실행할 구문(들) 
'''
def test_input_error2():
    num = input('정수를 입력하세요 : ')
    try:
        num = int(num)  # 에러 발생 가능성이 있는 문장
        print(num, type(num))
    except:
        print('정수만 입력해야 합니다. 다시 입력하세요.')

# 예외처리시 except: 에 pass를 사용하면
# 오류 발생시 프로그램이 멈추지 않고 계속 동작되게 할 수 있음
def except_pass():
    lst = ['3', '예외처리', 4, 2, 67.5, 'python']
    digit_num = []
    print(lst)

    # lst 에서 숫자만 골라내서 digit_num 에 기록 저장 처리
    for idx in range(len(lst)):
        try:
            digit_num.append(int(lst[idx]))
        except:
            pass
    print(digit_num)


def except_pass2():
    lst = ['3', '예외처리', 4, 2, 67.5, 23, 'python']
    digit_num = []
    print(lst)

    # lst 에서 숫자만 골라내서 digit_num 에 기록 저장 처리
    for item in lst:
        # if 조건문 처리와 비교
        print(item, type(item))
        try:
            if str(item).isdigit(): # is...() 함수는 문자형 값에 사용하는 함수임
                digit_num.append(int(item))
        except:
            pass
    print(digit_num)

# finally : 예외 발생과 상관없이 반드시 실행할 구문을 작성하는 영역임
import math # 수학 관련 함수들을 제공하는 모듈임

def test_finally():
    'finally 구문 사용 테스트 함수'
    try:    # 예외 발생 가능성이 있는 구문 작성 영역
        radius = float(input('반지름 : '))
    except: # 에러가 발생했을 때 처리할 구문 작성 영역
        print('숫자만 입력해야 합니다.')
    else:   # 에러가 발생하지 않았을 때 처리 구문 작성 영역
        print('반지름 : ', radius)
        print('원 면적 : ', math.pi * math.pow(radius, 2))
        print('원 둘레 : ', 2 * math.pi * radius)
    finally:    # 반드시 실행해야 되는 구문 작성 영역
        print('예외처리 구문 종료함')
    # try 구동 --> 에러 발생 --> except --> finally
    # try 구동 --> 정상 처리 --> else --> finally

    # 파이썬에서의 예외처리 구문 조합 형태
    # try: ~ except: ~
    # try: ~ except: ~ else:
    # try: ~ except: ~ finally: ~
    # try: ~ except: ~ else: ~ finally: ~
    # try: ~ finally: ~
    # 잘못 사용된 경우 : try: ~ else: ~

    # def test_except():
    #     'try: ~ else: ~ 잘못 사용된 경우의 테스트 함수'
    #     try:
    #         print('try area....')
    #     else:
    #         print('else area....')

# ---------------------------------------------------------------------------------
# try 쪽에서 여러 종류의 에러가 발생할 경우
# except: 구문을 여러 개 작성할 수 있다. (사용 갯수에 제한 없음)
# except 에러종류이름: 또는 except 에러클래스명 as 변수명:
# 에러클래스의 계층구조에 따라 하위 클래스를 먼저 작성할 것 (자바의 상속구조 처리와 같음)
def multi_except():
    '다중 except 사용 테스트 함수'
    try:
        # print(3 / 0)
        lst = []
        # print(lst[0])
        # print(int('안됨'))
        lst.append(int(input('숫자 입력 : ')))
        print(lst)
        print('2' + 4)
    except TypeError:
        print('이거맞나')
    except ZeroDivisionError:
        print('0으로 나눌 수 없습니다.')
    except IndexError:
        print('리스트 인덱스 잘못 사용됨')
    # except Exception as msg:
    #     print('에러가 발생함')
    #     print(msg)

# 예외를 강제로 발생시키기 ------------------------------------------
# raise 예외클래스명 또는 raise 예외클래스명('에러메세지')
# 주로 함수나 메소드 작성시에 이용함
# 코드상 지정하는 조건일 때 에러 발생시키고, 해당 함수를 사용해서 예외 처리함

def ndiv(a, b):
    if b == 0:
        raise Exception('0 나누기 못함')
    else:
        return a / b
    
# 함수 사용시 예외처리 작성함
def test_ndiv():
    '예외 발생 구문이 있는 함수 사용 테스트용'
    try:
        # 예외 발생 구문을 가진 함수 사용
        result = ndiv(12, 3)
        result = ndiv(12, 0)
        print(result)
    except Exception as msg:
        print(msg)

# 실행 테스트
if __name__ == '__main__':
    # test_error()
    # test_input_error()
    # test_input_error2()
    # # except_pass()
    # except_pass2()
    # test_finally()
    # test_except()
    # multi_except()
    test_ndiv()