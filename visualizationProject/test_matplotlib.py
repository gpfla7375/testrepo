# test_matplotlib.py
# matplotlib 모듈 사용한 시각화 테스트

# matplotlib 패키지 설치함
import matplotlib as mpl
import matplotlib.pyplot as plt

def test_plot1():
    '간단한 plot 그리기 : 기본은 선그래프임 (line plot)'
    # 그래프로 표현할 데이터는 리스트 또는 배열이여야 함
    sample_data = [4, 0, 2, 1, 8]
    plt.title("전반기 실적") # 그래프 제목 지정 함수
    plt.plot(sample_data)   # 선그래프 만드는 함수
    plt.show()  # 만든 그래프 출력 함수


def test_plot2():
    # title('표시할 제목') : 그래프 제목 지정 함수
    # x 축 값도 함께 지정 : plot([x축 값들], [y축 값들])
    x_data = [10, 20, 30, 40]
    y_data = [1, 4, 9, 16]
    plt.title('x ticks')
    plt.plot(x_data, y_data)
    plt.show()

# 그래프에 한글을 사용하려면, 한글폰트 파일을 다운받아서 사용함 ---------------------------
import matplotlib.font_manager as fm

def test_fonts():
    # 라이브러리 자원(설치한 패키지) 저장 폴더 경로 확인하기
    print(mpl.matplotlib_fname())
    # matplotlib 모듈에서 다운받은 글꼴을 그래프(plot)의 기본 글꼴로 사용하게 하려면,
    # D:\python_workspace\visualizationProject\.venv\lib\site-packages\matplotlib\mpl-data\fonts\ttf
    # ttf 폴더 안에 다운받은 글꼴파일을 복사해 넣음
    # 참고 : 압축 푼 ttf 파일을 더블 클릭해서 설치 버튼 누르고 설치한 경우에는
    #   C:\\windows\\fonts 에 기본 설치됨
    
    # 글꼴 파일 복사해놓고 나서, matplotlib 캐시에 변경 내용 반영함
    # 1. 캐시 파일 저장 위치 확인함
    print(mpl.get_cachedir())
    # 2. 해당 위치의 캐시파일을 직접 파일탐색기에서 찾아내서 삭제함
    #   => 이전 폰트리스트 정보를 가진 캐시임
    # 3. 프로그램 다시 실행 (shift + F10)하면 캐시 파일 생김 > 파일 탐색기에서 확인함
    #   => 만약, 캐시파일 안 생기면 컴퓨터 리부팅함

def test_fonts2():
    # 폰트 설정
    # 첫번째 방법 : rc parameter 를 설정해서, 설정 이후 그래프 작업 전체에 사용하게 함

    # 현재 사용되고 있는 폰트 종류와 글자 크기 확인
    print(mpl.rcParams['font.family'])
    print(mpl.rcParams['font.size'])

    # 한글 폰트로 설정 변경해 봄
    mpl.rc('font',family='NanumGothic')
    mpl.rc('axes', unicode_minus=False)
    # axes 에 적용되는 유니코드(0 ~ 65535) 숫자에 음수 부호 사용 해제 설정

    # 그래프에 설정된 글꼴을 사용 확인
    plt.title("오늘 매출추이")
    plt.plot([2, 4, 8, 10], [1, 2, 3, 4])
    plt.xlabel('월')
    plt.ylabel('일일')
    plt.show()


def test_fonts3():
    # 그래프에 특정 부분만 원하는 글꼴로 설정을 변경할 수도 있음
    # 이용할 글꼴 파일의 위치는 어디든 상관없음
    # font_path = '드라이브:/경로명.../글꼴파일이 있는 폴더명/사용할 글꼴파일명.확장자
    font_path = './fonts/NanumMyeongjoExtraBold.ttf'
    font_prop = fm.FontProperties(fname=font_path)
    plt.title('axis 테스트용', fontproperties=font_prop)
    plt.xlabel('0 ~ 10', fontproperties=font_prop)
    plt.ylabel('0 ~ 100', fontproperties=font_prop)
    plt.plot([1, 4, 6, 8],[10, 20, 30, 40], 'ro')
    plt.axis((0, 10, 0, 100))
    plt.show()


def test_fonts4():
    # 각 객체마다 별도의 폰트 적용 : fontdict 인수에 넣어서 사용함
    font1 = {'family': 'NanumGothic', 'size':24, 'color':'blue',  'weight': 'bold'}
    font2 = {'family': 'NanumMyeongjo', 'size': 16, 'color': 'green', 'weight': 'bold'}
    font3 = {'family': 'NanumGothic', 'size': 12, 'color': 'black', 'weight': 'bold'}
    plt.title('axis 테스트용', fontdict=font1)
    plt.xlabel('0 ~ 10', fontdict=font2)
    plt.ylabel('0 ~ 100', fontdict=font3)
    plt.plot([1, 4, 6, 8], [10, 20, 30, 40], 'ro')
    plt.axis((0, 10, 0, 100))
    plt.show()




# 함수 실행
if __name__ == '__main__':
    # test_plot1()
    # test_plot2()
    # test_fonts()
    # test_fonts2()
    # test_fonts3()
    test_fonts4()