import math,sys,os
import numpy as np
import pandas as pd
import matplotlib as mplt
import itertools
import matplotlib.pyplot as plt 
from matplotlib import rcParams

mplt.rcParams['ps.useafm'] = True
mplt.rcParams['pdf.use14corefonts'] = True
mplt.rcParams['text.usetex'] = True

rcParams.update({'figure.autolayout': True})

basepath = sys.argv[1] + '/'
option = sys.argv[2]

if (option == "keysight"):
    neededfiles = ['keysight.test']
else:
    neededfiles = ['aim.test','battlefield2.test','counterstrike-source.test','dns.test','h323.test','halflife2-deathmatch.test','hotline.test','ntp.test','rtp.test','ssl.test','tsp.test','yahoo.test']

mplt.rc('xtick', labelsize=30) 
mplt.rc('ytick', labelsize=30) 


char1densegpu = []
char1sparsegpu = []

bmklist = []
totalgpu = []


for filename in neededfiles:
    if (option == "keysight"):
        df1 = pd.read_csv(basepath+'sparseresults/padded-transposed/'+filename+'.csv')
        df2 = pd.read_csv(basepath+'denseresults/unsorted/padded-transposed/'+filename+'.csv')
    else:
        df1 = pd.read_csv(basepath+'sparseresultsmedianvalues/'+filename+'.csv')
        df2 = pd.read_csv(basepath+'denseresults/unsorted/padded/'+filename+'.csv')
    
    if (option == "keysight"):
        sparsecpuchar1_16 = (df1['Total CPU'].values.tolist()[0])
        cpuchar1_16 = (df2['Total CPU'].values.tolist()[0])
    else:
        sparsecpuchar1_16 = (df1['Total CPU'].values.tolist()[1])
        cpuchar1_16 = (df2['Total CPU'].values.tolist()[0])

    sparsegpuchar1 = (df1['Execution GPU'].drop_duplicates().values.tolist()[0])   
    gpuchar1 = (df2['Execution GPU'].drop_duplicates().values.tolist()[0])   
    
    char1densegpu.append(cpuchar1_16/gpuchar1)
    char1sparsegpu.append(sparsecpuchar1_16/sparsegpuchar1)
    
    
    bmk = filename.split('.')[0]
    bmk = bmk.split('-')[0]
    bmklist.append(bmk)

zipped=zip(bmklist,char1sparsegpu,char1densegpu)    
zippedsorted=sorted(zipped, key=lambda x: x[2])    

bmklist,char1sparsegpu,char1densegpu=zip(*zippedsorted)


N = len(bmklist)
fig,ax = plt.subplots()
ind = np.arange(N)
width=0.25

p1 = ax.bar(ind,char1sparsegpu, width, color='g',hatch='//')
p2 = ax.bar(ind+width,char1densegpu, width, color='g',alpha=0.55)

# plot look and feel
# remove plot frame lines
ax.spines["top"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)

# set x axis and y axis
plt.ylim(0, 5, 1)

# set x ticks and y ticks
yrange = list(range(0,5,1))
yrange.remove(0)
plt.yticks(yrange)
ax.set_xticks(ind + (0.5*width))
ax.set_xticklabels(bmklist,rotation=28,fontsize=35)

# remove the tick marks
plt.tick_params(axis="both", which="both", bottom="off", top="off", labelbottom="on", left="off", right="off", labelleft="on")

# set background lines
for y in yrange:
    ax.axhline(y=y,color='k',ls='dotted', alpha=0.1)
ax.axhline(y=1, color='k', ls='dotted')

# set labels
if option == "network":
    plt.ylabel("Speedup compared to 16-core CPU",fontsize=40)
    ax.legend((p1[0], p2[0]), ('Sparse','Dense'),fontsize=40, loc=2)

plt.show()
