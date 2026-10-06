import pandas as pd
import seaborn as sns

# Title: Logical Operators in Pandas
print("\n" + "=" * 50)
print("  Title: Logical Operators in Pandas  ")
print("=" * 50 + "\n")

# Summary of Bitwise Logical Operators in Pandas:
# &  :- AND (Both conditions must be True)
# |  :- OR  (At least one condition must be True)
# ~  :- NOT (Inverts condition / Negation)

# Load sample dataset from Seaborn library
# dataset = titanic, df means DataFrame
df = sns.load_dataset("titanic")

print("Titanic Dataset Preview:")
print(df.head())

# --- 1. AND Operator (&) ---
print("\n" + "=" * 40)
print("  1. AND Operator (&)  ")
print("=" * 40 + "\n")
print("# Filter: Age > 18 AND Sex == 'male':")
print(df[(df['age'] > 18) & (df['sex'] == 'male')][['sex', 'age', 'survived']].head())

# --- 2. OR Operator (|) ---
print("\n" + "=" * 40)
print("  2. OR Operator (|)  ")
print("=" * 40 + "\n")
print("# Filter: Class == 'First' OR Class == 'Second':")
print(df[(df['class'] == 'First') | (df['class'] == 'Second')][['class', 'sex', 'fare']].head())

# --- 3. NOT Operator (~) ---
print("\n" + "=" * 40)
print("  3. NOT Operator (~)  ")
print("=" * 40 + "\n")
print("# Filter: NOT (Sex == 'male'):")
print(df[~(df['sex'] == 'male')][['sex', 'age', 'class']].head())
