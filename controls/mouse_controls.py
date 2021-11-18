"""
For anything that has to do with mouse, just a wrapper
"""
from pynput.mouse import Button, Controller

from util import delay

mouse = Controller()

def _click(mb=Button.left):
    mouse.click(mb)
    mouse.release(mb)

@delay(time=0.3)
def click(pos=None, mb=Button.left):
    if pos:
        mouse.position = pos

    _click(mb)

