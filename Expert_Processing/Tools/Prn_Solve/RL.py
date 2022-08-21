
from ast import Str
from Tools.Formula.OriginData_Solve import RL_equation

from Tools.Prn_Solve.read_prn import read_prn
import xlwt

def cal_RL_and_write_one_xlsx(path,thickness):
    # thickness 0.3mm-10mm
    prn_data = read_prn(path)
    csv_matrix = prn_data[1]
    

    workBook = xlwt.Workbook("UTF-8")
    oneWorkSheet = workBook.add_sheet("sheet1")

    # col 1 = frequency
    oneWorkSheet.write(0,0,"frequency\mm")
    for i in range(len(csv_matrix[:,0])):
        oneWorkSheet.write(i+1,0,csv_matrix[i,0]/10e8)
    
    
    # 0,0 = null
    # others = RL

    # row 1 = thickness
    
    
        
    for d in range(1,thickness,1):
        oneWorkSheet.write(0,d,d/10)
        result = RL_equation(csv_matrix,d/10)
        for p in range(len(result)):
            oneWorkSheet.write(p+1,d,result[p])

    workBook.save(path[:-4] + '_RL.xls')
    return 0

        

    
    

    