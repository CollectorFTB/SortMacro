from time import sleep

import beachhead
import macro
import sort
from util import bring_up_window
import prophecy

def sort_stash():
    sort.sort2(18)

def throw_inventory_on_spreadsheet():
    inventory = beachhead.scan()
    if inventory:
        beachhead.update_spreadsheet(inventory, 'Beachhead-M')

def farm_prophecies(n=10):
    for i in range(n):
        prophecy.fill_inventory()
        prophecy.dump_inventory()
    
    


def main():
    bring_up_window('Path of Exile')
    sleep(0.3)
    farm_prophecies()    

if __name__ == "__main__":
    main()
