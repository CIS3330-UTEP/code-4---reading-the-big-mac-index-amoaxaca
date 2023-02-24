import pandas as pd

filename='./big-mac-full-index.csv'
df=pd.read_csv(filename)
query_string = "(iso_a3=='ARG')"
print(query_string)
arg_df=df.query(query_string)
print(arg_df)

