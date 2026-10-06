import pandas as pd

# Title: Importing JSON and SQL Data in Pandas
print("\n" + "=" * 50)
print("  Title: Importing JSON and SQL Data  ")
print("=" * 50 + "\n")

# 1. Load JSON file :- pd.read_json("filename.json")
# Example usage:
# df_json = pd.read_json("data.json")

# 2. Load SQL Database :- pd.read_sql("SELECT * FROM table", connection)
# Example usage:
# df_sql = pd.read_sql(sql_query, db_connection)

print("JSON Import Syntax: pd.read_json('filepath.json')")
print("SQL Import Syntax:  pd.read_sql(query, connection)")
