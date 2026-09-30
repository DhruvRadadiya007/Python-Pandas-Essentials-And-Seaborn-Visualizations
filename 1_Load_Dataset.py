# import pandas as pd
import seaborn as sns

print("\n")
print("# Load Sample Dataset ")
print("\n")

# load a sample dataset from the seaborn library
df = sns.load_dataset("tips") # dataset = tips , df means data frames 
print(df.head()) # used to show data records (we can control the view by adding limit example :- head(10) shows first 10 rows)



print("\n")
print(df.head(10)) # load only first 10 rows


