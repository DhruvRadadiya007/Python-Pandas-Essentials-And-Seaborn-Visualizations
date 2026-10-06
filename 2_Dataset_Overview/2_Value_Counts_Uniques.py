import seaborn as sns

# Title: Unique Values and Frequency Table (Value Counts)
print("\n" + "=" * 50)
print("  Title: Unique Values and Value Counts  ")
print("=" * 50 + "\n")

# Load sample dataset
df = sns.load_dataset("tips")

# Displays count of unique values per column
print("Unique values per column:\n", df.nunique())
print("\n")

# Displays number of values of categorical data
print("Value counts for column 'sex':\n", df['sex'].value_counts())
print("\n")
print("Alternative syntax df.value_counts('sex'):\n", df.value_counts('sex'))
