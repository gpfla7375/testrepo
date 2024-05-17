#list_mission.py
"""
키보드로 값들을 입력받아, 요구대로 처리하고 확인 출력 코드를 작성하시오.

입력 내용 :
    학생이름 : 홍길동 (name : str)
    학년 : 2 (grade : int)
    반 : 3 (s_class : int)
    번호 : 12 (s_no : int)
    점수 : 87.5 (score : float)

처리 내용 :
    입력받은 값들을 리스트(student_list)에 순서대로 저장 처리함

출력 내용 :
    리스트에 저장된 값들을 출력함
    2학년 3반 12번 홍길동의 점수는 87.50 입니다.
    -> 점수는 소수점아래 둘째자리까지 표시
    -> format() 사용함
"""
# name = input('학생이름 : ')
# grade = int(input('grade : '))
# s_class = int(input('s_class : '))
# s_no = int(input('s_no : '))
# score = float(input('score : '))
#
# student_list = [name, grade, s_class, s_no, score]
# print('{}학년 {}반 {}번 {}의 점수는 {:.2f} 입니다.'.format(student_list[1], student_list[2], student_list[3], student_list[0], student_list[4]))
#
# # 방법 2 : 입력받은 값들을 리스트에 append()
# name = input('학생이름 : ')
# grade = int(input('grade : '))
# s_class = int(input('s_class : '))
# s_no = int(input('s_no : '))
# score = float(input('score : '))
#
# student_list = []
# student_list.append(name)
# student_list.append(grade)
# student_list.append(s_class)
# student_list.append(s_no)
# student_list.append(score)
# print('{}학년 {}반 {}번 {}의 점수는 {:.2f} 입니다.'.format(student_list[1], student_list[2], student_list[3], student_list[0], student_list[4]))

# 방법 3: 방법 2 코드 줄 수 줄이기
student_list = []
student_list.append(input('학생이름 : '))
student_list.append(int(input('grade : ')))
student_list.append(int(input('s_class : ')))
student_list.append(int(input('s_no : ')))
student_list.append(float(input('score : ')))
print('{}학년 {}반 {}번 {}의 점수는 {:.2f} 입니다.'.format(student_list[1], student_list[2], student_list[3], student_list[0], student_list[4]))

# student_list = [input('학생이름 : '), int(input('grade : ')), int(input('s_class : ')), int(input('s_no : ')), float(input('score : '))]


"""    키보드로 값들을 입력받아, 요구대로 처리하고 확인 출력 코드를 작성하시오.
입력 내용 :
    국어 점수 : 78.5 (kor : float)
    영어 점수 : 88.7 (eng: float)
    수학 점수 : 93.5 (mat : float)
처리 내용 :
    3명의 학생 점수를 입력 받음, 각 학생의 총점과 평균은 각각 계산함
    학생별 점수는 각 리스트에 저장한 다음, [국어, 영어, 수학, 총점, 평균]
    각 학생 점수를 리스트(sungjuk_list)에 순서대로 저장 처리함
    [[국, 영, 수, 총, 평], [국, 영, 수, 총, 평], [국, 영, 수, 총, 평]]
    3명의 점수의 총합(total_score : int)과 전체평균(average_score : float)를
    계산하시오.
출력 내용 :
    리스트에 저장된 값들을 출력함,   국, 영, 수, 총, 평균 순서로 출력
     -> 점수는 소수점아래 둘째자리까지 표시
    -> format() 사용함
    전체 총점과 전체 평균을 출력하시오.
"""
sungjuk_list= []
total_score = 0
average_score = 0

for i in range(3):
    kor = float(input('국어 점수 : '))
    eng = float(input('영어 점수 : '))
    math = float(input('수학 점수 : '))

    sungjuk_list.append([kor, eng, math, int(kor + eng + math), float((kor + eng + math) / 3)])

    total_score += kor + eng + math
    average_score += total_score



for k in range(3):
    print('국어 : {:1.f}, 수학 : {:1.f}, 영어 : {:1.f}, 총점 : {}, 평균 : {:.2f}'.format(sungjuk_list[k][0], sungjuk_list[k][1], sungjuk_list[k][2], sungjuk_list[k][3], sungjuk_list[k][4]))
print('총합 : {}, 평균 : {:.2f}'.format(total_score, average_score / 3))


