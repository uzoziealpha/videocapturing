import cv2, time

#this triggers video objects to open the camera
video=cv2.VideoCapture(0)

#to see 
check, frame = video.read()
print(check)
# the fame bring the numpy array for us to use to see the captured frame
print(frame)


#converting the video frame into a gray image
gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)


# The time library holds the release for 3 seconds
time.sleep(3)

#creates a window to show the first frame of the video
cv2.imshow("Capturing", gray)



cv2.waitKey(0)
video.release()
cv2.destroyAllWindows