# Age and Gender Detection
import cv2
from deepface import DeepFace

# add image for analysis
img1 = cv2.imread("Rezwan.jpg")

# Get results
result = DeepFace.analyze(img1, actions=['age', 'gender'])
print(result)
