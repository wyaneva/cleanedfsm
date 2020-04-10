import sys,os
import math
import numpy as np
import pandas as pd
import matplotlib as mplt
import itertools
import matplotlib.pyplot as plt 

mplt.rcParams['ps.useafm'] = True
mplt.rcParams['pdf.use14corefonts'] = True
mplt.rcParams['text.usetex'] = True

mplt.rc('xtick', labelsize=30) 
mplt.rc('ytick', labelsize=30) 

linestyles = ['-', ':', '-.', '--']
markers = ['x', '^', 'o', '*']
handlestyles = itertools.product(linestyles, markers)    
total = 0
handles = []
labels = []
sortingpoints = []

path = sys.argv[1]
option = sys.argv[2]

# setup plot
fig, ax = plt.subplots()

for folder, sub_folders, files in os.walk(path):
    for special_file in files:
        if not special_file.endswith(".csv"):
            continue

        file_path = os.path.join(folder, special_file)
        print(file_path)
        df = pd.read_csv(file_path)
        testcases=(df['Testcases'].drop_duplicates().values.tolist())
        totalcpu = (df['Total CPU'].values.tolist())
        cores = (df['Cores'].values.tolist())
  
        totalcpu32=[]
        totalcpu16=[]
        totalcpu8=[]
        totalcpu1=[]
        bmk = special_file.split('.')[0]
        bmk = bmk.split('-')[0]
        
        for i in range(0,len(totalcpu)):
            if(cores[i]==32):
                totalcpu32.append(totalcpu[i])
            if(cores[i]==16):
                totalcpu16.append(totalcpu[i])
            if(cores[i]==8):
                totalcpu8.append(totalcpu[i])
            if(cores[i]==1):
                totalcpu1.append(totalcpu[i])

        myindices = []

        executiongpupre = (df['Execution GPU'].values.tolist())
        totalgpupre = (df['Total GPU'].values.tolist())
        
        for i in range(0,len(executiongpupre)):
            if(cores[i]==16):
                myindices.append(i)

        executiongpu  = [ executiongpupre[i] for i in myindices ]  
        totalgpu  = [ totalgpupre[i] for i in myindices ]       
        print(len(executiongpu), bmk)
        for i in range(0,len(executiongpu)):
            executiongpu[i] = totalcpu16[i]/executiongpu[i]
            if(testcases[i] == 36027 ):
                ycord = executiongpu[i]

        print(executiongpu[0],bmk)    
        total+=executiongpu[0]
        
        handlestyle = next(handlestyles, None)
        if handlestyle is not None:
            handle,=plt.plot(testcases,executiongpu,label=bmk,linestyle=handlestyle[0],marker=handlestyle[1],markersize=13)
            handles.append(handle)
            labels.append(bmk)
            sortingpoints.append(executiongpu[0])

print(total/12)

# annotate keysight
if(option == "keysight"):
    ycord = round(ycord,2)
    ax.annotate("(36027, "+ str(ycord) + ")" , xy=(36027,ycord), textcoords='data',fontsize=30,arrowprops=dict(facecolor='black', shrink=0.05)) 

# remove plot frame lines
ax.spines["top"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)

# set x axis and y axis
plt.ylim(0, 13, 1)
ax.set_xscale('log', basex=2,subsx=(2,3,4,5,6,7,8,9,10))  

# set x ticks and y ticks
yrange = list(range(0,13,1))
plt.yticks(yrange)

# remove the tick marks
plt.tick_params(axis="both", which="both", bottom="off", top="off", labelbottom="on", left="off", right="off", labelleft="on")

# set background lines
for y in yrange:
    ax.axhline(y=y,color='k',ls='dotted', alpha=0.1)
ax.axhline(y=1, color='k', ls='dotted')

# set labels
#if(option == "keysight"):
#    plt.xlabel('Number of tests (log base 2)',fontsize=30)
#else:
plt.ylabel('Speedup compared to 16-core CPU',fontsize=30)
plt.xlabel('Number of tests (log base 2)',fontsize=30)

#sort the labels/handles by the sorting points
sortingpoints, labels, handles = zip(*sorted(zip(sortingpoints, labels, handles), key=lambda t: t[0], reverse=True))
    #set the legend
plt.legend(loc = 2, fontsize = 20, labels=labels, handles=handles,fancybox=True, framealpha=0.2)

plt.show()
