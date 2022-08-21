
'''
这是处理吸波材料的脚本文件，主要负责 UV以及UV的衍生产品 
'''

from Tools.Formula.OriginData_Solve import *
from Tools.Prn_Solve.read_prn import read_prn
import xlwt


def read_one_prn_and_write_one_xlsx(path):
    prn_data = read_prn(path)
    
    csv_matrix = prn_data[1]
    f = csv_matrix[:,0] #fequency
    e1 = csv_matrix[:,1] #e1
    e11 = csv_matrix[:,2] #e11
    u1 = csv_matrix[:,3] #u1
    u11 = csv_matrix[:,4] #u11

    Utan(u11,u1)
    Etan(e11,e1)
    OriginF_2_PlotF(f)
    Attenuation(f,e1,e11,u1,u11)
    C0(u11,u1,f)

    a = [f,e1,e11,u1,u11
    ,OriginF_2_PlotF(f)
    ,Utan(u11,u1)
    ,Etan(e11,e1)
    ,Attenuation(f,e1,e11,u1,u11)
    ,C0(u11,u1,f)
    ,C0(u11,u1,f)*10e7]

    label = ["矢网frequency","e'","e''","u'","u''","绘图frequency","tan(δμ)","tan(δε)","alpha","C0","绘图C0"]

    workBook = xlwt.Workbook("UTF-8")
    oneWorkSheet = workBook.add_sheet("sheet1")
    for i in range(len(label)):
        oneWorkSheet.write(0, i, label[i])
        for o in range(len(f)):
            oneWorkSheet.write(o+1, i, a[i][o])
    
    workBook.save(path[:-4] + '_UV.xls')
    return 0