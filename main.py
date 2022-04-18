import cv2
import numpy as np
import mouse




cam = cv2.VideoCapture(0)

while True:
    check, img = cam.read() 
    frame = np.array(img)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, np.array([110, 200, 20]), np.array([130, 255, 255]))
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if 3000 > area > 100:
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            mouse.drag(0, 0, x, y, absolute=False, duration=0.1)
            mouse.click("left")


    cv2.imshow('Screen', frame)
    cv2.imshow("Identifier", mask)


    c = cv2.waitKey(1)
    if c == 33:
        break

cv2.destroyAllWindows()
