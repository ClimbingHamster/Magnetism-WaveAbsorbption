
from math import pi,sqrt

import numpy as np


def OriginF_2_PlotF(Origin_Frequency):
    Plot_Frequency = Origin_Frequency/10e8
    plot_frequency = 'Plot_Frequency'
    return Plot_Frequency

def Utan(u11,u1):
    utan = '磁性损耗正切'
    return u11/u1

def Etan(e11,e1):
    etan = '介电损耗正切'
    return e11/e1


def Attenuation(f,e1,e11,u1,u11):
    Attenuation = '衰减特性'

    first_item =  (sqrt(2)*pi*f)/(3e8)
    seconde_item = np.sqrt((u11*e11-u1*e1)+np.sqrt(np.power(u1*e11+u11*e1,2)+np.power(u11*e11-u1*e1,2)))

    alpha =first_item*seconde_item
    return alpha

def C0(u11,u1,f):
    C0 = u11*np.power(u1,-2)*np.power(f,-1)
    co= 'C0'
    return C0



def RL_equation(csv_matrix,d):
    
    A = csv_matrix
    Z_1 = np.sqrt( 
        (A[:,3] + 1j * A[:,4])
        /
        
        (A[:,1] + 1j * A[:,2]) 
    )

    Z_2 =np.tanh(

        (-1j*(2*pi*A[:,0]*np.sqrt((A[:,1]+1j*A[:,2])*(A[:,3]+1j*A[:,4]))*d/2.99792458e11))

    )
      
    Z = Z_1 * Z_2
    RL = 20 * np.log10( np.abs((1-Z)/(1+Z)))
    return RL




