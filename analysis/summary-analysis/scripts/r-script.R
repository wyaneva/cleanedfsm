pf <- read.csv('../data/fsm-summary.csv')
library(plyr)

# Gets the number of states per FSM
states <- sort(by(pf, pf$FSM, nrow))

# Gets the number of transitions per FSM
transitions <- sort(by(as.numeric(as.character(pf$Transitions)), pf$FSM, sum))

# Saves them for output
transitions_out <- capture.output(transitions)
states_out <- capture.output(states)

# Outputs them in file
cat("Transitions", transitions_out, file="../data/r-fsm-summary.txt", sep="\n", append=FALSE)
cat("\nStates", states_out, file="../data/r-fsm-summary.txt", sep="\n", append=TRUE)
