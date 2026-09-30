import seaborn as sns

print("\n")
print("# Load Sample Dataset ")
print("\n")

# load a sample dataset from the seaborn library
df = sns.load_dataset("titanic") # dataset = titan , df means data frames 
print(df.head()) # used to show data records (we can control the view by adding limit example :- head(10) shows first 10 rows)


print("# Two major indexing methods : ")
print("1. loc :- label based indexing")
print("2. iloc :- Position -based indexing")
print("\n")
print("# loc 1#")
print("\n")
print(df.loc[0:5,"age"]) # for single column
print(df.loc[0:5,["age",'sex']]) # for multiple columns

print("\n")
print("# loc 2#")
print("\n")
print(df.loc[df['age'] > 18, 'fare']) # with condition 


print("\n")
print("# loc 2#")
print("\n")
print(df.loc[(df['fare'] > 50) & (df['sex'] == 'male'), ['sex','fare','class']]) # with condition 

print("\n")
print("# iloc 1 #")
print("\n")
print(df.iloc[0 : 5, 2:4]) 

print("\n")
print("# Filtering with boolean conditions ")
print("\n")

print("#1#")
print("\n")

print(df[df['age'] > 30])

print("\n")
print("#2#")
print("\n")

print(df[df['sex'] == "male"])

print("\n")
print("#3#")
print("\n")

print(df[(df['age'] > 18) & (df['survived'] == 1)])


print("\n")
print("# Handling missing values before filtering #")
print("\n")

print(df[df['age'].notna()].loc[df['age'] >70]) # Filter the DataFrame to include only rows where 'age' is not null,
# and then select those rows where 'age' is greater than 70

