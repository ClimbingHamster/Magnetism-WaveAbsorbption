#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from  csv import reader
import matplotlib.pyplot as plt
from value import *


# In[19]:


# read prn file data
def prn_read(path_file):
    with open(path_file) as f:
        csv_prn = []
        prn_data = reader(f)
        for b in prn_data:
            if b == []:
                continue
            else:
                csv_prn.append(b[0].split())
            arry = np.array(csv_prn[1:])
            # astype string ==>> float
            csv_matrix = arry.astype(float)
        f.close()
        return csv_matrix

# calculate Refection loss
def RL_equation(csv_matrix,d,pi):
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
    return(RL)



def quick_plot(path_file,d,pi):
    #quick show plot
    csv_matrix =prn_read(path_file)
    RL = RL_equation(csv_matrix,d,pi)
    
    a = path_file.split('\\')
    b = len(a)
                        
    FIG = plt.subplot()
    FIG.plot(csv_matrix[:,0]/10e8,RL)
    FIG.set(xlabel='Fequency (1e10 GHz)', ylabel='Reflection loss (DB)',
       title='RL & Fequency\n' + r'd =' + str(d) + 'mm'+ '    '+ a[b-1]  )
    plt.show()
    
# compute RL
def compute_RL(path_file,d,pi):
    csv_matrix =prn_read(path_file)
    RL = RL_equation(csv_matrix,d,pi)
    return RL

# In[20]:



#quick_plot(path_file,4,pi)


# In[ ]:




