# reads the summary of all fsms
# picks the ones larger than l7-filter (more than 40 694 transitions)
# sorts them and outputs them in a separate file

pf <- read.csv('../data/summarised-fsm.csv')
sd <- subset(pf, transitions > 40694)

library(dplyr)
sdar <- arrange(sd, sd$transitions)

# Print the table on screen
options("max.print"=10000)
print.data.frame(sdar)

# Save table for output
sdar_out <- capture.output(print.data.frame(sdar))
cat(sdar_out, file="../data/sorted-large-fsm.csv", sep="\n")
