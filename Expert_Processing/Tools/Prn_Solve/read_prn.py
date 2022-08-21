

import numpy as np
from  csv import reader

def read_prn(prn_path_filename):
    print("prn_path_filename" + prn_path_filename)
    with open(prn_path_filename) as f:
        csv_prn = []
        prn_data = reader(f)
        for b in prn_data:
            if b == []:
                continue
            else:
                csv_prn.append(b[0].split())
        arry0 = np.array(csv_prn[0])
        arry = np.array(csv_prn[1:])
            # astype string ==>> float
        csv_matrix = arry.astype(float)

            
    f.close()
    return arry0,csv_matrix



# filename = r'E:\Python\Expert_Cal\NAME_DATA\Magnetism_Data\BC220103-20-changh-CSSFCA13-21.4mg.txt'

def read_mag_data(filename):
    with open(filename) as f:
        txt = f.read()
        label = txt.split('\n')[0].split(',')
        # label 已经导出
        print(label)
    
        matrix = []
        for i in range(len(txt.split('\n'))-1):
      
            row = txt.split('\n')[i].split(',')
            matrix.append(row)
            # 数据也导出，matrix就是
        label = np.array(matrix[0])
        matrix = np.array(matrix[1:])

    f.close()
    return label,matrix