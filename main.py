from time import sleep

import beachhead
import macro
import sort
from util import bring_up_window


def sort_stash():
    sort.sort2(6)

def throw_inventory_on_spreadsheet():
    inventory = beachhead.scan()
    if inventory:
        beachhead.update_spreadsheet(inventory, 'Beachhead-M')


def main()
    bring_up_window('Path of Exile')
    sleep(0.3)
    throw_inventory_on_spreadsheet()    

if __name__ == "__main__":
    main()
