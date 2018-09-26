# merges all consolidated fsm files from fsm analysis into a single file
# adds a column at the beginning, noting which the fsm is
# the fsm name is derived from the name of the consolidated file

import os,csv,sys

path = sys.argv[1] # path to the files containing fsm summaries
                   # the new file will be saved in the directory 'data' next to current directory

# open the new file
with open("../data/fsm-summary.csv", 'w') as write_file:
    write_file.write("FSM, State, Transitions, Density\n")

    for folder, sub_folders, files in os.walk(path):
        for special_file in files:
            file_path = os.path.join(folder, special_file)
            fsmname=file_path.rsplit('/')[-1]
            fsmname=fsmname.split('.')[0]

            with open(file_path, 'r+') as read_file:
                next(read_file)
                for line in read_file:
                    print(fsmname)
                    write_file.write(fsmname + "," + line)
        read_file.close()
write_file.close()
