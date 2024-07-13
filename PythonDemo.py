# Part 1:
# Generated data is stored in users.csv file.

# Part 2:
import pandas as pd

# This block prints the actual content of the csv file to the terminal
# First we read the CSV file into a pandas DataFrame (df)
# Then we set the display options by enforcing a maximum number of columns to be displayed in the terminal
# In that way, I ensure that all columns are printed out
users = "./users.csv"
df = pd.read_csv(users)
pd.options.display.max_columns = len(df.columns)
print("----------------------------------")
print("Users Table:")
print("----------------------------------")
print(df)
print()

