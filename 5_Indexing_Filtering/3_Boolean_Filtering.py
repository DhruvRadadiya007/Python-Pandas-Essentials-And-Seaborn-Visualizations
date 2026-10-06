import seaborn as sns

# Title: Filtering with Boolean Conditions
print("\n" + "=" * 50)
print("  Title: Filtering with Boolean Conditions  ")
print("=" * 50 + "\n")

# Load sample dataset from Seaborn library
# dataset = titanic, df means DataFrame
df = sns.load_dataset("titanic")

# --- Condition 1: Single numeric condition ---
print("# Condition 1: Filter rows where age > 30")
print(df[df['age'] > 30].head())
print("\n")

# --- Condition 2: Single categorical condition ---
print("# Condition 2: Filter rows where sex == 'male'")
print(df[df['sex'] == "male"].head())
print("\n")

# --- Condition 3: Multiple conditions with bitwise AND (&) ---
print("# Condition 3: Filter rows where age > 18 AND survived == 1")
print(df[(df['age'] > 18) & (df['survived'] == 1)].head())
