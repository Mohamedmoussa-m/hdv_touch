import pyautogui
from pynput import keyboard
import keyboard
import time


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



# VARIABLES
search_bar = (230, 197)
first_item_found = (186, 394)
first_price_reg = (820, 388, 200, 48)
second_price_reg = (819, 465, 203, 50)
item_found_reg = (41, 366, 81, 50)

# ASSETS
no_item = r'C:\Users\moise\Documents\GitHub\bot_touch\bot_hdv\assets\no_item.PNG'


def search(item):
    pyautogui.click(search_bar, clicks=2, interval=.1)
    time.sleep(.3)
    keyboard.write(item)
    keyboard.press_and_release('enter')


def wait_item():
    no_item = pyautogui.locateOnScreen(no_item, region=item_found_reg)
    while no_item:
        no_item = pyautogui.locateOnScreen(no_item, region=item_found_reg)
        print("Item Not Found")
    return True
    

