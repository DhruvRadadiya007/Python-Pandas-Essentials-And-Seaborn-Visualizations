import pandas as pd 
import seaborn as sns

print("\n")
print("# Load Sample Dataset ")
print("\n")

# load a sample dataset from the seaborn library
df = sns.load_dataset("tips") # dataset = tips , df means data frames 
print(df.head()) # used to show data records (we can control the view by adding limit example :- head(10) shows first 10 rows)


print("\n")
print("# Dataset Overview ")
print("\n")

print("Shape:",df.shape) # displays number of rows and columns
print("\n")
print("Data Types:",df.dtypes) # displays data types
print("\n")
print("Unique values:",df.nunique()) # displays unique values
print("\n")
print(df.value_counts('sex')) # displays number of values of only categorical data
print("\n")
print("Columns:",df.columns.to_list) # displays column names in the form of list
print("\n")
print(df.info()) # show basic dataset info 

print("\n")
print("# Statistical Dataset Info")
print("\n")

print(df.describe()) # it has a property include = "all"

print("\n")
print("# Getting count of values in a column")
print("\n")


print(df['sex'].value_counts())



print("\n")
print("DataFrame inspection essentials ")
print("\n")

# .head(n)	View first n rows
# .tail(n)	View last n rows
# .shape	Dimensions (rows, columns)
# .columns	Column names
# .dtypes	Data type
# .nunique()	Count unique values
# .value_counts()	Frequency table (for categoricals)
# .describe()	Summary stats (numeric only by default)


