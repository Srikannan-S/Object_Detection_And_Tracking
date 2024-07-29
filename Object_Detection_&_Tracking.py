import imutils
import cv2

# HSV Values in low and high for the particular object
redLower=(0,0,111)
redUpper=(178,144,221)

# Cam Ini
cam=cv2.VideoCapture(0)

while True:
    _,frame=cam.read()

    # Imutils is used to resize the output frame
    frame=imutils.resize(frame,width=1000)

    # Converting into blur 
    blurred=cv2.GaussianBlur(frame,(11,11),0)

    # COnverting the blur image into HSV
    hsv=cv2.cvtColor(blurred,cv2.COLOR_BGR2HSV)

    # Mask the blue color only

    mask=cv2.inRange(hsv,redLower,redUpper)
    mask=cv2.erode(mask,None,iterations=2)
    mask=cv2.dilate(mask,None,iterations=2)

    cnts=cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,
                          cv2.CHAIN_APPROX_SIMPLE)[-2]
    center=None
    if len(cnts)>0:
        c=max(cnts,key=cv2.contourArea)
        ((x,y),radius)=cv2.minEnclosingCircle(c)
        # Getting centroid
        M=cv2.moments(c)
        # Getting center
        center=(int(M["m10"]/M["m00"]),int(M["m01"]/M["m00"]))
        if radius > 10:
            # Entire Circle
            cv2.circle(frame,(int(x),int(y)),int(radius),(0,225,255),2)
            # Center Circle
            cv2.circle(frame,center,5,(0,255,0),-1)

            # To get the values to check left or right print(center,radius)

            if radius > 250:
                print("stop")
            else:
                if(center[0]<150):
                    print("Right")
                elif(center[0]>450):
                    print("Left")
                elif(radius<250):
                    print("Front")
                else:
                    print("Stop")

    cv2.imshow("Frame",frame)
    key=cv2.waitKey(1)
    if key== ord("q"):
        break
    
cam.release()
cv2.destroyAllWindows()
