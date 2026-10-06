import seaborn as sns

# Title: Renaming Columns Using Axis Parameter
print("\n" + "=" * 50)
print("  Title: Rename Columns with Axis Parameter  ")
print("=" * 50 + "\n")

# Load sample dataset
df = sns.load_dataset("tips")

print("Original Columns:", df.columns.to_list())

# You can pass dictionary with axis=1 or axis='columns'
# Note: df.rename({"sex": "gender", "tip": "tip_amount"}, axis=1)

df = df.rename(columns={"sex": "gender", "tip": "tip_amount"})

# or this way :-

# df = df.rename(mapper={"sex": "gender", "tip": "tip_amount"}, axis=1)


print("\nRenamed Columns:", df.columns.to_list())
print(df.head(1))
