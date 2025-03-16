import cv2
import numpy as np

input_path = "./texture-2.jpg"
output_path = "./"

texture = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)
(h,w) = texture.shape


texture = cv2.resize(texture,(355,298))


# brush[brush>=125] = 255
# brush[brush<125] = 0
cv2.imshow('texture', texture)
cv2.waitKey(0) 
cv2.imwrite(output_path + "/texture-2.png", texture)


# brush[brush<120] = 255

# bgr = cv2.cvtColor(brush,cv2.COLOR_GRAY2BGR)
# hsv = cv2.cvtColor(bgr,cv2.COLOR_BGR2HSV)

# value_mean = hsv[brush>120,2].mean()
# print(value_mean/255)

# canvas = cv2.cvtColor(canvas, cv2.COLOR_HSV2BGR)
# cv2.imshow('brush', canvas)
# cv2.waitKey(0)




# ret2,th2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# img = np.uint8(img*th2.astype("float32")/255)
# cv2.imwrite(output_path + "/brush.png", img)
# cv2.imshow('up', img)
# cv2.waitKey(0) 