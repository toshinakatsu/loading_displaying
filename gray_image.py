import cv2

# 画像の読み込み
cv_img = cv2.imread('lena.jpg')

# 黒画像・白画像を生成する
black_img = cv_img * 0
white_img = black_img + 255

# Create gray_img(overlay)
gray_img = cv2.addWeighted(black_img, 0.5, white_img, 0.5, 0)

# 画像を表示する
cv2.imshow("gray_img", gray_img)
cv2.waitKey(0) & amp; 0xFF == ord('q')