pf <- read.csv('fsm-summary.csv')
library(plyr)

# Gets the number of states per FSM
by(pf, pf$FSM, nrow)

# Gets the number of transitions per FSM
by(pf$Transitions, pf$FSM, sum)

# Saves them for output
transitions <- capture.output(by(pf$Transitions, pf$FSM, sum))
states <- capture.output(by(pf, pf$FSM, nrow))

# Outputs them in file
cat("Transitions", transitions, file="r-fsm-summary.txt", sep="\n", append=TRUE)
cat("\nStates", states, file="r-fsm-summary.txt", sep="\n", append=TRUE)
