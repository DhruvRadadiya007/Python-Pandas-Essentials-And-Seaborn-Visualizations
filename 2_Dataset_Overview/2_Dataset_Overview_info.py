import pandas as pd 
import seaborn as sns

# Title: 1. Load Sample Dataset
print("\n" + "=" * 40)
print("  Title: Load Sample Dataset  ")
print("=" * 40 + "\n")

# Load a sample dataset from the Seaborn library
# dataset = tips, df means DataFrame
df = sns.load_dataset("tips")

# Used to show data records (we can control the view by adding limit, e.g., head(10) shows first 10 rows)
print(df.head())

# Title: 2. Dataset Overview
print("\n" + "=" * 40)
print("  Title: Dataset Overview  ")
print("=" * 40 + "\n")

# Displays number of rows and columns (shape)
print("Shape:", df.shape)
print("\n")

# Displays data types of each column
print("Data Types:\n", df.dtypes)
print("\n")

# Displays count of unique values per column
print("Unique values:\n", df.nunique())
print("\n")

# Displays number of values for categorical data column
print("Value counts for 'sex':\n", df.value_counts('sex'))
print("\n")

# Displays column names in the form of a Python list
print("Columns:", df.columns.to_list())
print("\n")

# Show basic dataset info (data types, non-null counts, memory usage)
print("Dataset Summary Info:")
print(df.info())

# Title: 3. Statistical Dataset Info
print("\n" + "=" * 40)
print("  Title: Statistical Dataset Info  ")
print("=" * 40 + "\n")

# Summary statistics (it has optional parameters like include="all" or include="category")
print(df.describe())

# Title: 4. Count Values in a Specific Column
print("\n" + "=" * 40)
print("  Title: Count Values in a Column  ")
print("=" * 40 + "\n")

# Getting count of unique values in a specific column ('sex')
print(df['sex'].value_counts())

# Title: 5. DataFrame Inspection Essentials Summary
print("\n" + "=" * 40)
print("  Title: DataFrame Inspection Essentials  ")
print("=" * 40 + "\n")

# Quick Reference Guide:
# .head(n)        - View first n rows
# .tail(n)        - View last n rows
# .shape          - Dimensions (rows, columns)
# .columns        - Column names
# .dtypes         - Data types of columns
# .nunique()      - Count unique values per column
# .value_counts() - Frequency table (for categorical data)
# .describe()     - Summary statistics (numeric columns by default)
