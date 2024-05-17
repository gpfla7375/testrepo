# path : loop\\whileSample.py
# module : loop.whileSample
# while 문 사용 테스트 스크립트

'''
while 반복에 대한 조건식: (콜론 주의)
    반복 실행 구문 (들여쓰기 주의)
반복에 대한 조건식은 무한 루프가 되지 않게 작성할 것
만약, True 를 사용했다면, 반드시 while 안에 종료에 대한 조건처리 구문이 있어야 함
if 종료조건:
    break
'''

def test_while():
    num = 5
    while num > 0:
        print(num)
        num -= 1

# 반복 횟수가 정해지지 않은 경우 while 문 주로 사용함
# 문자 하나 입력받아서, 그문자의 유니코드를 출력하는 처리를 반복 실행
# 단 '0' 이 입력되면 반복이 종료됨

def print_unicode():
    ch = input('문자 하나 입력 [0이 입력되면 종료됨]: ')
    while ord(ch) != 48:
        print(f'{ch} is unicode {ord(ch)}')
        ch = input('문자 하나 입력 [0이 입력되면 종료됨]: ')


def print_unicode2():
    while True:
        ch = input('문자 하나 입력 [0이 입력되면 종료됨]: ')
        if ch == '0':
            break
        print(f'{ch} is unicode {ord(ch)}')

# 파이썬에서는 여러 줄의 문자열 값을 표현할 때 3쌍의 따옴표를 이용할 수 있음
def display_menu():
    prompt = '''
        *** 원하는 메뉴 번호를 선택하세요. ***
        1. 추가
        2. 삭제
        3. 출력
        4. 끝내기
    '''
    # print(prompt)
    while True:
        print(prompt)
        no = int(input('번호 입력 : '))
        if no == 4:
            break
        print('---------- END -------------')


# 이 파이썬 스크립트 파일을 실행파일로 만들고자 한다면, 아래쪽에 main  코드 추가하면 됨
if __name__ == '__main__':
    display_menu()
