from tokenize import Double
import xlwt

def write_magentic_to_xls(path,data):
    
    label = data[0]
    matrix = data[1]

    print(matrix[:,0])

    workBook = xlwt.Workbook("UTF-8")
    oneWorkSheet = workBook.add_sheet("sheet1")

    for i in range(len(label)):
        oneWorkSheet.write(0,i,label[i])
    
    for o in range(len(matrix[:,0])):
        for p in range(len(label)):
            oneWorkSheet.write(o+1,p,float(matrix[o][p]))

    workBook.save(path[:-4] + '_mag.xls')