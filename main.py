from time import sleep

from util import bring_up_window
import prophecy


def farm_prophecies(n=10):
    for i in range(n):
        talk_to_navali()
        prophecy.seek_inventory()

        click_stash_tab()
        prophecy.dump_inventory()
    
from controls.mouse_controls import mouse

def debug_print():
    from threading import Thread
    
    def debug_cursor():
        while True:
            from time import sleep
            position = mouse.position
            print(f'Current : ({position[0]},{position[1]})')
            sleep(0.5)
    
    Thread(target=debug_cursor).start()
    

def main():
    bring_up_window('Path of Exile')
    debug_print()    

if __name__ == "__main__":
    main()
