# import plotly.plotly as py
# import plotly.graph_objs as go
# import plotly.figure_factory as FF

import math
import numpy as np
import pandas as pd
import matplotlib as mplt
import itertools
import matplotlib.pyplot as plt 
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})
neededfiles = ['aim.test','battlefield2.test','counterstrike-source.test','dns.test','h323.test','halflife2-deathmatch.test','hotline.test','ntp.test','rtp.test','ssl.test','tsp.test','yahoo.test']
names = ['padded','padded-transposed','with-offsets']
mplt.rc('xtick', labelsize=30) 
mplt.rc('ytick', labelsize=30) 

mplt.rcParams['ps.useafm'] = True
mplt.rcParams['pdf.use14corefonts'] = True
mplt.rcParams['text.usetex'] = True

#maxpadded = []
#offset = []

#char1cpu = []
#char1gpu = []

maxpaddednosort = []
offsetnosort = []
char1nosort = []
bmklist = []

for filename in neededfiles:
    df1 = pd.read_csv('./char1unsorted/'+filename+'.csv')
    df2 = pd.read_csv('./maxpaddingunsorted/'+filename+'.csv')
    df3 = pd.read_csv('./offsetunsorted/'+filename+'.csv')
    df4 = pd.read_csv('./individualcsvcpusortedminimum/'+filename+'.csv')
    
    cpuchar1 = (df4['Total Time'].values.tolist()[1])
    cpumaxpadded = (df2['Total CPU'].values.tolist()[1])
    cpuoffset = (df3['Total CPU'].values.tolist()[1])
    #cpuchar4 = (df4['Total CPU'].values.tolist()[3])
    gpuchar1 = (df1['Execution GPU'].drop_duplicates().values.tolist()[0])   
    gpumaxpadded = (df2['Execution GPU'].drop_duplicates().values.tolist()[0])   
    gpuoffset = (df3['Execution GPU'].drop_duplicates().values.tolist()[0])   
    #gpuchar4 = (df4['Execution GPU'].drop_duplicates().values.tolist()[0])   
     
    #maxpadded.append(cpumaxpadded/gpumaxpadded)
    
    #offset.append(cpuoffset/gpuoffset)

    # df1 = pd.read_csv('./individualcsvchar1/'+filename+'.csv')
    # df2 = pd.read_csv('./individualcsvoffset/'+filename+'.csv')
    # df3 = pd.read_csv('./individualcsvmaxpadded/'+filename+'.csv')
    
    # cpuchar1 = (df1['Total CPU'].values.tolist()[3])
    # cpumaxpadded = (df2['Total CPU'].values.tolist()[3])
    # cpuoffset = (df3['Total CPU'].values.tolist()[3])
    # #cpuchar4 = (df4['Total CPU'].values.tolist()[3])
    

    # gpuchar1 = (df1['Execution GPU'].drop_duplicates().values.tolist()[0])   
    # gpuoffset = (df2['Execution GPU'].drop_duplicates().values.tolist()[0])   
    # gpumaxpadded = (df3['Execution GPU'].drop_duplicates().values.tolist()[0])   
    # #gpuchar4 = (df4['Execution GPU'].drop_duplicates().values.tolist()[0])   
   
    maxpaddednosort.append(cpumaxpadded/gpumaxpadded)
    char1nosort.append(cpuchar1/gpuchar1)
    offsetnosort.append(cpuoffset/gpuoffset)
    
    if filename == 'halflife2-deathmatch.test':
        filename = 'halflife2.test'
    
    bmk = filename.split('.')[0]
    bmk = bmk.split('-')[0]
    bmklist.append(bmk)
    #totalgpu.append( timecpu1/(df['Total GPU'].drop_duplicates().values.tolist()[0]))


zipped=zip(bmklist,maxpaddednosort,char1nosort,offsetnosort)    
zippedsorted=sorted(zipped, key=lambda x: x[2])    

bmklist,maxpaddednosort,char1nosort,offsetnosort=zip(*zippedsorted)

N = len(bmklist)
fig,ax = plt.subplots()
ind = np.arange(N)
width=0.25

print(maxpaddednosort,offsetnosort,bmklist)

p1 = ax.bar(ind,maxpaddednosort, width, color='#009292')
p2 = ax.bar(ind+width,char1nosort, width, color='#490092')
p3 = ax.bar(ind+2*width,offsetnosort, width, color='#888888',hatch='//')

# plot look and feel
# remove plot frame lines
ax.spines["top"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)

# set x axis and y axis
plt.ylim(0, 9, 1)

# set x ticks and y ticks
yrange = list(range(0,9,1))
yrange.remove(0)
plt.yticks(yrange)
ax.set_xticks(ind + width)
ax.set_xticklabels(bmklist,rotation=28,fontsize=35)

# remove the tick marks
plt.tick_params(axis="both", which="both", bottom="off", top="off", labelbottom="on", left="off", right="off", labelleft="on")

# set background lines
for y in yrange:
    ax.axhline(y=y,color='k',ls='dotted', alpha=0.1)
ax.axhline(y=1, color='k', ls='dotted')

# set labels
ax.legend((p1[0], p2[0],p3[0]), (names),fontsize=40)
plt.ylabel("Speed up compared to 16-core CPU",fontsize=40)

plt.show()
plt.close()
