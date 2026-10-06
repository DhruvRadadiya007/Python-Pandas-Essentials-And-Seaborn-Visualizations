import seaborn as sns

# Title: Viewing DataFrame Columns
print("\n" + "=" * 40)
print("  Title: View Columns  ")
print("=" * 40 + "\n")

# Load dataset
df = sns.load_dataset("tips")

# 1. View One Column
print("# View One Column ('sex'):")
print(df["sex"].head())

# 2. View Multiple Columns
print("\n# View Multiple Columns (['sex', 'tip']):")
print(df[["sex", "tip"]].head())
