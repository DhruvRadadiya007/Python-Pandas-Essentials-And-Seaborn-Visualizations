import pandas as pd
import seaborn as sns

# Title: Logical AND Operator (&) in Pandas
print("\n" + "=" * 50)
print("  Title: Logical AND Operator (&)  ")
print("=" * 50 + "\n")

# Load sample dataset from Seaborn library
# dataset = titanic, df means DataFrame
df = sns.load_dataset("titanic")

# Logical Operators in Pandas:
# & :- AND (Both conditions must be True)

# --- Example: Filter passengers where age > 18 AND sex == 'male' ---
print("# Filter: age > 18 AND sex == 'male'")
result = df[(df['age'] > 18) & (df['sex'] == 'male')]
print(result[['sex', 'age', 'survived', 'class']].head())
