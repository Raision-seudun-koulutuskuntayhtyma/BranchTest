# EXAMPLE OF QT APPICATION FOR TAKING PRODUCT IMAGES WITH WEB CAMERA

# LIBRARIES AND MODULES
from PyQt5 import QtWidgets, uic # For the UI
from PyQt5.QtGui import QPixmap
import sys # For accessing system parameters
import photo # For vido processing functions


# CLASS DEFINITIONS

# Class for the main window
class Ui(QtWidgets.QMainWindow):

    # CONSTRUCTOR
    def __init__(self):
        super().__init__()

        # Load the ui file
        uic.loadUi('productPicture.ui', self)

        # PROPERTIES FOR WORKFLOW
        self.stop_capture_flag = False
        self.image_saved = False

        # UI OBJECTS

        # Set all buttons inital state to disabled
        self.startCaptureButton.setEnabled(False)
        # self.takeStillButton.setEnabled(False)

        # Controls and their corresponding UI elements (direct assignment to properties)
        self.product = self.productId
 
        # Indicators (direct assignment to properties)
        self.picture = self.kuvanPaikka
        

        # SIGNALS & SLOTS

        # Video päälle button signal to capture slot -> call capture function
        self.startCaptureButton.clicked.connect(self.capture)

        # If there has been change in the product field enable Start Capture button -> call show_start_button function
        self.product.textChanged.connect(self.show_start_button) 

        # Ota kuva button signal to exit capture mode and save the image -> call save_image function
        self.takeStillButton.clicked.connect(self.take_picture)

        # MAKE UI VISIBLE
        self.show()

    # METHODS

    # Capture video
    def capture(self):

        # Read the value of productId text field
        file_name = self.product.text()
        self.stop_capture_flag = False
        
        # Start Video Capture 
        # TODO: Muuta uudempaan funktioon qt_video_capture(cam_ix, margin, color)
        # photo.video_to_still_image(file_name, 0, 30, 'orange')
        photo.qt_video_capture(0, 20, 'yellow')

        # Enable Take Still button
        self.takeStillButton.setEnabled(True)
         

        # Disable Start Video Capture button
        self.startCaptureButton.setEnabled(False)

    # Enable Start Capture button   
    def show_start_button(self):
        self.startCaptureButton.setEnabled(True)   

    def take_picture(self):
        self.stop_capture_flag = True

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