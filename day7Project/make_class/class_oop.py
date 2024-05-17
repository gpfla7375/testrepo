# path : make_class\\class_oop.py
# 파이썬에서 객체 지향 프로그래밍(OOP) 적용

# 객체 지향 프로그래밍에서의 클래스 멤버는
# field(멤버변수), method(멤버함수), constructor(생성자), destructor(소멸자)
# oop 에 사용되는 기술 (3대 특징)도 적용해야 함
# encapsulation(캡슐화), inheritance(상속), polymorphism(다형성)

# oop 적용 기술 1 : 캡슐화
# 캡슐화 : 데이터 보호가 목적임, 필드에 접근제한을 설정해야 함
# 필드에 접근제한자(access modifier)를 사용하게 됨
# private(비공개), public(공개), protected(상속시 후손에게만 공개)

# 파이썬에서는 접근제한자 없음 (제공 안 됨)
# 파이썬에서는 기본적으로 모든 멤버는 public 임
# 레퍼런스.필드명, 클래스명.필드명
# 레퍼런스.메소드명(), 클래스명.메소드()

# private : 클래스 밖에서 사용 못 함, 클래스 안에서만 사용할 수 있음
# 파이썬에서 클래스 멤버를 비공개(private) 처리하려면,
# 필드명이나 메소드명 이름 앞에 '_'(underscore) 를 2개 붙이면 됨
class PClass:
    # field (private)
    __num = 10
    
    # constructor 추가 : 매개변수 있는 생성자를 작성함
    def __init__(self, num):
        self.__num = num

    # method (public)
    def set_num(self, n):
        self.__num = n

    def get_num(self):
        return self.__num

# ----------------------------------------------------

# 클래스 멤버 사용
# pref = PClass() # 기본생성자 자동 실행됨, 객체 공간 할당하고 주소 리턴함
# print('pref 가 가진 주소로 참조접근 : ', id(pref))
# print('인스턴스 안의 __num 값 : ', pref.get_num())

# 클래스 밖에서 필드 접근 확인
# print('인스턴스 안의 __num 값 : ', pref.__num) # private 이므로 AttributeError

# 생성자 (Constructor)
# 객체 인스턴스가 메모리에 할당될 때, 필드 초기화가 목적인 함수
# 생성자가 없으면, 내부에서 기본생성자 자동 작동됨
# 생성자를 작성한다면, __init__ 로 정의해야 함
# 파이썬에서는 생성자는 오버로딩(overloading) 할 수 없음 : 생성자는 1개 (기본 또는 매개변수 있는 생성자)
'''
class 클래스명:
    def __init__(self, 매개변수):   # 주로 매개변수 있는 생성자를 작성함
        self.필드명 = 매개변수

생성자 사용 :
레퍼런스변수 = 클래스명() # 기본생성자로 객체 인스턴스 할당하고 주소 리턴
레퍼런스변수 = 클래스명(전달값)  # 매개변수 있는 생성자 실행하고 주소 리턴
'''

# 추가된 생성자 확인
pref2 = PClass(20)
print('pref2 가 참조하는 인스턴스 안의 필드값 확인 : ', pref2.get_num())

# destructor (소멸자 함수)
# 객체 인스턴스가 메모리에서 제거될 떄 자동 실행되는 함수임
# 클래스 안에 직접 작성한다면, __del__ 로 함수 정의함
# 해당 객체 관련 메모리나 자원들의 공유 설정, 점유 설정 등을 해제할 떄
'''
class 클래스명:
    def __del__(self):
        해당 클래스 객체가 소멸될 때 같이 제거 또는 해제할 내용에 대한 코드 작성
'''

class Var:
    # field : private
    __number : 100

    # constructor
    def __init__(self, n):
        self.__number = n

    # destructor
    def __del__(self):
        print('인스턴스 제거시 자동 작동됨!', id(self))


    # method : getter and setter
    def set_number(self, n):
        self.__number = n

    def get_number(self):
        return self.__number

# Var -----------------------------------------------
# 클래스 객체 생성
v1 = Var(77)
v2 = Var(99)

print('v1 : ', v1.get_number(), id(v1))
print('v2 : ', v2.get_number(), id(v2))
# 프로그램 종료시 소멸자가 자동 실행됨

# 키보드로 값을 입력받아서 필드값 변경 처리
# v1.set_number(int(input('v1 참조 객체의 변경할 필드값 : ')))
# print('v1 : ', v1.get_number(), id(v1))
# v2.set_number(int(input('v2 참조 객체의 변경할 필드값 : ')))
# print('v2 : ', v2.get_number(), id(v2))

# 정적 메소드 (static method) ----------------------------------------------
# 프로그램 실행시 정적 메모리(static)에 따로 기록되는 메소드를 말함
# 메소드 작성시 메소드 이름 위에 장식자(decorator == 어노테이션: annotation)
# @staticmethod
# self 가 없는 메소드임 => 메소드 사용 : 클래스명.메소드()

class C:
    def ham(self, x, y):
        print('instance method : ', x, y)   # 주소를 자동으로 전달받아서(self), 객체 인스턴스에 접근하는 메소드

class D:
    @staticmethod
    def spam(x, y): # static 메모리에 로딩됨, self 매개변수 없음
        print('static or class method : ', x, y)

# static method 는 사용시 객체 레퍼런스(인스턴스의 주소) 없이 실행 => self 가 없음
# 클래스명.method(전달값)
D.spam(100, 200)

# static method 를 instance method 처럼 사용해도 됨
dref = D()
dref.spam(100, 200)

# instance method 사용
# C.ham(11, 22) # static method 처럼 사용할 수 없음 => self 에게 반드시 주소 전달 필요함
# 해결방법 : 직접 주소 전달하면 됨
cref = C().ham(10, 20)
C.ham(id(cref), 20, 10)



