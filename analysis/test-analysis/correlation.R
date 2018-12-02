# read data
pf <- read.csv('testlengthvsspeedup.csv')
summary(pf)

# plot correlation graph
library(ggplot2)
ggplot(aes(x=avg.test.length, y=speedup), data=pf) +
geom_point()

# use test to establish correlation
library(dplyr)
cor.test(pf$speedup, pf$avg.test.length)
