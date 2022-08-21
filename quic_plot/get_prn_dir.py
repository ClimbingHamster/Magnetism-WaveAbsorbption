#!/usr/bin/env python
# coding: utf-8

# In[1]:


# thin from 1mm to 5mm , step 0.1mm ;
# deal vu into a xls ;
# to origin plot


# In[2]:


from os import listdir
from RL_calculate import *
from value import *


# In[3]:


#活动 prn 文件列表   path << cmd 可以直接拖拽文件夹
def get_prn_dir(path):
    listdir1 = listdir(path)
    prn_list = []
    for i in listdir1:
        #print(i[-4:])
        if i[-4:] == r'.prn':
            prn_list.append(path + r'/' +  i)
    return prn_list
    

#path << cmd 可以直接拖拽文件夹
def get_prn_folder_path():
    PATH = input(r'拖拽放置prn的文件夹： ')
    return PATH


def get_d():
    d = input(r'输入厚度，d = ?mm ')
    return float(d)
def get_path_file():
    path_file = input(r'拖拽一个prn文件： ')
    return path_file




# In[4]:




#get_prn_dir(path_workspace)


# In[ ]:




