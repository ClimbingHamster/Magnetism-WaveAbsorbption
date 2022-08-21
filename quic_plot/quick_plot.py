
from get_prn_dir import * 
from value import *

from warnings import filterwarnings

filterwarnings("ignore")

while 1:
    path_file = get_path_file()
    d = get_d()

    quick_plot(path_file,d,pi)
    print(path_file +'  ·······Done\n\n')
  


 
