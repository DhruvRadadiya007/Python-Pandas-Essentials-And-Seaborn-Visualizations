import seaborn as sns

# Title: Dataset Summary Info and Statistical Description
print("\n" + "=" * 50)
print("  Title: info() and describe() Summary Statistics  ")
print("=" * 50 + "\n")

# Load sample dataset
df = sns.load_dataset("tips")

# Show basic dataset summary info (data types, non-null counts, memory usage)
print("--- Basic Dataset Info (df.info()) ---")
print(df.info())
print("\n")

# Statistical description (it has optional parameters like include="all" or include="category")
print("--- Statistical Summary (df.describe()) ---")
print(df.describe())
