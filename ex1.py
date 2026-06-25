import cv2
img=cv2.imread("sample1.jpg")
cv2.imshow("tulips",img)
cv2.imwrite("tulips.jpg",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
