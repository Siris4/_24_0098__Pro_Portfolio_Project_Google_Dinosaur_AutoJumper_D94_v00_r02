import pyautogui
import time
from PIL import ImageGrab, ImageOps
import numpy as np

# Detection box coordinates for the obstacle region (based on the orange box)
dino_region = (435, 524, 874, 824)  # Top-left: (435, 524), Bottom-right: (874, 824)

# The target color to detect (medium-dark gray)
target_color = (83, 83, 83)

# Function to capture the game screen and return the pixel values of the region
def capture_screen(region):
    image = ImageGrab.grab(bbox=region)
    return image

# Function to detect the target color in the screen region
def detect_color(image, color):
    # Get the pixel data from the image
    pixels = np.array(image)

    # Check if any pixel in the image matches the target color (ignoring alpha channel if present)
    for row in pixels:
        for pixel in row:
            if tuple(pixel[:3]) == color:  # Compare only RGB, ignore alpha if any
                return True
    return False

# Function to handle jumping based on color detection
def start_jumping():
    time.sleep(5)  # Wait 5 seconds to allow the user to switch to the game window

    while True:
        # Capture the current state of the screen region
        screen_image = capture_screen(dino_region)

        # Check if the target color is detected in the image
        if detect_color(screen_image, target_color):
            pyautogui.press('space')  # Jump if the target color is detected
            time.sleep(0.1)  # Prevent multiple jumps by pausing briefly

        # Small delay to match the screen refresh rate and not overwhelm the CPU
        time.sleep(0.05)

# Start the function
start_jumping()
