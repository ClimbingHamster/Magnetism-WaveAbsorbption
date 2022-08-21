
from posixpath import split

from Tools.Prn_Solve import RL

from Tools.Prn_Solve.UV_others import read_one_prn_and_write_one_xlsx
from Tools.Prn_Solve.get_path import get_path1, get_path3
import os




def script():
    path = get_path1()
    #thickness = get_path3()
    thickness = 100

    #path = r'E:\Python\Expert_Cal\NAME_DATA\矢网测量数据_2022-01-13\SFZAO_#2_3.03mm.prn'
    #path = r'E:\Python\Expert_Cal\NAME_DATA\矢网测量数据_2022-01-13'

    if os.path.isdir(path):
        for i in os.listdir(path):
            if i[-4:] == r".prn":
                read_one_prn_and_write_one_xlsx(path+'\\'+i)
                RL.cal_RL_and_write_one_xlsx(path+'\\'+i,thickness)
    elif os.path.isfile(path):
    
        read_one_prn_and_write_one_xlsx(path)
        RL.cal_RL_and_write_one_xlsx(path,thickness)

while(1):
    script()