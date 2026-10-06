import seaborn as sns

# Title: Position-Based Indexing with iloc (.iloc)
print("\n" + "=" * 50)
print("  Title: Position-Based Indexing with .iloc  ")
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

# --- Example 1: Integer position slicing ---
print("--- iloc 1: Slicing by integer positions ---")
print("# Selecting rows 0 to 4 (index 0:5) and columns at index positions 2 to 3 (2:4):")
print(df.iloc[0:5, 2:4])
