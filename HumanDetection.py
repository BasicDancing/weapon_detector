# Age and Gender Detection
import cv2

from deepface import DeepFace
from EmailSending import send_event
from TextRW import write_age

import threading

age_detect = threading.Event()

age_file = open("age.txt","w")

def age_detection():
    while True:
        age_detect.wait()
        age_detect.clear()

        # add image for analysis
        img1 = cv2.imread("weapon.png")

        age = "There is no face to detact!"

         # Get results
        try:
            result = DeepFace.analyze(img1, actions=['age'], enforce_detection=False)
            age = int(result[0]['age'])
            print("Age :", age)

            write_age(age)

            if age >= 15:
                send_event.set()
        except:
            print(age)
