#!/usr/bin/env python
# coding: utf-8

# In[25]:


import xlwt
from get_prn_dir import *
from value import *
import numpy as np
import csv


# In[65]:


A = get_prn_folder_path()
B = get_prn_dir(A)

print("计算中···")

#   E:\Python\矢网测量数据_2022-01-13
#write FREQUENCY in first cloum
# write RL in one excel
for i in B:
    # i === filename
    #i[:-4] === name  + _RL.xls  
    filename = i[:-4] + r'_RL.xls'
    
    
    FREQUENCY = prn_read(i)[:,0] / 10e8 # 1--20
    FREQUENCY_LIST = FREQUENCY.tolist() # to list form
    
    # create a excel
    workBook = xlwt.Workbook("UTF-8")
    oneWorkSheet = workBook.add_sheet("sheet1")
    oneWorkSheet.write(0, 0, "frequency")
    for o in range(len(FREQUENCY_LIST)):
        oneWorkSheet.write(o + 1,0,FREQUENCY_LIST[o])
    
                                      
    for d in np.arange(10,50,1):  # d = 
        RL = compute_RL(i,d/10,pi)
        RL = RL.tolist()
        for p in range(len(RL)):
            oneWorkSheet.write(p + 1,d-9,RL[p])
        oneWorkSheet.write(0,d-9, r'd='+ str(d/10) + r'mm')
    workBook.save(filename)
    print(filename + r'  done')
    
    
    
    filename2 = i[:-4] + r'_UV.xls'
    workBook2 = xlwt.Workbook("UTF-8")
    oneWorkSheet2 = workBook2.add_sheet("sheet1")
    #oneWorkSheet2.write(0, 0, "frequency")
    with open(i) as f:
        csv_prn = []
        prn_data = csv.reader(f)
        for b in prn_data:
            if b == []:
                continue
            else:
                csv_prn.append(b[0].split())
    for q in range(len(csv_prn[0])):   #col
        for w in range(len(csv_prn)):  #row
            if w == 0:
                oneWorkSheet2.write(w,q,csv_prn[w][q])
            elif q ==0 :
                oneWorkSheet2.write(w,q,float(csv_prn[w][q])/10e8)
            else:
                oneWorkSheet2.write(w,q,float(csv_prn[w][q]))
    workBook2.save(filename2)
    print(filename2 + r'  done')


# In[62]:


input(r'press anter to close')


# In[ ]:




