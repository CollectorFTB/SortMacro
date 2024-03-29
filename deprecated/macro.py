import time

from clipboard import *

import controls.keyboard_controls as kb

def check_item(parse_mode):
    kb.combo('ctrl', 'c')
    
    if not (raw_data := get_clipboard_data()):
        return None, None  

    raw_data = raw_data.split('\r\n')
    stack_size = 1
    try:
        temp = raw_data[raw_data.index('--------')+1:][0]
        raw_data = raw_data[:raw_data.index('--------')]
        stack_size = int(temp.split(' ')[-1].split('/')[0])
        map_tier = int(temp.split(' ')[2])
    except:
        pass

    re = raw_data[-1]
    temp = re.split(' ')
    if parse_mode == 1:
        if 'Map' in temp:
            if 1 <= map_tier <=5:
                re = 'White Maps'
            elif 6 <= map_tier <=10:
                re = 'Yellow Maps'
            elif 11 <= map_tier <=16:
                re = 'Red Maps'    
            else:
                re = 'Map'
        elif 'Essence' in temp or "Remnant" in temp:
            re = 'Essence'
        elif 'Jewel' in temp:
            re = 'Jewel'
        elif 'Splinter' in temp:
            re = 'Splinter'
        elif 'Sextant' in temp:
            re = 'Sextant'
        elif 'Ring' in temp:
            re = 'Ring'
        elif 'Card' in raw_data[0].split(' '):
            re = 'Div'
        elif 'Gem' in raw_data[0].split(' '):
            re = 'Gem'
    if parse_mode == 2:
        if 'Map' in temp:
            if 1 <= map_tier <=5:
                re = 'White Maps'
            elif 6 <= map_tier <=10:
                re = 'Yellow Maps'
            elif 11 <= map_tier <=16:
                re = 'T' + str(map_tier)
            else:
                re = 'Map'
            stack_size = 1
        elif 'Card' in raw_data[0].split(' '):
            re = raw_data[1]
        elif 'Divine' in raw_data[0].split(' '):
            re = 'Divine Vessel'
            stack_size = 0.5
        elif 'Ring' in re:
            re = 'Rings'
            stack_size = 1

    return re, stack_size
