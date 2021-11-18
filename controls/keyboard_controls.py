"""
Wraps keyboard module with common functionality needed for Path of Exile scripts (i.e: hold, click multiple keys at once)
"""
import time
import keyboard
from contextlib import contextmanager


@contextmanager
def hold(key):
    keyboard.press(key)
    try:
        yield
    finally:
        keyboard.release(key)


def press_and_release(key):
    keyboard.press_and_release(key)


def combo(*keys):
    for key in keys:
        keyboard.press(key)

    time.sleep(0.3)

    for key in keys[::-1]:
        keyboard.release(key)