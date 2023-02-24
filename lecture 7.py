#big_mac_file = './big-mac-full-index.csv'

#file=open(big_mac_file)

#for line in file:
    #if "ARG" in line:
        #print(line.split(","))

#csv_reader=csv_reader(file)

#for line in csv_reader:
    #print(line)

import pandas as pd

filename='./big-mac-full-index.csv'
df=pd.read_csv(filename)

