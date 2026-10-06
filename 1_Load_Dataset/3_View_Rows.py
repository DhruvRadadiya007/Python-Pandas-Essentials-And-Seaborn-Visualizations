import seaborn as sns

# Title: Viewing Specified Number of Rows
print("\n" + "=" * 40)
print("  Title: View First 10 Rows  ")
print("=" * 40 + "\n")

# Load dataset
df = sns.load_dataset("tips")

# Used to show data records (we can control the view limit, e.g., head(10) shows first 10 rows)
print(df.head(10))
