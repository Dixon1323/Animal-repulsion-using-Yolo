from ultralytics import YOLO
import cv2
import math 
import time
import requests



cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)


model = YOLO("best.pt")


classNames = ['boar', 'cat', 'dog', 'rabbit', 'rat']

val=requests.get("https://blynk.cloud/external/api/update?token=YOUR_AUTH_TOKEN&v0=10")
time.sleep(0.2)


while True:
    success, img = cap.read()
    results = model(img, stream=True)


    for r in results:
        boxes = r.boxes

        for box in boxes:

            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2) 

            

            
            confidence = math.ceil((box.conf[0]*100))/100
            print("Confidence --->",confidence)

            
            cls = int(box.cls[0])
            print("Class name -->", classNames[cls])
            a=classNames[cls]
            # print(a)

            
            org = [x1, y1+50]
            font = cv2.FONT_HERSHEY_SIMPLEX
            fontScale = 1
            color = (0, 0, 255)
            thickness = 2
            if(a=="dog"):
                cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
                print(x1," ",y1," ",x2," ",y2)
                cv2.putText(img, classNames[cls], org, font, fontScale, color, thickness)
                requests.get("https://blynk.cloud/external/api/update?token=YOUR_AUTH_TOKEN&v0=0")
                time.sleep(0.2)
                

            elif(a=="cat"):
                cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
                print(x1," ",y1," ",x2," ",y2)
                cv2.putText(img, classNames[cls], org, font, fontScale, color, thickness)
                requests.get("https://blynk.cloud/external/api/update?token=YOUR_AUTH_TOKEN&v0=1")
                time.sleep(0.2)
                


            elif(a=="boar"):
                cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
                print(x1," ",y1," ",x2," ",y2)
                cv2.putText(img, classNames[cls], org, font, fontScale, color, thickness)
                requests.get("https://blynk.cloud/external/api/update?token=YOUR_AUTH_TOKEN&v0=2")
                time.sleep(0.2)
                


            elif(a=="rabbit"):
                cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
                print(x1," ",y1," ",x2," ",y2)
                cv2.putText(img, classNames[cls], org, font, fontScale, color, thickness)
                requests.get("https://blynk.cloud/external/api/update?token=YOUR_AUTH_TOKEN&v0=3")
                time.sleep(0.2)
                


            elif(a=="rat"):
                cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
                print(x1," ",y1," ",x2," ",y2)
                cv2.putText(img, classNames[cls], org, font, fontScale, color, thickness)
                requests.get("https://blynk.cloud/external/api/update?token=YOUR_AUTH_TOKEN&v0=4")
                time.sleep(0.2)



    cv2.imshow('Webcam', img)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
