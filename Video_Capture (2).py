import cv2

vidcap= cv2.VideoCapture(0)
vidcod= cv2.VideoWriter_fourcc(*"XVID")
output= cv2.VideoWriter("mycam.mp4",vidcod, 20.0,(640,480))

while (True):
    ret,frame= vidcap.read()
    grayFrame= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    cv2.imshow("My  Colour Video", frame)
    cv2.imshow("My Grayscale Video",grayFrame)
    output.write(frame)
    if cv2.waitKey(1) &0XFF == ord("x"):
        break

vidcap.release()
output.release()
cv2.destroyAllWindows()
