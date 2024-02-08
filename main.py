import pyautogui
from pynput import keyboard
import keyboard
import time
import pytesseract
import pygame
import cv2
import numpy as np
import re


'''

check if full screen

close chat

check_item(item):
    type in search bar
    wait for name to appear
    click item
    int(first_price), int(second_price)
    if first_price / second_price <= 0.8:
        Notfie()
    
    



'''
# Variables
items = ["chapeau de la sain ballotin"]


# CONSTANTS
search_bar = (230, 197)
first_item_found = (85, 379, 323, 27)
first_price_reg = (852, 402, 139, 26)
second_price_reg = (855, 476, 134, 26)
item_found_reg = (41, 366, 81, 50)

# ASSETS



def search(item):
    pyautogui.click(search_bar, clicks=2, interval=.5)
    time.sleep(.5)
    keyboard.write(item, delay=.1)
    keyboard.press_and_release('enter')


def wait_item():
    item_found = ocr_this(item_found_reg)
    while not item_found:
        print("item NOT FOUND")     #test
        item_found = ocr_this(item_found_reg)
    print("Item Found")     #test
    return True

    
def open_item():
    item_found = wait_item()
    if item_found:
        time.sleep(.4)
        pyautogui.click(first_item_found)

        
def preprocess_image(image):
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Invert colors
    inverted = cv2.bitwise_not(gray)
    
    # Apply adaptive thresholding
    threshold = cv2.adaptiveThreshold(inverted, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    
    return threshold

def ocr_this(reg):
    # Capture screenshot
    roi = pyautogui.screenshot(region=reg)
    
    # Convert screenshot to OpenCV format
    image = np.array(roi)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    
    # Preprocess image
    preprocessed_image = preprocess_image(image)
    
    # Perform OCR on preprocessed image
    custom_config = r'--oem 3 --psm 4'
    text = pytesseract.image_to_string(preprocessed_image, config=custom_config)

    text = re.sub(r'[\s.]', '', text)
    return text
        


def compare_first_seconde():
    time.sleep(.5)
    try:
        first_price = ocr_this(first_price_reg)
        second_price = ocr_this(second_price_reg)
        first_price = int(first_price)
        second_price = int(second_price)
    except:
        print("MA BGHACH HADCHI I WLI INT, SBAR")
        time.sleep(1)
        try: 
            first_price = ocr_this(first_price_reg)
            second_price = ocr_this(second_price_reg)
            first_price = int(first_price)
            second_price = int(second_price)
        except:
            print("SIR T9AWED")

    taux = first_price / second_price
    if taux <= 1:
        notif_sound()

def notif_sound():
    pygame.mixer.init()
    wav = "assets/mixkit-confirmation-tone-2867.wav"
    sound = pygame.mixer.Sound(wav)
    sound.play()
    while pygame.mixer.get_busy():
        pygame.time.wait(100)
    


    

    
    







if __name__ == "__main__":
    search(items[0])
    wait_item()
    open_item()
    compare_first_seconde()
    
    pass


