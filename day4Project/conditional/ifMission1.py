# conditional\\ifMission1.py
# conditional.ifMission1
# if 문 실습문제
'''
키보드로 정수 2개를 입력받아서, 두 정수가 모두 양수일때만
합, 차, 곱, 몫(int), 나머지 를 계산해서 출력하시오.
입력 내용 :
 첫번째 정수 : 12 (num1 : int)
 두번째 정수 : 5 (num2 : int)
처리 내용 :
 조건 : 두 수 모두 양수이냐? (양수의 조건 : 값 > 0)
 양수가 맞을때만 사칙연산 계산해서 출력함
 둘 다 또는 하나만 0, 음수이면 처리할 내용이 없음
'''
def practice1():
    num1 = int(input('정수 입력 : '))
    num2 = int(input('정수 입력 : '))
    if num1 > 0 and num2 > 0:
        print('합 : ', int(num1 + num2))
        print('차 : ', int(num1 - num2))
        print('곱 : ', int(num1 * num2))
        print('몫 : ', int(num1 / num2))
    else:
        print('처리할 내용이 없음')





