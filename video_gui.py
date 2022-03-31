# EXAMPLE OF QT APPICATION FOR TAKING PRODUCT IMAGES WITH WEB CAMERA

# LIBRARIES AND MODULES
from PyQt5 import QtWidgets, uic # For the UI
from PyQt5.QtCore import QThread, pyqtSignal # For creating multiple threads and signaling between UI and Video thread
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

    # The actual task to run
    def run(self):
        video_stream = cv2.VideoCapture(self.cam_ix)
        while (video_stream.isOpened()):
            pass
