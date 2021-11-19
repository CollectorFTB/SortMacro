"""
Responsible for interacting with the prophecy window to seek and seal prophecies
"""
import time

import inventory 
import controls.keyboard_controls as kb
import controls.mouse_controls as mouse
import controls.clipboard as clip
SEAL = (639, 381)
SEEK = (443, 1033)


STASH = (1193, 544)
CLOSE_STASH = (836, 93)
NAVALI = (900, 469)
VIEW = (821, 382)
DESTROY = (1037, 849+200)


def seek_inventory():
    for inventory_position in inventory.Inventory():
        while True:
            mouse.click(SEEK)
            mouse.click(SEAL)
            kb.press_and_release('enter')
            mouse.click(inventory_position)

            kb.combo('ctrl', 'c')
            data = clip.get_clipboard_data()
            if check_bad_prophecy(data):
                delete_prophecy()
            else:
                break

def dump_inventory():
    mouse.click(STASH)

    with kb.hold('ctrl'):   
        for inventory_position in inventory.Inventory():
            mouse.click(inventory_position)

    mouse.click(CLOSE_STASH)

def talk_to_navali():
    mouse.click(NAVALI)
    mouse.click(VIEW)

def check_bad_prophecy(item_desc):
    item_desc = item_desc.lower()
    bad_prophecies = ['Erased from Memory',
                      'Waiting In Ambush',
                      'The Undead Brutes',
                      'The Corrupt',
                      'The Cursed Choir',
                      'The Mysterious Gift',
                      'A Regal Death',
                      'The Singular Spirit',
                      'The Alchemist',
                      'The Apex Predator',
                      'Smothering Tendrils',
                      'Golden Touch',
                      'Fire and Ice',
                      'A vision of ice and fire',
                      'Gilded Within',
                      'Ancient Doom',
                      'Gilded Within',
                      'The God Of Misfortune',
                      'The Dreamer\'s Dream',
                      'The Dream Trial',
                      'The Queen\'s Vaults',
                      'The Snuffed Flame',
                      'Risen Blood',
                      'Nemesis Of Greed',
                      'Thaumaturgical History I',
                      'Day of Sacrifice I',
                      'The Beginning and the End',
                      'The Invader',
                      'The Hardened Armour',
                      'The Sharpened Blade',
                      'Hidden Vaal Pathways',
                      'The Warmongers I',
                      'The Mysterious Gift',
                      'Forceful Exorcism',
                      'Beyond Sight I',
                      'The Fortune Teller\'s Collection',
                      'Soil, Worms and Blood',
                      'A Valuable Combination',
                      'A Forest of False Idols',
                      'The Wealthy Exile',
                      'Ending the Torment',
                      'The Ambitious Bandit I',
                      'An Unseen Peril',
                      'The Brothers of Necromancy',
                      'Mysterious Invaders',
                      'Possessed Foe',
                      'The Four Feral Exiles',
                      'The Scout',
                      'Notched Flesh',
                      'The Bloody Flowers Redux',
                      'The Brutal Enforcer',
                      'The Trembling Earth',
                      'A Firm Foothold',
                      'The Bishop\'s Legacy',
                      'Rebirth',
                      'Anarchy\'s End I',
                      'Deadly Rivalry I',
                      'Kalandra\'s Craft',
                      'A Whispered Prayer',
                      'Sun\'s Punishment',
                      'The Walking Mountain',
                      'The Last Watch',
                      'Winter\'s Mournful Melodies',
                      ]
    return any(p.lower() in item_desc for p in bad_prophecies)

def filter_prophecies():
    time.sleep(1)
    for inventory_position in inventory.Inventory():
        mouse.move(inventory_position)
        kb.combo('ctrl', 'c')
        data = clip.get_clipboard_data()
        if check_bad_prophecy(data):
            delete_prophecy()

def delete_prophecy():
    mouse.click()
    mouse.click(DESTROY)
    kb.press_and_release('enter')
