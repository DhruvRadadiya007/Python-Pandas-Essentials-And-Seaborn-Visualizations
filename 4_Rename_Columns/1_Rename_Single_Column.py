import seaborn as sns

# Title: Renaming a Single Column
print("\n" + "=" * 40)
print("  Title: Rename Single Column  ")
print("=" * 40 + "\n")

# Load sample dataset
# dataset = tips, df means DataFrame
df = sns.load_dataset("tips")

print("Original Columns:", df.columns.to_list())

# Rename column 'sex' to 'gender'
df = df.rename(columns={"sex": "gender"})

print("\nRenamed Columns:", df.columns.to_list())
print(df.head(1))
