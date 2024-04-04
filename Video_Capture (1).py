import cv2 as cv

vid_capture= cv.VideoCapture(0)
vid_cod= cv.VideoWriter_fourcc(*'XVID')
output= cv.VideoWriter("cam_video.mp4",vid_cod,20.0, (640,480))

while (True):
    ret,frame= vid_capture.read()
    cv.imshow("My Camera Video", frame)
    output.write(frame)
    if cv.waitKey(1) &0XFF == ord('x'):
        break

vid_capture.release()
output.release()
cv.destroyAllWindows()
