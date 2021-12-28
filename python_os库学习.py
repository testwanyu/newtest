"""os 库提供通用的、基本的操作系统交互功能"""
"""
os 库是Python标准库，包含几百个函数，常用的有路径操作、进程管理、环境参数等。

路径操作 ：os.path子库，处理文件路径及信息

进程管理：启动系统中其他程序

环境参数：获得系统软硬件信息等环境参数
"""
import os

filename = os.path.dirname(__file__) #当前文件上一级目录
print(filename)



print(os.path.abspath("report/report.html"))  #返回path,在当前系统中的绝对路径,os.path.abspath取决于os.getcwd,如果是一个绝对路径，
print(os.path.realpath("diedaiqi.txt"))  # 就返回，如果不是绝对路径，根据编码执行getcwd/getcwdu.然后把path和当前工作路径连接起来．

print(os.pardir)  #返回当前目录的父目录，默认值为 ..
print(os.getcwd()) #返回当前目前的父目录
print(os.path.getctime('python_os库学习.py'))  #返回创建时间
print(os.path.getatime('python_os库学习.py')) #返回上一次访问的时间
print(os.path.isfile('python_os库学习.py'))
files = os.scandir(r'C:\Users\Administrator\Desktop')
# files1 = os.listdir(r'C:\Users\Administrator\Desktop')
# for file in files1:
#     if file.endswith('doc') or file.endswith('lnk'):
#         print(file)


all = os.walk(r'D:\项目资料')
for path ,dir,filelist in all:
    for filename in filelist:
        if filename.endswith('jpg'):
            print(filename)





