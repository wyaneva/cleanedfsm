import os,csv,sys
totalnetwork= 255 #maximum possible inputs 
path = sys.argv[1] #path to the fsm directory
placetosave = sys.argv[2] #directory to save csv

summary_lines = []
for folder, sub_folders, files in os.walk(path):
    for special_file in files:
        file_path = os.path.join(folder, special_file)
        with open(file_path, 'r+') as read_file:
            d=dict()
            for line in read_file:
                line = line.strip().split()
                if(len(line) == 4):
                    if line[1] not in d:
                        d[line[1]] = 1
                    else:
                        d[line[1]] += 1

            # save separate summaries for each fsm
            filename=file_path.rsplit('/')[-1]
            with open(placetosave + "/" + filename + ".csv", 'w') as write_file:
                file = csv.writer(write_file)
                file.writerow(['State', 'Transitions', 'Percentage Transitions'])

                num_states = 0
                num_trans = 0
                for key,values in d.items():
                    file.writerow([key,values,values/totalnetwork])
                    num_states += 1;
                    num_trans += values

                line = str(filename + "," + str(num_states) + "," + str(num_trans) + "\n")
                print(line)
                summary_lines.append(line)

            write_file.close()

        read_file.close()

# write the summary file
with open(placetosave + "/benchmark_summary.csv", 'w') as summary_file:
    summary_file.write("benchmark, states, transitions\n")
    for line in summary_lines:
        summary_file.write(line)

summary_file.close()
