import seaborn as sns

# Title: Loading Sample Dataset
print("\n" + "=" * 40)
print("  Title: Load Sample Dataset  ")
print("=" * 40 + "\n")

# Load a sample dataset from the Seaborn library
# dataset = tips, df means DataFrame
df = sns.load_dataset("tips")

# Display top 5 rows
print(df.head())
