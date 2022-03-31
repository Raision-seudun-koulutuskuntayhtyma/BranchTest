# EXAMPLE OF QT APPICATION FOR TAKING PRODUCT IMAGES WITH WEB CAMERA

# LIBRARIES AND MODULES
from PyQt5 import QtWidgets, uic # For the UI
from PyQt5.QtCore import QThread, pyqtSignal # For creating multiple threads and signaling between UI and Video thread
from PyQt5.QtCore import Qt # For scaling video to indicator object
from PyQt5.QtGui import QImage, QPixmap # For image handling

import sys # For accessing system parameters
import cv2 # For accesing open CV functions
import photo # For vido our home made vido processing functions

# CLASS DEFINITIONS

# A class to create another thread to handle the video and preventing the GUI from freezing while streaming
class VideoThread(QThread):
    def __init__(self, cam_ix, margin, color):
        super().__init__()
        self.cam_ix = cam_ix
        self.margin = margin
        self.color = color

    # Create a signal to uppdate the Wideo output element
    changeVideoImage = pyqtSignal(QImage)

    # The actual task to run on thread
    def run(self):
        video_stream = cv2.VideoCapture(self.cam_ix)
        # Capture the stream frame by frame, read() fuction returns true if reading is successfull and a wideo frame
        ret, frame = video_stream.read()

        # Check if capture is successfull and return a frame
        if ret == True:

            # read dimensions of the frame
            height, width, channels = frame.shape
            vf_color = photo.color_bgr_values(self.color)

            # Add a view finder
            photo.create_view_finder(frame, width, height, self.margin, vf_color)

            # Convert the frame to QT format
            rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # BGR -> RGB
            line_bytes = channels * width # Calcutate amount of bytes in a single video line
            qt_formatted_frame = QImage(rgb_image.data, width, height, line_bytes, QImage.Format_RGB888)

            # Scale the original video to fit its place in the UI
            video_view = qt_formatted_frame.scaled(640, 480, Qt.KeepAspectRatio)

            # Emit the video to UI using signal changeVideoImage
            self.changeVideoImage.emit(video_view)

