# dnnface\\dnnface.py
# 딥러닝 ai 학습모델 다운받아서, 카메라 영상에서 얼굴 인식 처리
import sys
import cv2
import numpy as np

# 영상 이미지에서 얼굴을 인식하는 ai 학습모델 (caffe 모델에서 다운받은 것임)
model = 'res10_300x300_ssd_iter_140000_fp16.caffemodel'
config = 'deploy.prototxt'

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('Error opening video stream or file')
    sys.exit()

# opencv 가 제공하는 dnn 사용
net = cv2.dnn.readNet(model, config)
if net.empty():
    print('Net open failed!')
    sys.exit()
    
# 영상에서 얼굴 인식 출력 확인
while True:
    ret, frame = cap.read()
    if not ret: # ret (리턴값)이 False 이면
        break
    # opencv 가 제공하는 dnn 사용
    # DNN 모듈에 이미지를 입력으로 제공
    blob = cv2.dnn.blobFromImage(frame, 1.0, (300, 300), (104.0, 177.0, 123.0))
    net.setInput(blob)
    detect = net.forward()  # ai 실행

    # print('detect shape: ', detect.shape)
    (h, w) = frame.shape[:2]
    detect = detect[0, 0, :, :]

    # 얼굴 위치에서 계산 처리
    for i in range(detect.shape[0]):
        confidence = detect[i, 2]
        if confidence < 0.5:
            break
        x1 = int(detect[i, 3] * w)
        y1 = int(detect[i, 4] * h)
        x2 = int(detect[i, 5] * w)
        y2 = int(detect[i, 6] * h)
        
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0)) # 얼굴 위치에 초록색 사각형 선 표시

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == 27:
        break

    # while ---------------------------------------------------------------
cv2.destroyAllWindows()
