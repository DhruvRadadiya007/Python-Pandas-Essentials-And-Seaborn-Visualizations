import seaborn as sns

# Title: Handling Missing Values Before Filtering
print("\n" + "=" * 50)
print("  Title: Handling Missing Values Before Filtering  ")
print("=" * 50 + "\n")

# Load sample dataset from Seaborn library
# dataset = titanic, df means DataFrame
df = sns.load_dataset("titanic")

print("Dataset Preview:")
print(df.head())
print("\n")

# --- Handling missing values before filtering ---
print("# Filter DataFrame to include only rows where 'age' is not null,")
print("# and then select those rows where 'age' is greater than 70:")

# Filter non-null age values then apply condition using loc
result = df[df['age'].notna()].loc[df['age'] > 70]
print(result)

print("\n# Age not null (First 10 non-null age rows):")
print(df[df['age'].notna()].head(10))
