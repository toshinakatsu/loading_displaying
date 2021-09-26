import cv2

img = cv2.imread('messi5.jpg')

print(type(img))  # <class 'numpy.ndarray'>
print(img.shape)  # (520, 520, 3)   (高さ, 幅, 色) を取得

# タプルを変数に代入
h, w, c = img.shape
print('height : ', h)
print('width : ', w)
print('channel : ', c)


# 変数に代入せず、インデックスで指定
print('height : ', img.shape[0])
print('width : ', img.shape[1])

# (幅, 高さ) のタプルを取得
print(img.shape[1::-1])



