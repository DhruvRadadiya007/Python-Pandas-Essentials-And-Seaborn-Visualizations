import seaborn as sns

# Title: Label-Based Indexing with loc (.loc)
print("\n" + "=" * 50)
print("  Title: Label-Based Indexing with .loc  ")
print("=" * 50 + "\n")

# Load sample dataset from Seaborn library
# dataset = titanic, df means DataFrame
df = sns.load_dataset("titanic")

print("Dataset Preview:")
print(df.head())
print("\n")

# Explanation of loc vs iloc index slicing behavior:
# Note: In .loc (label-based), the end index is INCLUSIVE (e.g., 0:5 includes rows 0, 1, 2, 3, 4, AND 5).
# In .iloc (position-based), the end index is EXCLUSIVE (e.g., 0:5 includes rows 0, 1, 2, 3, and 4).

# --- Example 1: Selecting single and multiple columns by label ---
print("--- loc 1: Slicing by label ---")
print("# Single column ('age'):")
print(df.loc[0:5, "age"])  # For single column

print("\n# Multiple columns (['age', 'sex']):")
print(df.loc[0:5, ["age", "sex"]])  # For multiple columns

# --- Example 2: Selecting rows with single condition ---
print("\n--- loc 2: Filtering rows with condition ---")
print("# Filter rows where age > 18 and select 'fare' column:")
print(df.loc[df['age'] > 18, 'fare'])  # With condition

# --- Example 3: Selecting rows with multiple conditions ---
print("\n--- loc 3: Filtering rows with multiple conditions ---")
print("# Filter rows where fare > 50 AND sex == 'male', selecting ['sex', 'fare', 'class']:")
print(df.loc[(df['fare'] > 50) & (df['sex'] == 'male'), ['sex', 'fare', 'class']])  # With condition
