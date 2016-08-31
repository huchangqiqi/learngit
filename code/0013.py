import xlwt
from datetime import datetime
import json
#
"""
style0 = xlwt.easyxf('font: name Times New Roman,color-index red,bold on',num_format_str='#,##0.00')
style1 = xlwt.easyxf(num_format_str='D-MMM-YY')

wb = xlwt.Workbook()
ws = wb.add_sheet('A Test Sheet')

ws.write(0,0,1234.56, style0)
ws.write(1,0,datetime.now(),style1)
ws.write(2,0,1)
ws.write(2,1,1)
ws.write(2,2,xlwt.Formula("A3+B3"))

wb.save('example.xls')
"""
wb = xlwt.Workbook()
ws = wb.add_sheet('student')

with open ('student.txt','r') as f:
    data = f.read()
    jsonData = json.loads(data)
    for x in range(len(jsonData)):
        s = str(x+1)
        ws.write(x,0,int(s))
        for y in range(len(jsonData[s])):
            #print(jsonData[s][y])
            ws.write(x,y+1,jsonData[s][y])
    wb.save('student.xls')



