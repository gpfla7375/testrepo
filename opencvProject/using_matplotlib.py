# using_matplotlib.py
# 이미지 읽어올 때 색상 채널 바꾸기
import matplotlib.pyplot as plt
import cv2

# 컬러 영상 출력
imgBGR = cv2.imread('./images/cat.bmp') # BGR 순으로 읽어들임
imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)
plt.axis("off")
# plt.imshow(imgBGR)
# plt.imshow(imgRGB)
# plt.show()

# 그레이스케일로 이미지 읽어 들이기
imgGray = cv2.imread('./images/cat.bmp', cv2.IMREAD_GRAYSCALE)

# 두 개의 영상을 함께 출력
plt.subplot(141), plt.axis("off"), plt.imshow(imgRGB)
plt.subplot(142), plt.axis("off"), plt.imshow(imgGray, cmap='gray')
plt.subplot(143), plt.axis("off"), plt.imshow(imgRGB)
plt.subplot(144), plt.axis("off"), plt.imshow(imgBGR)
plt.subplot(245), plt.axis("off"), plt.imshow(imgGray)
plt.subplot(246), plt.axis("off"), plt.imshow(imgRGB)
plt.subplot(247), plt.axis("off"), plt.imshow(imgGray)
plt.subplot(248), plt.axis("off"), plt.imshow(imgBGR)
plt.subplot(341), plt.axis("off"), plt.imshow(imgGray)
plt.subplot(342), plt.axis("off"), plt.imshow(imgRGB)
plt.subplot(343), plt.axis("off"), plt.imshow(imgGray)
plt.subplot(344), plt.axis("off"), plt.imshow(imgBGR)
plt.show()