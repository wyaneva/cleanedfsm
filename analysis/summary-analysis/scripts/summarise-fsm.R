pf <- read.csv('../data/merged-fsm.csv')
library(plyr)

# Gets the number of states per FSM and sorts them
states <- sort(by(pf, pf$FSM, nrow))

# Gets the number of transitions per FSM and sorts them
transitions <- sort(by(as.numeric(as.character(pf$Transitions)), pf$FSM, sum))

# Saves them for output
transitions_out <- capture.output(transitions)
states_out <- capture.output(states)

# Outputs them in file
cat("Transitions", transitions_out, file="../data/sorted-fsm-summary.txt", sep="\n", append=FALSE)
cat("\nStates", states_out, file="../data/sorted-fsm-summary.txt", sep="\n", append=TRUE)

#####################################################################################

# Using dplyr to make a table which summarises states, transitions and density by FSM
library(dplyr)

byFSM <- group_by(pf, FSM)
table <- summarize(byFSM, 
                   states=n(), 
                   transitions=sum(as.numeric(as.character(Transitions))), 
                   density=sum(as.numeric(as.character(Density)))/n())

# Print the table on screen
options("max.print"=10000)
print.data.frame(table)

# Save table for output
table_out <- capture.output(print.data.frame(table))
cat(table_out, file="../data/summarised-fsm.tsv", sep="\n")
