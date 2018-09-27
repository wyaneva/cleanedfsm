Contains scripts which perform analysis on the FSMs AND its tests and output them in data files. These data files will be analysed using R.

1. `summarise-fsm.py`: 
* merges all consolidated fsm files from fsm analysis into a single file
* adds a column at the beginning, noting which the fsm is
* the fsm name is derived from the name of the consolidated file

2. `r-script.R`:
* contains R scripts that group the data by FSM and summarise states, transitions and density
* `R -p r-script.R` executes the script and stays inside R
