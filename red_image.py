import cv2

# 画像の読み込み
cv_img = cv2.imread('lena.jpg')

# 黒画像・白画像を生成する
black_img = cv_img * 0
white_img = black_img + 255

# Create Red_img(Split ⇒ Marge)
blue_img_cb, green_img_cb, red_img_cb = cv2.split(black_img) # all "0"
blue_img_cw, green_img_cw, red_img_cw = cv2.split(white_img) # all "255"
red_img = cv2.merge((blue_img_cb, green_img_cb, red_img_cw)) # (b,g,r) = (0,0,255)

# 画像を表示する
cv2.imshow("red_img", red_img)
cv2.waitKey(0) & amp; 0xFF == ord('q')