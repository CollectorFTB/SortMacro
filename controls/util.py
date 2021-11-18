"""
Basic utility needed for handling inputs (keyboard and mouse)
"""
import time
from functools import wraps

def delay(func):
    @wraps
    def wrapper(time):
        time.sleep(time)
    return wrapper
