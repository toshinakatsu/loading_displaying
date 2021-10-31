import cv2
 
# 画像の読み込み
cv_img = cv2.imread('lena.jpg')

# 黒画像を生成して表示する
black_img = cv_img * 0
cv2.imshow("black_img", black_img)
cv2.waitKey(0) & amp; 0xFF == ord('q')