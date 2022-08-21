


from Tools.Prn_Solve.get_path import get_path2
from Tools.Prn_Solve.magentism import write_magentic_to_xls
from Tools.Prn_Solve.read_prn import read_mag_data
import os

def script():
    path = get_path2()
    
    #path  = r'E:\Python\Expert_Cal\NAME_DATA\Magnetism_Data\BC220103-20-changh-CSSFCA13-21.4mg.txt'

    #read_mag_data(path)
    # 获得磁性数据

    if os.path.isdir(path):
        for i in os.listdir(path):
            if i[-4:] == r".txt":
                # convert_write(i,xls)
                data = read_mag_data(path+ '\\' + i)
                write_magentic_to_xls(path+'\\'+i,data)
                pass
    elif os.path.isfile(path):
        # convert_write(path,xls)
        data = read_mag_data(path)
        write_magentic_to_xls(path,data)
        pass
    

while(1):
    script()