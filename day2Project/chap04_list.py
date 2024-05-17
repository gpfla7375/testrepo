# chap04_list.py
# 리스트(list) 자료형
# 파이썬이 제공하는 군집자료형임
# 자바의 List 와 같은 자료형임

# 개념 : 여러 종류의 값들을 순차적으로 저장하는 자료형임
# 저장 용량에 제한은 없다.
# 저장되는 값의 종류에도 제한은 없다.
# 저장 순서에 대한 순번(인덱스:index) 가 있음

# 리스트 생성 방법 1 : list() 함수 사용
list_1 = list()
print(list_1, type(list_1))

# 리스트 생성 방법 2 : [] 사용
list_2 = []
print(list_2, type(list_2))
# list 자료형 특징 1 : 문자열(str)과 같이 인덱싱, 슬라이싱 연산이 가능함
# index(순번: 저장 순서, 0부터 시작함)
# 인덱싱 표현 : 리스트변수[index]
list_3 = [1, 2, 3, 'python',3.56, [11, 22, 33], True, False]
print('0번째 기록된 값 조회 : ', list_3[0])
print('3번째 기록된 값 조회 : ', list_3[3])
print('5번째 기록된 값 조회 : ', list_3[5])

# 슬라이싱 : 리스트에 저장된 데이터들 부분 추출
# 표현 : 리스트변수[시작인덱스:끝인덱스:간격]
# 시작인덱스부터 끝인덱스 - 1 위치까지 추출됨
# 간격 : 생략되면 기본값 1임
print('0번 인덱스부터 3번 인덱스까지의 데이터 추출 : ', list_3[0:4:1])
print('0번 인덱스부터 3번 인덱스까지의 데이터 추출 : ', list_3[:4])

# len(리스트변수) : 리스트에 저장된 데이터 갯수 리턴
print('list_3 에 저장된 값 갯수 : ' ,len(list_3))

# len() 을 이용해서 마지막 위치의 값 조회에 활용할 수도 있음
print('list_3에 저장된 값의 마지막 인덱스 : ', len(list_3) - 1)
print('list_3 의 마지막 값 : ', list_3[len(list_3) - 1])

# list 자료형 특징 2 : 요소(element)의 값은 변경할 수 있음
# 변경할 값의 종류도 제한이 없다
# 인덱스 이용 : 리스트변수[인덱스] = 바꿀값
print('변경 전 : ', list_3)
list_3[0] = 77
print('변경 후 : ', list_3)
list_3[1] = 'test'
print('변경 후 : ', list_3)
list_3[2] = [1.2, 2.3, 2.4]
print('변경 후 : ', list_3)

# list 자료형 특징 3 : 리스트를 다루는 함수(메소드)들이 제공됨
# 리스트 변수, 함수명(전달인자)
# append() : 뒤에 추가
# insert() : 앨리먼트 사이에 추가
# remove() : 삭제
# pop() : 꺼내면서 리스트에서 제거
# reverse() : 리스트 안에 데이터 순서를 반대로 바꿈 (뒤집기)
# clear() : 리스트 비움

# chap05. 파이썬에서 제공하는 list 관련 함수 테스트 -------------------------------------------
lst = [1, 3, 5, 'list', True, 20, ['a', 'b', 'c']]
print(f'before : {lst}')
print(f'length: {len(lst)}')
print(f'after : {lst}')

# append() : 리스트 뒤로 추가, 마지막 인덱스 증가됨
# 리스트변수.append(추가할값)
lst.append(456)
print(f'before : {lst}')
print(f'length: {len(lst)}')

# remove() : 지정한 데이터 제거함, 갯수 줄어듦
# 리스트변수.remove(제거할값)
lst.remove(20)
print(f'before : {lst}')
print(f'length: {len(lst)}')

# 같은 값들이 여러 개 저장되어 있는 리스트인 경우
lst_1 = [1, 1, 2, 2, 1, 3]
print(f'before : {lst_1}')
print(f'length: {len(lst_1)}')

lst_1.remove(1) # 앞에서 부터 검색해서 첫번째로 만나는 값을 삭제함
print(f'before : {lst_1}')
print(f'length: {len(lst_1)}')

# insert() : 리스트 안의 원하는 위치에 추가
# 리스트변수.insert(위치인덱스, 추가할값)
lst.insert(1, '추가확인')
print(f'before : {lst}')
print(f'length: {len(lst)}')

# pop() : 인덱스 위치의 값을 꺼냄 (제거)
# 리스트변수.pop() : 마지막 위치의 값을 빼냄(제거)
# 리스트변수.pop(index) : 해당 인덱스 위치의 값을 빼냄
num = lst.pop()
print(f'before : {lst}')
print(f'length: {len(lst)}')
print(f'num: {num}')

lst.pop(3)
print(f'before : {lst}')
print(f'length: {len(lst)}')

# extend() : 기존 리스트 뒤쪽에 다른 리스트를 추가해서 리스트를 확장함
# 리스트변수1 .extend(리스트변수2)
lst.extend(lst_1)
print(f'before : {lst}')
print(f'length: {len(lst)}')

# reverse() : 리스트의 저장 순서를 반대로 뒤집기함
# 리스트변수.reverse()
lst.reverse()
print(f'before : {lst}')
print(f'length: {len(lst)}')

# sort() : 리스트의 저장 값들을 오름차순정렬 처리함
# 주의 : 한 가지 종류의 값들로만 저장되어 있을 때 사용할 수 있음ㄴ
# lst.sort() # TypeError: '<' not supported between instances of 'list' and 'int'

lst_int = [3, 63, 64, 23, 56, 37, 1, 2]
print(f'before : {lst_int}')
print(f'length: {len(lst_int)}')
lst_int.sort() # reverse=False 기본 값이므로 생략함, 오름차순정렬
print(f'after : {lst_int}')
lst_int.sort(reverse=True) # 내림차순정렬
print(f'after : {lst_int}')

lst_str = ['d', 'we', 'ax', 'bee', 'flam', 'e']
print('before : {}'.format(lst_str))
print('length : {}'.format(len(lst_str)))
lst_str.sort()
print('after : {}'.format(lst_str))
lst_str.sort(reverse=True)
print('after : {}'.format(lst_str))

lst_str_kr = ['에이', '우리', '도끼', '벌', '불', '이']
print('before : {}'.format(lst_str_kr))
print('length : {}'.format(len(lst_str_kr)))
lst_str_kr.sort()
print('after : {}'.format(lst_str_kr))
lst_str_kr.sort(reverse=True)
print('after : {}'.format(lst_str_kr))

# count() : 리스트에 저장된 똑같은 값의 갯수 조회
# 리스트변수.count(찾을값)
print(f'lst : {lst}')
print(f'lst 에 저장된 정수 1의 갯수 : ', lst.count(1))
