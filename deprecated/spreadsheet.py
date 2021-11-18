import datetime
import pprint
import random

import gspread
from oauth2client.service_account import ServiceAccountCredentials


def get_spreadsheet(name):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('secret.json', scope)  
    client = gspread.authorize(creds)
    s = client.open(name)
    return client.open(name)

def print_rows(sheet, start, stop):
    for i in range(start, stop): 
        print(sheet.row_values(i))


def delete_rows(sheet, start, stop):
    for i in range(start, stop):
        sheet.delete_row(i)

def copy_paste_request(sheet, old_row_start, old_row_end, old_col_start, old_col_end, new_row, new_col):
    request = {
      "cutPaste": {
        "source": {
          "sheetId": sheet.id,
          "startRowIndex": old_row_start,
          "endRowIndex": old_row_end,
          "startColumnIndex": old_col_start,
          "endColumnIndex": old_col_end
        },
        "destination": {
          "sheetId": sheet.id,
          "rowIndex": new_row,
          "columnIndex": new_col    
        },
        "pasteType": "PASTE_NORMAL"
      }
    }
    return request

def color_request(sheet, color, row, col):
    request = {
                "repeatCell": {
                    "range": {
                    "sheetId": sheet.id,
                    "startRowIndex": row-1,
                    "endRowIndex": row,
                    "startColumnIndex": col-1,
                    "endColumnIndex": col
                    },
                    "cell": {
                    "userEnteredFormat": {
                        "backgroundColor": {
                        "red": color[0],
                        "green": color[1],
                        "blue": color[2]
                        }
                    }
                    },
                    "fields": "userEnteredFormat(backgroundColor)"
                }
            }
    return request

def random_colors_grid(ss, sheet):
    requests = []

    for i in range(0, 8):
        for j in range(0, 6):
            color = random.random(), random.random(), random.random()
            sheet.update_cell(i+1, j+1, ",".join([format(c, '.3f') for c in color]))
            requests.append(color_request(sheet, color, i, j))
    
    body = {'requests': requests}
    ss.batch_update(body)


def change_colors(ss, sheet):
    requests = []

    for i in range(3, 52):
        data = sheet.row_values(i)
        for name in data:
            for cl in c_dict:
                if name.lower() in c_dict[cl]:
                    requests.append(color_request(sheet, class_colors[cl], i-1, data.index(name)))
        

    ss.batch_update({'requests': requests})


def test():
    ss = get_spreadsheet('PoE shit')
    sheet = ss.worksheet('Beachhead')    


if __name__== '__main__':
    test()
     