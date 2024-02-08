import pyautogui
from pynput import keyboard
import keyboard
import time
import pytesseract


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
items = ["solomonk"]


# CONSTANTS
search_bar = (230, 197)
first_item_found = (85, 379, 323, 27)
first_price_reg = (820, 388, 200, 48)
second_price_reg = (819, 465, 203, 50)
item_found_reg = (41, 366, 81, 50)

# ASSETS



def search(item):
    pyautogui.click(search_bar, clicks=2, interval=.5)
    time.sleep(.3)
    keyboard.write(item)
    keyboard.press_and_release('enter')


def wait_item():
    no_item_path = "assets/o_item.PNG"
    no_item = pyautogui.locateOnScreen(no_item_path, region=item_found_reg)
    while no_item:
        no_item = pyautogui.locateOnScreen(no_item_path, region=item_found_reg)
        print("Item Not Found")
    return True
    
def open_item():
    item_found = wait_item()
    if item_found:
        time.sleep(.1)
        pyautogui.click(first_item_found)

def ocr_this(reg):
    roi = pyautogui.screenshot(region=reg)
    custom_config = r'--oem 3 --psm 3'
    text = pytesseract.image_to_string(roi, config=custom_config)
    # print(text)
    return text







if __name__ == "__main__":
    # ocr_this(first_item_found)
    pass


