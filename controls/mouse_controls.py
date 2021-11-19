"""
For anything that has to do with mouse, just a wrapper
"""
from pynput.mouse import Button, Controller

from util import delay
from time import sleep
mouse = Controller()

def _click(mb=Button.left):
    mouse.click(mb)
    mouse.release(mb)

@delay(0.4)
def click(pos=None, mb=Button.left): 
    if pos:
        move(pos)
    _click(mb)

@delay(0.1)
def move(pos):
    x,y = pos
    mouse.position = pos
    mouse.position = x+5, y-5
    mouse.position = pos
