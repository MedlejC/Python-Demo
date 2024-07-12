# Part 1:
# Generated data is stored in users.csv file.

# Part 2:
import pandas as pd

users = "./users.csv"
df = pd.read_csv(users)
pd.options.display.max_columns = len(df.columns)
print(df)