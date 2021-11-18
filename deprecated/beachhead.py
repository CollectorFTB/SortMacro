import spreadsheet as ss
from macro import check_item, move_mouse_inv


def scan():
    inventory = dict()
    for j in range(12):
        for i in range(5):
            move_mouse_inv(i, j)
            item, stack_size = check_item(2)
            if item:
                try:
                    inventory[item] += stack_size
                except:
                    inventory[item] = stack_size
            else:
                return inventory
    return inventory


def update_spreadsheet(inventory, spreadsheet_name):
    spreadsheet = ss.get_spreadsheet('PoE shit')
    spreadsheet = spreadsheet.worksheet(spreadsheet_name)
    for i in range(10, 41):
        row = spreadsheet.row_values(i)
        for item in inventory.keys():
            if item in row:
                index = row.index(item) + 2 # weird ass google spreadsheets indexing
                value = int(spreadsheet.cell(i, index).value) # grab old value at that index
                spreadsheet.update_cell(i, index, inventory[item] + value) # update that cell


# def throw_inventory_on_spreadsheet():
#     inventory = beachhead.scan()
#     if inventory:
#         beachhead.update_spreadsheet(inventory, 'Beachhead-M')
