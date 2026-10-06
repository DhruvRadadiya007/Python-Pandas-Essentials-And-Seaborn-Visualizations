import seaborn as sns

# Title: 1. Load Sample Dataset Overview
print("\n" + "=" * 40)
print("  Title: Load Sample Dataset  ")
print("=" * 40 + "\n")

# Load a sample dataset from the Seaborn library
# dataset = tips, df means DataFrame
df = sns.load_dataset("tips")
print(df.head())  # Used to show data records (default is 5 rows)

# Title: 2. View One Column
print("\n" + "=" * 40)
print("  Title: View One Column  ")
print("=" * 40 + "\n")

# Viewing a single column from the DataFrame
print(df["sex"].head())

# Title: 3. View Multiple Columns
print("\n" + "=" * 40)
print("  Title: View Multiple Columns  ")
print("=" * 40 + "\n")

# Viewing multiple columns by passing a list of column names
print(df[["sex", "tip"]].head())

# Title: 4. View Specified Number of Rows
print("\n" + "=" * 40)
print("  Title: View First 10 Rows  ")
print("=" * 40 + "\n")

# Used to show data records (we can control the view limit, e.g., head(10) shows the first 10 rows)
print(df.head(10))
