from EmailSending import send_mail
from Detection import capture_detected
from HumanDetection import age_detection
import threading

# Create threads for capturing the image and sending the email
capture_thread = threading.Thread(target=capture_detected)
age_thread = threading.Thread(target=age_detection)
send_thread = threading.Thread(target=send_mail)

# Start the threads
capture_thread.start()
age_thread.start()
send_thread.start()