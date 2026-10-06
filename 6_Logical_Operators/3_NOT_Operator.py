import pandas as pd
import seaborn as sns

# Title: Logical NOT Operator (~) in Pandas
print("\n" + "=" * 50)
print("  Title: Logical NOT Operator (~)  ")
print("=" * 50 + "\n")

# Load sample dataset from Seaborn library
# dataset = titanic, df means DataFrame
df = sns.load_dataset("titanic")

# Logical Operators in Pandas:
# ~ :- NOT (Inverts a boolean condition)

# --- Example: Filter passengers who are NOT male (i.e. female) ---
print("# Filter: NOT (sex == 'male')")
result = df[~(df['sex'] == 'male')]
print(result[['sex', 'age', 'survived', 'class']].head())
