# CREATE A STILL PRODUCT IMAGE FROM WEBCAM STREAM
# -----------------------------------------------

# LIBRARIES AND MODULES

# OpenCV for image and video manipulatation
import cv2

# NumPy for array and matrice operations
import numpy

# Dimensions for the video window and the still image
picture_width = 400
picture_height = 300

# Creating a VideoCapture object for the wideo stream from the first Web camera ie unit 0
video_stream = cv2.VideoCapture(0)
 
# Loop until iterruptd by keystroke s -> save
while (video_stream.isOpened()):

    # Capture the stream frame by frame, read() fuction returns true if reading is successfull and a wideo frame
    ret, frame = video_stream.read()

    # Check if capture is successfull
    if ret == True:
        
        # Resize the frame for database use using cubic interpolation
        frame = cv2.resize(frame, (picture_width, picture_height), fx = 0, fy = 0, interpolation = cv2.INTER_CUBIC)
 
    # Display the video frame
    cv2.imshow('Video stream', frame)
     
    # Define key stroke s as the save and exit from video streaming 
    if cv2.waitKey(25) & 0xFF == ord('s'):
        break

# Save the last captured frame as jpg
cv2.imwrite('product.jpg', frame)
print('Kuva tallennetu työhakemistoon nimellä product.jpg')

# Release the video capture object
video_stream.release()

# Read the still image and show it in a new window
still_image = cv2.imread('product.jpg')
cv2.imshow('Still image', still_image)

# Wait for key stroke q to close all open video and picture windows
while True:
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
 
# Closes all the windows currently opened.
cv2.destroyAllWindows()