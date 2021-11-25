"""
Responsible for interacting with the prophecy window to seek and seal prophecies
"""
import time
import json
import inventory 
import controls.keyboard_controls as kb
import controls.mouse_controls as mouse
import controls.clipboard as clip

from collections import defaultdict
from pprint import pprint as pp

SEAL = (639, 381)
SEEK = (443, 1033)


STASH = (1193, 544)
CLOSE_STASH = (836, 93)
NAVALI = (900, 469)
VIEW = (821, 382)
DESTROY = (1037, 849+200)

BAD_PROPHECIES = ['Erased from Memory',
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
                      'The Sinner\'s Stone',
                      'The hungering swarm',
                      'Blinding Light',
                      'The Vanguard',
                      'Mouth of Horrors',
                      'Crimson Hues',
                      'Reforged Bonds',
                      'Fire and Brimstone',
                      'The Dreaded Rhoa',
                      'The Flow of Energy',
                      'End of the Light',
                      'Dance of Steel',
                      'Severed Limbs',
                      'A Rift in time',
                      'The King and the Brambles',
                      'From the void',
                      'The Beautiful Guide',
                      'Heavy Blows',
                      'Burning Dread',
                      'Flesh of the beast',
                      'Black Devotion',
                      'The Malevolent Witch',
                      'The storm spire',
                      'Blind Faith',
                      'The Silverwood',
                      'Dark Instincts',
                      'Custodians of Silence',
                      'The Misunderstood queen',
                      'Blood in the Eyes',
                      'Greed\'s Folly',
                      'The Great leader of the north',
                      'Dying Cry',
                      'The nightmare awakens',
                      'Graceful flames',
                      'Overflowing Riches',
                      'Strong as a bull',
                      'Trapped in the tower',
                      'The soulless beast',
                      'The fall of an empire',
                      'Nature\'s Resilience',
                      'The Watcher\'s Watcher',
                      'Pleasure and pain',
                      'Weeping Death',
                      'Heart of the fire',
                      'Power Magnified',
                      'Cold blooded fury',
                      'Blood of the betrayed',
                      'Lost in the pages',
                      'Cold Greed',
                      'The Flayed man',
                      'Faith Exhumed',
                      'The karui Rebellion',
                      'The nest'
                      ]


def seek_inventory():
    try:
        d = defaultdict(int)
        d.update(json.load(open('data.json', 'r')))

        for inventory_position in inventory.Inventory():
            while True:
                mouse.click(SEEK)
                mouse.click(SEAL)
                kb.press_and_release('enter')
                mouse.click(inventory_position)
                
                time.sleep(0.1)
                kb.combo('ctrl', 'c')
                data = clip.get_clipboard_data()


                try:
                    d[data.split('\r\n')[2]] += 1
                except:
                    print('FUCK')

                if check_bad_prophecy(data):
                    delete_prophecy()
                else:
                    break
    finally:    
        d = {k:v for k,v in d.items() if k.lower() not in [l.lower() for l in BAD_PROPHECIES]}
        json.dump(d, open('data.json', 'w'))


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

    return any(p.lower() in item_desc for p in BAD_PROPHECIES)

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
