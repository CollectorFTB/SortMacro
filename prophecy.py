"""
Responsible for interacting with the prophecy window to seek and seal prophecies
"""
import time

import inventory 
import keyboard_controls as kb
import mouse_controls as mouse

SEAL = (511, 450)
SEEK = (332, 777)

def seek_inventory():
    for inventory_position in inventory.Inventory():
        mouse.click(SEAL)
        kb.press_and_release('enter')
        mouse.click(inventory_position)
        mouse.click(SEEK)

def dump_inventory():
    with kb.hold('ctrl'):
        for inventory_position in inventory.Inventory():
            # TODO: Check if need to destory?
            mouse.click(inventory_position)


