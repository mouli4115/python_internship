import cv2
image=cv2.imread("image2.jpg")
# print(image)
gry=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imwrite("grey.png",gry)