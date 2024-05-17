# path : loop\\loopMission.py
# module : loop.loopMission

# 리스트 안의 튜플아이템의 값들에 대해
# 둘 중의 큰값과 작은값을 분류해서 출력 처리

# 방법 1 : 조건식 직접 작성
def practice1():
    nlist = [(12, 56), (53, 23), (1, 34)]
    # for 문 안에서 if 문 사용
    for f, s in nlist:
        if f > s:
            max = f
            min = s
        else:
            max = s
            min = f
        print(f'큰값 {max} 작은값 {min}')

# 방법 2 : 내장함수 이용
def practice2():
    nlist = [(12, 56), (53, 23), (1, 34)]
    for f, s in nlist:
        vmax = max(f, s)
        vmin = min(f, s)
        print(f'큰값 {vmax} 작은값 {vmin}')




# 활용 실습 : 조건식 직접 작성
# 리스트 안의 군집아이템들이 가진 값들 중 각각 가장 큰 값을 골라 내서
# 별도의 리스트에 저장 처리하고 출력
def practice3():
    list = [[123, 24, 35, 63], [234, 35, 64, 1], [23, 4, 5, 6]]
    mlist = []
    for i in list:
        vmax = 0
        for k in i:
            if vmax < k:
                vmax = k
        mlist.append(vmax)
    print(mlist)

# 내장함수 max(Iterable) 사용
def practice4():
    list = [max([123, 24, 35, 63]), max([234, 35, 64, 1]), max([23, 4, 5, 6])]
    print(list)

''' while 문 실습문제
아래의 작성된 for문을 while문으로 변경하시오.
sungjuk_list = [[12, '홍길동', 98], [15, '김유신', 87], [23, '황지니', 45]]

for student in sungjuk_list:
    if(student[2] >= 60):
        print('{}번 {} 학생은 합격입니다.'.format(student[0], student[1]))
    else:
        print('{}번 {} 학생은 불합격입니다.'.format(student[0], student[1]))
'''
# 1. while 문으로 변경
def practice_while():
    sungjuk_list = [[12, '홍길동', 98], [15, '김유신', 87], [23, '황지니', 45]]
    index = 0
    while index < len(sungjuk_list):
        student = sungjuk_list[index]
        if (student[2] >= 60):
            print('{}번 {} 학생은 합격입니다.'.format(student[0], student[1]))
        else:
            print('{}번 {} 학생은 불합격입니다.'.format(student[0], student[1]))
        index += 1

# 2. for 문 안에 continue 를 사용해서 합격자 정보만 출력되게 처리
def practice_continue():
    sungjuk_list = [[12, '홍길동', 98], [15, '김유신', 87], [23, '황지니', 45]]
    for student in sungjuk_list:
        if (student[2] >= 60):
            print('{}번 {} 학생은 합격입니다.'.format(student[0], student[1]))
        else:
            continue


# 3. print() 안에 간단 if 문 사용해서 출력 처리
def practice_short_if():
    sungjuk_list = [[12, '홍길동', 98], [15, '김유신', 87], [23, '황지니', 45]]
    for student in sungjuk_list:
        print('{}번 {} 학생은 합격입니다.'.format(student[0], student[1]) if student[2] >= 60 else '{}번 {} 학생은 불합격입니다.'.format(student[0], student[1]))


if __name__ == '__main__':
    # practice1()
    # practice2()
    # practice3()
    # practice4()
    # practice_while()
    # practice_continue()
    practice_short_if()
