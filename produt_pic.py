# CREATE A STILL PRODUCT IMAGE FROM WEBCAM STREAM
# -----------------------------------------------

# LIBRARIES AND MODULES

# OpenCV for image and video manipulatation
# External library must be installed with pip: pip install opencv-python
import cv2

# NumPy for array and matrix operations
# Will be automatically installed with openCV
import numpy

# Set the camera index
cam_index = int(input('Anna kameran indeksi 0 - Cannon, 1 - Thinkpad: '))

# Ask the file name for product image
file_name = input('Anna kuvatidoston nimi: ')

# Ask the scalling ratio for product image, 1 when no scale given or invalid scale factor
ratio_str = input('Anna kuvan skaalauskerroin: ')
try:
    ratio = float(ratio_str)
except:
    print('Invalid scale factor, using original video size')
    ratio = 1

# Ask the safety margin in pixels
safety_margin = int(input('Syötö turvamarginaali kuvapisteinä: '))

# Creating a VideoCapture object for the wideo stream from the Web camera
video_stream = cv2.VideoCapture(cam_index)

# Loop until iterrupted by keystroke s -> save
while (video_stream.isOpened()):

    # Capture the stream frame by frame, read() fuction returns true if reading is successfull and a wideo frame
    ret, frame = video_stream.read()

    # Check if capture is successfull
    if ret == True:

        # Find out frame dimensions and number of channels (for proportional resizing)
        org_height, org_width, channels = frame.shape

        # Dimensions for the video window and the still image
        picture_width = int(round(org_width * ratio, 0))
        picture_height = int(round(org_height * ratio, 0))

        # Resize the frame for database use using bicubic interpolation
        frame = cv2.resize(frame, (picture_width, picture_height),
                           fx=0, fy=0, interpolation=cv2.INTER_CUBIC)
        
        # Draw a red safe area rectangle into frame (BGR colour space, line 4 px)
        top_left = (safety_margin, safety_margin)
        bottom_right = (picture_width - safety_margin, picture_height - safety_margin)
        cv2.rectangle(frame, top_left, bottom_right, (0, 0, 255), 1)

        # Display the video frame in a window named Video stream
        cv2.imshow('Video stream with safe area', frame)
        

    # Define a key stroke s as the save and exit from video streaming, wait 25 ms for key storke
    if cv2.waitKey(25) & 0xFF == ord('s'):
        break

# Save the last captured frame as jpg image (without rectangle)
ret, frame = video_stream.read()
if ret == True:
    cv2.imwrite(file_name, frame)
    print('Kuva tallennetu työhakemistoon nimellä', file_name)

# Release the video capture object
video_stream.release()

# Read the still image and show it in a new window
still_image = cv2.imread(file_name)
cv2.imshow('Still image', still_image)

# Show original frame dimensions on the console
print('Alkuperäinen kuvakoko oli', org_width, 'x', org_height,
      'pikseliä ja kuvassa on', channels, 'kanavaa')

# Wait for key stroke q to close all open video and picture windows
while True:
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Closes all the windows currently opened.
cv2.destroyAllWindows()
