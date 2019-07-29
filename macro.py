from time import sleep

import keyboard
from pynput.mouse import Button, Controller

import win32clipboard as clipboard
from util import bring_up_window

mouse = Controller()

def click(mb=Button.left):
    sleep(0.3)
    mouse.click(mb)
    mouse.release(mb)
    sleep(0.3)

def check_item(parse_mode):
    clipboard.OpenClipboard()
    clipboard.EmptyClipboard()
    clipboard.CloseClipboard()  

    keyboard.press('ctrl')
    keyboard.press('c')
    keyboard.release('ctrl')
    keyboard.release('c')
    sleep(0.2)
    
    clipboard.OpenClipboard()
    try:
        raw_data = clipboard.GetClipboardData()
    except:
        return None, None
    clipboard.CloseClipboard()

    raw_data = raw_data.split('\r\n')
    stack_size = 1
    try:
        temp = raw_data[raw_data.index('--------')+1:][0]
        raw_data = raw_data[:raw_data.index('--------')]
        stack_size = int(temp.split(' ')[-1].split('/')[0])
        map_tier = int(temp.split(' ')[2])
    except:
        pass

    re = raw_data[-1]
    temp = re.split(' ')
    if parse_mode == 1:
        if 'Map' in temp:
            if 1 <= map_tier <=5:
                re = 'White Maps'
            elif 6 <= map_tier <=10:
                re = 'Yellow Maps'
            elif 11 <= map_tier <=16:
                re = 'Red Maps'    
            else:
                re = 'Map'
        elif 'Essence' in temp or "Remnant" in temp:
            re = 'Essence'
        elif 'Jewel' in temp:
            re = 'Jewel'
        elif 'Splinter' in temp:
            re = 'Splinter'
        elif 'Sextant' in temp:
            re = 'Sextant'
        elif 'Ring' in temp:
            re = 'Ring'
        elif 'Card' in raw_data[0].split(' '):
            re = 'Div'
        elif 'Gem' in raw_data[0].split(' '):
            re = 'Gem'
    if parse_mode == 2:
        if 'Map' in temp:
            if 1 <= map_tier <=5:
                re = 'White Maps'
            elif 6 <= map_tier <=10:
                re = 'Yellow Maps'
            elif 11 <= map_tier <=16:
                re = 'T' + str(map_tier)
            else:
                re = 'Map'
            stack_size = 1
        elif 'Card' in raw_data[0].split(' '):
            re = raw_data[1]
        elif 'Divine' in raw_data[0].split(' '):
            re = 'Divine Vessel'
            stack_size = 0.5
        elif 'Ring' in re:
            re = 'Rings'
            stack_size = 1

    return re, stack_size



        
def move_mouse_quad(row, col): # stash tab row,col translated to mouse x,y
    step = 26.66
    start = (24, 172)
    mouse.position = (start[0] + int(col * step), start[1] + int(row * step))
    sleep(0.1)

def move_mouse_inv(row, col):
    step = 26.66*2
    start = (1295, 615)
    mouse.position = (start[0] + int(col * step), start[1] + int(row * step))
    sleep(0.1)


def mouse_coords():
    print(mouse.position)
