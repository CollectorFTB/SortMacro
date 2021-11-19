"""
Basic utility needed for handling inputs (keyboard and mouse)
"""
import time
from functools import wraps

def delay(t):
    def fac(func):
        @wraps(delay)
        def wrapper(*args, **kwargs):
            time.sleep(t)
            ret = func(*args, **kwargs)
            time.sleep(t)
            return ret
        return wrapper
    return fac