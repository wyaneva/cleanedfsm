# plots the correlation between max speedup and avg test length

import numpy as np
from numpy.polynomial.polynomial import polyfit
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import rcParams

rcParams['ps.useafm'] = True
rcParams['pdf.use14corefonts'] = True
rcParams['text.usetex'] = True
rcParams.update({'figure.autolayout': True})

# Sample data
df = pd.read_csv("testlengthvsspeedup.csv")
speedup = (df['speedup'].values.tolist())
avgtestlength = (df['avg test length'].values.tolist())

# Scatter plot
plt.scatter(avgtestlength, speedup)

# Add correlation line
axes = plt.gca()
m, b = np.polyfit(avgtestlength, speedup, 1)
X_plot = np.linspace(axes.get_xlim()[0],axes.get_xlim()[1],100)
plt.plot(X_plot, m*X_plot + b, '-')

# remove plot frame lines
axes.spines["top"].set_visible(False)
axes.spines["bottom"].set_visible(False)
axes.spines["right"].set_visible(False)
axes.spines["left"].set_visible(False)

# set x ticks and y ticks
xrange1 = list(range(6,19,2))
plt.xticks(xrange1,fontsize=20)
yrange = list(range(0,13,2))
plt.yticks(yrange, fontsize=20)

# remove the tick marks
plt.tick_params(axis="both", which="both", bottom="off", top="off", labelbottom="on", left="off", right="off", labelleft="on")

plt.xlabel("Average test length",fontsize=30)
plt.ylabel("Maximum speedup",fontsize=30)

plt.show()
