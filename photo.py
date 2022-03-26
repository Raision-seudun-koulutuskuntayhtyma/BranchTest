# FUNCTIONS FOR WEB CAMERA IMAGE MANIPULATION
# -------------------------------------------

# MODULES AND LIBRARIES

# OpenCV for image and video manipulatation
# External library must be installed with pip: pip install opencv-python
import cv2

# NumPy for array and matrix operations
# Will be automatically installed with openCV
import numpy

# TAKE A STILL IMAGE WITH WEB CAMERA

def take_still(cam_ix, view_scale, safe_margin, file_name, save_scale):
    """Takes a still image with web camera and saves it as jpg. 
    Capture window has a safe area rectangle to give propper margins for the final image.
    Lines of thirds are present in the preview window. Center point of safe area is also
    marked with a circle.

    Args:
        cam_ix (int): Index of the web camera, 1st camera is 0
        view_scale (float): Factor for scaling the capture window 0,5 half size, 2 double size
        safe_margin (int): Safety margin in pixels from the edge of the picture to the safe area rectangle 
        file_name (string): name of the output file
        save_scale (float): Factor for scaling the the final image 0,5 half size, 2 double size

    Returns:
        dict: Satus and picture dimensions
    """
    # Creating a VideoCapture object for the wideo stream from the Web camera
    video_stream = cv2.VideoCapture(cam_ix)

    # Loop until iterrupted by keystroke s -> save
    while (video_stream.isOpened()):

        # Capture the stream frame by frame, read() fuction returns true if reading is successfull and a wideo frame
        ret, frame = video_stream.read()

        # Check if capture is successfull
        if ret == True:

            # Find out frame dimensions and number of channels (for proportional resizing)
            orig_height, orig_width, channels = frame.shape

            # Dimensions for the video window and the still image
            picture_width = int(round(orig_width * view_scale, 0))
            picture_height = int(round(orig_height * view_scale, 0))

            # Resize the frame for preview using bicubic interpolation
            frame = cv2.resize(frame, (picture_width, picture_height),
                               fx=0, fy=0, interpolation=cv2.INTER_CUBIC)

            # Draw a red safe area rectangle into the frame (BGR colour space, line width 4 px)
            top_left = (safe_margin, safe_margin)
            bottom_right = (picture_width - safe_margin,
                            picture_height - safe_margin)
            cv2.rectangle(frame, top_left, bottom_right, (0, 0, 255), 4)

            # Draw a center circle into the frame (radius 40 px, line width 1 px)
            center_x = int(round(picture_width / 2 ,0))
            center_y = int(round(picture_height / 2 ,0))
            cv2.circle(frame, (center_x, center_y), 40, (0, 0, 255), 1)

            # Define dividing lines for thirds to help positioning objects into safe area

            # Calculate starting and ending coordinates for vertical lines
            safe_area_width = int(round(picture_width - safe_margin * 2 , 0))
            safe_area_height = int(round(picture_height - safe_margin * 2, 0))

            v_line_1_top_x = int(round(safe_margin + safe_area_width / 3, 0))
            v_line_1_top_y = safe_margin
            v_line_1_bottom_x = int(round(safe_margin + safe_area_width / 3, 0)) 
            v_line_1_bottom_y = picture_height - safe_margin

            v_line_2_top_x = int(round(safe_margin + safe_area_width / 3 * 2 , 0 ))
            v_line_2_top_y = safe_margin
            v_line_2_bottom_x = int(round(safe_margin + safe_area_width / 3 * 2,  0))
            v_line_2_bottom_y = picture_height - safe_margin

            # Create end points for vertical lines
            v_line_1_top = (v_line_1_top_x, v_line_1_top_y)
            v_line_1_bottom = (v_line_1_bottom_x, v_line_1_bottom_y)

            v_line_2_top = (v_line_2_top_x, v_line_2_top_y)
            v_line_2_bottom = (v_line_2_bottom_x, v_line_2_bottom_y)

            # Calculate starting and ending coordinates for horizontal lines
            h_line_1_left_x = safe_margin
            h_line_1_left_y = int(round(safe_margin + safe_area_height / 3, 0))
            h_line_1_right_x = safe_margin + safe_area_width
            h_line_1_right_y = int(round(safe_margin + safe_area_height / 3, 0))

            h_line_2_left_x = safe_margin
            h_line_2_left_y = int(round(safe_margin + safe_area_height / 3 * 2, 0))
            h_line_2_right_x = safe_margin + safe_area_width
            h_line_2_right_y = int(round(safe_margin + safe_area_height / 3 * 2, 0))

            # Create end points for horizontal lines
            h_line_1_left = (h_line_1_left_x, h_line_1_left_y)
            h_line_1_right = (h_line_1_right_x, h_line_1_right_y)

            h_line_2_left = (h_line_2_left_x, h_line_2_left_y)
            h_line_2_right = (h_line_2_right_x, h_line_2_right_y)

            # Draw lines (1 pix red)
            cv2.line(frame, v_line_1_top, v_line_1_bottom, (0, 0, 255), 1)
            cv2.line(frame, v_line_2_top, v_line_2_bottom, (0, 0, 255), 1)
            cv2.line(frame, h_line_1_left, h_line_1_right, (0, 0, 255), 1)
            cv2.line(frame, h_line_2_left, h_line_2_right, (0, 0, 255), 1)

            # Display the video frame in a window named Video stream
            cv2.imshow('Video stream with safe area', frame)

        # Define a key stroke s as the save and exit from video streaming, wait 25 ms for key storke
        if cv2.waitKey(25) & 0xFF == ord('s'):
            break

    # Save the last captured frame as jpg image (without rectangle)
    ret, frame = video_stream.read()
    if ret == True:

        # Dimensions for the the still image
        final_width = int(round(orig_width * save_scale, 0))
        final_height = int(round(orig_height * save_scale, 0))

        # Resize the frame for final image using bicubic interpolation
        frame = cv2.resize(frame, (final_width, final_height),
                           fx=0, fy=0, interpolation=cv2.INTER_CUBIC)

        # Save the final image
        cv2.imwrite(file_name, frame)

    # Release the video capture object
    video_stream.release()

    # Read the still image and show it in a new window
    still_image = cv2.imread(file_name)
    cv2.imshow('Still image', still_image)

    # Wait for key stroke q to close all open video and picture windows
    while True:
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # Closes all the windows currently opened.
    cv2.destroyAllWindows()

    # Return image information
    capture_info = {'original width': orig_width, 'original height': orig_height, 'final width': final_width,
                    'final height': final_height, 'channels': channels}
    return capture_info

# Quick test inside the module
if __name__ == '__main__':

    # Otetaan kuva kameralla 2 (indeksi 1), 2 x suurennos 50 px suoja-alue ja lopullinen koko 2 x
    picture_info = take_still(1, 2, 50, 'testi.jpg', 2)
    print(picture_info)

