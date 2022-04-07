# EXAMPLE OF QT WIDGET FOR TAKING PRODUCT IMAGES WITH WEB CAMERA

# LIBRARIES AND MODULES

from PyQt5 import QtWidgets, uic # For the UI, PyQT must be installed with pip first
from PyQt5.QtGui import QPixmap # For creating pixel maps from files
import sys # For accessing system parameters

import qimage2ndarray # Library for converting between QImages and numpy arrays, must be installed with pip

import cv2 # Library for imange manipulation, must be installed with pip
import photo # Home brew module for video capture


# CLASS DEFINITIONS

# Class for the widget window
class Ui(QtWidgets.QWidget):

    # CONSTRUCTOR
    def __init__(self):
        super().__init__()

        # Load the ui file
        uic.loadUi('videoWidget.ui', self)
       

        # UI OBJECTS

        # Set all buttons inital state to disabled
        self.captureButton.setEnabled(False)
        self.stillButton.setEnabled(False)
        self.saveButton.setEnabled(False)

        # Controls and their corresponding UI elements (direct assignment to properties)
        self.product = self.productId
 
        # Indicators (direct assignment to properties)
        self.picture = self.productImage

        # Set the product image to no image
        self.pixmap = QPixmap('none.png') # Create pixmap from png file
        self.picture.setPixmap(self.pixmap) # Update product picture
        

        # SIGNALS & SLOTS

        # Start Capture button signal to capture slot -> call capture function
        self.captureButton.clicked.connect(self.capture)

        # If there has been change in the product field enable Start Capture button -> call show_start_button function
        self.product.textChanged.connect(self.show_start_button) 

        # Take Still button signal to exit capture mode and save the image -> call save_image function
        self.stillButton.clicked.connect(self.take_picture)

        # MAKE UI VISIBLE
        self.show()

    # METHODS

    # Capture video
    def capture(self):

        # Read the value of productId text field
        self.fileName = self.product.text()
        self.stop_capture_flag = False
        
        # Start Video Capture and convert output to QImage format
        # TODO: Move conversions qt_vide_capture function in module photo.py
        
        frame = photo.qt_video_capture(0, 20, 'yellow') # Capture and add a view finder, last frame out without view finder
        rgbFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # Convert last frame to RGB
        self.photo = qimage2ndarray.array2qimage(rgbFrame) # Convert the pixel array to QImage format

        # Enable Take Still button
        self.stillButton.setEnabled(True)
         

        # Disable Start Video Capture button
        self.captureButton.setEnabled(False)

    # Enable Start Capture button   
    def show_start_button(self):
        self.captureButton.setEnabled(True)   

    def take_picture(self):
        self.stop_capture_flag = True
        self.pixmap = QPixmap(self.photo)
        self.picture.setPixmap(self.pixmap)
    '''
    # Play sound
    def tone(self):
        if self.calculateFrequency() < 37:
            sound.warn_sound()
            alarmWindow = QtWidgets.QMessageBox()
            alarmWindow.setText('Frequency shoud be 37 Hz at minimum')
            alarmWindow.setWindowTitle('Frequency error')
            alarmWindow.exec_()

            # Set the minimum allowed value
            self.tens.setValue(3)
            self.ones.setValue(7)

        else:        
            sound.create_sound(self.calculateFrequency(), self.duration.value())
'''
'''
 # Calculate frequency
    def calculateFrequency(self):
        fthousands = self.thousands.value() * 1000
        fhundreds = self.hundreds.value() * 100
        ftens = self.tens.value() * 10
        fones = self.ones.value()
        frequency = fthousands + fhundreds + ftens + fones 
        return frequency

    # Update the LCD
    def updateLcd(self):
        self.bigLcd.display(self.calculateFrequency())

    # Load preset
    def loadPreset(self, d1, d2, d3, d4):
        self.thousands.setValue(d1)
        self.hundreds.setValue(d2)
        self.tens.setValue(d3)
        self.ones.setValue(d4)
'''

# CREATE & RUN UI

app = QtWidgets.QApplication(sys.argv)
mainwindow = Ui()
app.exec_()