from macro import check_item, click, move_mouse_quad, move_mouse_inv, mouse, keyboard
import time
# 332, 777 seek prophecy
# 511, 450 seal prophecy
# 567, 418 stash
# 232, 143 dump2

def fill_inventory():
    for i in range(5):
        for j in range(12):
            mouse.position = (511, 450)
            click()
            keyboard.press_and_release('enter')
            move_mouse_inv(i, j)
            click()
            mouse.position = (332, 777)
            click()

def dump_inventory():
    keyboard.press_and_release('esc')
    mouse.position = (898, 429)
    click()
    mouse.position = (232, 143)
    click()
    keyboard.press('ctrl')
    for i in range(5):
        for j in range(12):
            move_mouse_inv(i, j)
            click()

    keyboard.release('ctrl')

    mouse.position = (1078, 391)
    click()
    mouse.position = (614, 267)
    click()

    keyboard.press_and_release('i')


