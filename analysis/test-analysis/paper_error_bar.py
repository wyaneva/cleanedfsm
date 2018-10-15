# import plotly.plotly as py
# import plotly.graph_objs as go
# import plotly.figure_factory as FF

import math, sys
import numpy as np
import pandas as pd
import matplotlib as mplt
import itertools
import matplotlib.pyplot as plt 
from matplotlib import rcParams

rcParams['ps.useafm'] = True
rcParams['pdf.use14corefonts'] = True
rcParams['text.usetex'] = True

rcParams.update({'figure.autolayout': True})

fsmfile = sys.argv[1] # the csv file which contains the test case analysis for the FSMs

df = pd.read_csv(fsmfile)
mplt.rc('xtick', labelsize=40) 
mplt.rc('ytick', labelsize=40) 

fsm = (df['FSM'].drop_duplicates().values.tolist())
num_fsm = len(fsm)
for i in range(0,len(fsm)):
    filename = fsm[i]
    fsm[i]=fsm[i].split('-')[0]
    if filename == 'halflife2-deathmatch':
        fsm[i] = 'halflife2'
     
avgall = (df['Average all'].drop_duplicates().values.tolist())
stderr = (df['Standard Deviation'].drop_duplicates().values.tolist())

zipped=zip(fsm,avgall,stderr)
zippedsorted = sorted(zipped,key=lambda x: x[1]) 

fsm,avgall,stderr=zip(*zippedsorted)

fig,ax=plt.subplots()
# remove plot frame lines
ax.spines["top"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)

# set x axis and y axis
#plt.ylim(0, 30, 5)

# set x ticks and y ticks
#yrange = list(range(0,30,5))
#yrange.remove(0)
yrange = list(range(400,1700,200))
plt.yticks(yrange)
ax.set_xticklabels(fsm,rotation=45,fontsize=50)

# remove the tick marks
plt.tick_params(axis="both", which="both", bottom="off", top="off", labelbottom="on", left="off", right="off", labelleft="on")

# set background lines
for y in yrange:
    plt.plot(range(0-1, num_fsm+1), [y]*len(range(0-1, num_fsm+1)), "--", lw=0.5, color="black", alpha=0.3)

#plt.ylabel("Average Test Length",fontsize=50)
plt.errorbar(fsm, avgall, stderr, linestyle='None', marker='^', capsize=10,markersize=20) 

plt.show()
plt.close()
