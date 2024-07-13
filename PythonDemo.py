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

# Part 2-a:
# This block filters the data where 'Status' column equals 'Active'
active_users = df.loc[df['Status'] == 'Active']
print("----------------------------------")
print("Active Users:")
print("----------------------------------")
print(active_users)

# Number of active users:
print("\nNumber of Active Users: ", len(active_users))
print()

# Part 2-b:
# This block filters the data where 'Gender' column equals 'Female'
female_users = df.loc[df['Gender'] == 'Female']
print("----------------------------------")
print("Female Users:")
print("----------------------------------")
print(female_users)

# Percentage of female users:
percentage_female = (len(female_users)/len(df))*100
print("\nPercentage of Female Users: ",percentage_female)
print()

# Part 2-c:
# This blocks define the age groups and their corresponding labels
age_bins = [0,20,30,40,50,60,70,80,90,100]
age_labels = ['0-20', '21-30', '31-40', '41-50', '51-60', '61 70', '71-80', '81-90', '91-100']

# Adding a new column (Age Group) that categorizes the ages into the bins defined, with their corresponding labels
df["Age Group"] = pd.cut(df['Age'], bins=age_bins, labels=age_labels)

# Then, I can count the number of users in each age group
age_group_count = df.groupby("Age Group").size()
print(age_group_count)


# Part 4 - Bar Chart
import matplotlib.pyplot as plt

plt.bar(age_labels, age_group_count)
plt.title('Distribution of Users by Age Group')
plt.xlabel('Age Groups')
plt.ylabel('Number of Users')
plt.xticks(rotation=45)
plt.show()