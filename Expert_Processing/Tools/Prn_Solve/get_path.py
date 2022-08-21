




def get_path1():
    path = input("拖拽矢量网络的  prn文件|文件夹")
    if " " in path:
        path = path[1:-1]
    return path



def get_path2():
    path = input("拖拽磁性测量的  prn文件|文件夹")
    if " " in path:
        path = path[1:-1]
    return path


def get_path3():
    path = input("输入最大厚度")
    if " " in path:
        path = path[1:-1]
    return path

def get_path4():
    path = input("拖拽 矢网测量数据prn文件")
    if " " in path:
        path = path[1:-1]
    return path


    
