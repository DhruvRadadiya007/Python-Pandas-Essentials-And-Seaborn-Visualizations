import pandas as pd
import seaborn as sns

# Title: Logical OR Operator (|) in Pandas
print("\n" + "=" * 50)
print("  Title: Logical OR Operator (|)  ")
print("=" * 50 + "\n")

# Load sample dataset from Seaborn library
# dataset = titanic, df means DataFrame
df = sns.load_dataset("titanic")

# Logical Operators in Pandas:
# | :- OR (At least one condition must be True)

# --- Example: Filter passengers where class == 'First' OR class == 'Second' ---
print("# Filter: class == 'First' OR class == 'Second'")
result = df[(df['class'] == 'First') | (df['class'] == 'Second')]
print(result[['class', 'sex', 'age', 'fare']].head())
