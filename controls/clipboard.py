"""
Lets you easily access clipboard data without dealing with pesky libraries
"""
import win32clipboard as cb 
from contextlib import contextmanager

# TODO: Implement class to wrap this clipboard logic to encapsulate the module being static

@contextmanager
def clipboard():
    cb.OpenClipboard()
    try:
        yield 
    finally:
        cb.CloseClipboard()


def get_clipboard_data():
    with clipboard():
        try:
            return cb.GetClipboardData()
        except: # ????
            return ''
        finally:
            cb.EmptyClipboard()