'''
f:frequency:x
d:thickness:y
RL:reflextion loss:z
'''




from Tools.Formula.OriginData_Solve import RL_equation
from Tools.Prn_Solve.get_path import get_path4
from Tools.Prn_Solve.read_prn import read_prn
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D




def script():
    path = get_path4()


    if path[-4:] == r'.prn':
        csv_matrix = read_prn(path)
        thickness = [x/10 for x in range(1,100)]
        matrix = np.array(csv_matrix[1])

    

    

    #x = matrix[:,0]
    #y = thickness
    #z = RL
        x = []
        y = []
        z = []
    
        for o in thickness:
            RL = RL_equation(matrix,o)
        
            for i in range(len(matrix[:,0])):
                y.append(o)
                x.append(matrix[i,0])
                z.append(RL[i])
            

                
            
        

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
    
        ax.plot_trisurf(y, x, z)
        ax.set_ylabel('y : frequency : 10e8')
        ax.set_xlabel('x : thickness')
        ax.set_zlabel('z : RL')

        filename = path.split('\\')
        i = len(filename)
        plt.title(filename[i-1])
        plt.show()
    
    
while(1):
    script()
    
    
#  E:\Python\Expert_Cal\NAME_DATA\矢网测量数据_2022-01-13\SFZAO_#1_3.22mm.prn