import xlsxwriter
import xlrd
import urllib.request
# from record import *
from movement import *




base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sheets_dir = base_dir+r"/sheets/"


replay()




f = open(base_dir + r'/urls.txt')
urls =[]
for s in f:
    print(s)
    urls.append(s)


for i in range(len(urls)):

    urllib.request.urlretrieve(urls[i], sheets_dir +r'/file{}.xlsx'.format(i+1))



col_one = 7 #COL H
col_two = col_three = 4 # COL E
col_four = 3 #COL D
#these are 0 indexed

sheets = os.listdir(sheets_dir)

#assigning variables to the correct documents
one = two = three = four = ''
for item in sheets:

    if item[-6] == '1':
        one = item
    if item[-6] == '2':
        two = item
    if item[-6] == '3':
        three = item
    if item[-6] == '4':
        four = item

data = []

sheet1 = xlrd.open_workbook(sheets_dir + one).sheet_by_index(0)
data1 = sheet1.col_values(col_one)
data1_fin = [data1[7]]
data1 = data1[8:]
data1 = list(set(data1))
data1.sort()

data1_fin = data1_fin + data1
data.append(data1_fin)
print(data1_fin)

sheet2 = xlrd.open_workbook(sheets_dir + two).sheet_by_index(0)
data2 = sheet2.col_values(col_two)
data.append(data2)
print(data2)

sheet3 = xlrd.open_workbook(sheets_dir + three).sheet_by_index(0)
data3 = sheet3.col_values(col_three)
data.append(data3)
print(data3)

sheet4 = xlrd.open_workbook(sheets_dir + four).sheet_by_index(0)
data4 = sheet4.col_values(col_four)
data.append(data4[2:])
print(data4)

workbook = xlsxwriter.Workbook(base_dir + r'/outputSheet/output.xlsx')
worksheet = workbook.add_worksheet()

row = 0
col = 0
for doc in data:
    row = 0
    for item in doc:
        item = str(item)
        item = item.replace(', ', ',')
        worksheet.write(row,col,item)
        row += 1
    col += 1
worksheet.set_column(0,8,20)

row = 0

for i in range(2,len(data1)):

    worksheet.write_formula('E{}'.format(i), '=VLOOKUP(A{},B2:B{},1,FALSE)'.format(i,len(data2)))
    worksheet.write_formula('F{}'.format(i), '=VLOOKUP(A{},C2:C{},1,FALSE)'.format(i,len(data3)))
    worksheet.write_formula('G{}'.format(i), '=VLOOKUP(A{},D2:D{},1,FALSE)'.format(i,len(data4[2:])))


workbook.close()
