import numpy as np
import cv2

# 画像ファイルの読み込み
img_color = cv2.imread('coins.png')
img_gray = cv2.imread('coins.png', cv2.IMREAD_GRAYSCALE)

# 画像のGUI表示
cv2.imshow('color', img_color)  # この時点ではウィンドウは表示されない
cv2.waitKey(0)  # ここで初めてウィンドウが表示される

# cv2.destroyAllWindows()




