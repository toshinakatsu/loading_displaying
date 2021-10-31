import cv2
 
# 画像の読み込み
cv_img = cv2.imread('lena.jpg')

# 白画像を生成して表示する
black_img = cv_img * 0
white_img = black_img + 255
cv2.imshow("white_img", white_img)
cv2.waitKey(0) & amp; 0xFF == ord('q')