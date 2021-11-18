from collections import OrderedDict

from macro import check_item, click, move_mouse_quad


def swap(pos1, pos2):
    
    move_mouse_quad(*pos1)
    click()
    move_mouse_quad(*pos2)
    click()
    move_mouse_quad(*pos1)
    click()

def sort2(n):
    stash = OrderedDict()
    for j in range(n):
        for i in range(24):
            move_mouse_quad(i, j)
            item, _ = check_item(1)
            if item:
                try:
                    stash[item].append((i,j))
                except:
                    stash[item] = [(i,j)]

    i, j = 0, 0

    for key in stash.keys():
        for k in range(len(stash[key])):
            if (i, j) in stash[key]:
                pass
            else:
                for v in stash.values():
                    if (i, j) in v:
                        to_add = (i, j)
                        to_remove = sorted(stash[key], key= lambda x: x[0]+x[1]*24)[k]
                        key_index = tuple(stash.values()).index(v)
                        other_key = tuple(stash.keys())[key_index]
                        stash[other_key].remove(to_add)
                        stash[other_key].append(to_remove)
                        stash[key].remove(to_remove)
                        stash[key].append(to_add)
                        swap(to_add, to_remove) # lol this works
                        break
            j = j+1 if (i+1)%24 == 0 else j
            i = (i+1)%24                  
