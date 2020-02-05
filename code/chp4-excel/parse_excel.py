"""
    This is a script to parse child labor and child marriage data.
    The excel file used in this script can be found here:
        http://www.unicef.org/sowc2014/numbers/
"""

import xlrd
book = xlrd.open_workbook("../../data/chp4/SOWC 2014 Stat Tables_Table 9.xlsx")
'''for sheet in book.sheets():
 print (sheet.name)
 '''
sheet = book.sheet_by_name("Table 9 ")
#print(sheet.nrows)
data = {}
for i in range(14, sheet.nrows):

    # Start at 14th row, because that is where the countries begin
    row = sheet.row_values(i)
    #print(row)
    country = row[1]
    #print(row[4])
    data[country] = {
        'child_labor': {
            'total': [row[4], row[5]],
            'male': [row[6], row[7]],
            'female': [row[8], row[9]],
        },
        'child_marriage': {
            'married_by_15': [row[10], row[11]],
            'married_by_18': [row[12], row[13]],
        }
    }

    if country == "Zimbabwe":
        break

import pprint
#pprint.pprint(data)
