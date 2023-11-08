from EmailSending import send_mail
from Detection import capture_detected
import threading

# Create threading events
capture_event = threading.Event()
send_event = threading.Event()

# Create threads for capturing the image and sending the email
capture_thread = threading.Thread(target=capture_detected)
send_thread = threading.Thread(target=send_mail)

# Start the threads
capture_thread.start()
send_thread.start()

# Wait for both threads to finish