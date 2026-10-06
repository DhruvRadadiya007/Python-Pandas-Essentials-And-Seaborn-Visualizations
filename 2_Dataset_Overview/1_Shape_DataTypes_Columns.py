import seaborn as sns

# Title: Dataset Shape, Data Types, and Column Names
print("\n" + "=" * 50)
print("  Title: Shape, Data Types, and Columns  ")
print("=" * 50 + "\n")

# Load sample dataset
df = sns.load_dataset("tips")

# Displays number of rows and columns (shape)
print("Shape (rows, columns):", df.shape)
print("\n")

# Displays data types of each column
print("Data Types:\n", df.dtypes)
print("\n")

# Displays column names in the form of a list
print("Columns List:", df.columns.to_list())
