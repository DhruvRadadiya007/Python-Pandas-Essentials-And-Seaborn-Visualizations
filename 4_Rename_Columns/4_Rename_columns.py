import seaborn as sns

# Title: 1. Load Sample Dataset
print("\n" + "=" * 40)
print("  Title: Load Sample Dataset  ")
print("=" * 40 + "\n")

# Load a sample dataset from the Seaborn library
# dataset = tips, df means DataFrame
df = sns.load_dataset("tips")

# Used to show data records (we can control the view by adding limit, e.g., head(10) shows first 10 rows)
print(df.head())

# Title: 2. Rename Columns in DataFrame
print("\n" + "=" * 40)
print("  Title: Rename Columns  ")
print("=" * 40 + "\n")

# Rename column 'sex' to 'gender' using columns dictionary parameter
# Note: You can also specify axis=1 or axis='columns' (e.g., df.rename({"sex": "gender"}, axis=1))
df = df.rename(columns={"sex": "gender"})
print(df.head(1))
