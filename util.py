"""
Voodoo win32gui magic here, wrote this code 3 years ago, no idea what goes on here
"""
import string
import win32gui
from controls.util import delay 


def contains_only_letters_from_collection(word, collection):
    return len([char for char in word if char not in collection]) == 0


def filter_ascii_windows(windows):
    return [window for window in windows if not contains_only_letters_from_collection(window, string.ascii_letters)]


def get_all_windows():
    def callback(hwnd, strings):
        if win32gui.IsWindowVisible(hwnd):
            window_title = win32gui.GetWindowText(hwnd)
            left, top, right, bottom = win32gui.GetWindowRect(hwnd)
            if window_title and right-left and bottom-top:
                strings.append(window_title)
        return True

    windows = list()
    win32gui.EnumWindows(callback, windows)    
    windows = filter_ascii_windows(windows) # filter ascii only windows
    return windows


@delay(time=0.3)
def bring_up_window(window_title):
    # search window
    window = win32gui.FindWindow(None, window_title)

    # show window ?
    win32gui.ShowWindow(window, 5)

    # put in infront
    win32gui.SetForegroundWindow(window)

    # return window dimensions
