# camera_save.py
# 카메라를 통해 들어오는 영상 프레임을 저장 처리

import cv2
import sys

# 시스템 기본 카메라를 cv2.VideoCapture 객체로 생성
cap = cv2.VideoCapture(0)   # 카메라 열기함

if not cap.isOpened():  # 카메라 열기가 실패했다면
    print('Camera is not opened')
    sys.exit()

# 프레임 해상도, 초당 프레임수(fps)
print('Frame width : ', round(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
print('Frame height : ', round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('FPS : ', round(cap.get(cv2.CAP_PROP_FPS)))

# 동영상 저장을 위한 cv2.VideoWriter 객체 생성
fw = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
fh = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = round(cap.get(cv2.CAP_PROP_FPS))
fourcc = cv2.VideoWriter_fourcc(*'DIVX')   # *'DIVX' == 'D', 'I', 'V', 'X'

out = cv2.VideoWriter('./multi/output.avi', fourcc, fps, (fw, fh))

# 매 프레임 처리 및 화면 출력, 동영상 저장 처리
while True:
    ret, frame = cap.read()    # 다른 앱에서 카메라 사용 중이면 작동 안 됨

    if not ret:     # ret 가 False 이면
        break

    edge = cv2.Canny(frame, 50, 150)  # 경계선 검출 함수
    edge = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR)
    # out.write(edge)   # 파일로 저장
    out.write(frame)  # 파일로 저장

    cv2.imshow('frame', frame)
    cv2.imshow('edge', edge)

    if cv2.waitKey(1) == 27:  # esc 키
        break
# while end ----------------------------

cap.release()
out.release()
cv2.destroyAllWindows()
