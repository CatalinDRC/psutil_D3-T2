# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import psutil
import platform
from datetime import datetime

#Lucrul cu fisiere
f = open("Stocare.txt",'a')

# CPU usage

core=[]
print("CPU Usage Per Core:")
for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
    print(f"Core {i}: {percentage}%")
    core.append(percentage)
print(f"Total CPU Usage: {psutil.cpu_percent()}%")


if(psutil.cpu_percent() >= 90):
    print("Atentie CPU este prea ridicat")
    f.write(f"PCU are valoarea ={psutil.cpu_percent()}")
f.close()
# A function that defines "k","M"....
def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

# get the memory details
print("="*20, "Memory", "="*20)
print("The memory in the disk")
svmem = psutil.virtual_memory()
print(f"Total: {get_size(svmem.total)}")
print(f"Available: {get_size(svmem.available)}")
print(f"Used: {get_size(svmem.used)}")
print(f"Percentage: {svmem.percent}%")

if(svmem.percent >= 90):
    print("Memoria depaseste peste 90% din spatiu")

#instalam gputil

import  GPUtil
# get % percentage of GPU usage of that GPU
print("="*20, "GPU", "="*20)
print("The Graphical unit:")
gpus = GPUtil.getGPUs()
list_gpus = []
for gpu in gpus:

    # get used memory
    gpu_used_memory = gpu.memoryUsed
    # get total memory
    gpu_total_memory = gpu.memoryTotal
    # get GPU temperature in Celsius
    gpu_temperature = gpu.temperature

load = (gpu_used_memory/gpu_total_memory)*100
print("The load:")
print(f"{load}%")
print(f"Temperatura este:{gpu_temperature} grade C")
if(load >= 90):
    print("Atentie GPU depaseste 90%")

#Reprezentarea grafica a CPU-ului
import matplotlib.pyplot as plt


#https://www.youtube.com/watch?v=MPiz50TsyF0&ab_channel=CoreySchafer


#Setam stilul
plt.style.use("fivethirtyeight")

#introducem valorile feliilor
slices = [core[0],core[1],core[2],core[3],100 - (core[0] + core[1] + core[2] + core[3])]
labels = ['Core1','Core2','Core3','Core4','Nefolosit']
colors = ['blue','red','yellow','green','red']
slices1 = [psutil.cpu_percent(),100 - psutil.cpu_percent()]
labels1 = ['Memorie Folosita','Memorie ramasa']
slices2 = [svmem.percent,100  - svmem.percent]
labels2 = ['Memorie folosita disk','Memorie ramasa disk']
slices3 = [load,100  - load]
labels3= ['Mem Grafica folosita','Mem Grafica ramasa']
#Formam graficul
plt.pie(slices, labels = labels ,colors = colors, wedgeprops = {'edgecolor':'black'},autopct = '%1.1f%%')

#Scrie un titlu deasupra graficului
plt.title("Core use:")
plt.tight_layout()
#arata graficul
plt.show()
plt.title("CPU use:")
plt.pie(slices1,labels = labels1,wedgeprops = {'edgecolor':'black'},autopct = '%1.1f%%')
plt.show()
plt.title("Disk use:")
plt.pie(slices2,labels = labels2,wedgeprops = {'edgecolor':'black'},autopct = '%1.1f%%')
plt.show()
plt.title("Graphic memory use:")
plt.pie(slices3,labels = labels3,wedgeprops = {'edgecolor':'black'},autopct = '%1.1f%%')
plt.show()
#Colors
#Blue = #008fd5
#Red = #fc4f30
#Yellow = #e5ae37
#Green = #6d904f


