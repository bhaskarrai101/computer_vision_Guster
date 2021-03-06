import cv2
import mediapipe as mp
import time

# create vedio object
cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands() # this calsss uses only RGB color images
mpDraw = mp.solutions.drawing_utils # we draw marks on hands
# for frame rate
pTime= 0
cTime= 0

while True:
    success, img = cap.read() #This will give our frame
    
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #we need to convert it from BGR to RGB
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)
    
    if results.multi_hand_landmarks:
        # for loop to detect multiple hands
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                #print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                print(id,cx,cy)
                if id == 8:
                    cv2.circle(img, (cx,cy), 15,(179,89,55),cv2.FILLED)
                
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
    
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    
    cv2.putText(img, str(int(fps)),(10,70), cv2.FONT_HERSHEY_PLAIN,3,(255,255,0),3)
    
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()