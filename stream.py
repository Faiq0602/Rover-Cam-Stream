import cv2 as cv
cam = cv.VideoCapture("http://192.168.94.65:8080/video")
while(True):
	ret , frame = cam.read()
	cv.imshow('livestream' , frame)
	if cv.waitKey(1) == ord("q"):
		break
		
capture.release()
cv.destroyAllWindows()
