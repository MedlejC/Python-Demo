# Python Demo

<p align="center"> 
<img src="https://skillicons.dev/icons?i=python,vscode"/>
</p>

### Tip: Press " . " (dot) key on your keyboard to open Github's built-in web-based editor.

## Usage:
- Clone the Repository
  ```bash
  git clone https://github.com/MedlejC/Python-Demo.git
  ```
- Navigate to the Project Directory
  ```bash
  cd Python-Demo
  ```
- Activate your Virtual Environment:
  ```bash
  python3 -m venv venv
  source venv/bin/activate # for macOS and Linus
  # OR
  .\venv\Scripts\activate # for Windows
  ```
- Install the Required Packages:
  ```bash
  pip install -r requirements.txt
  ```
  I kept my requirements.txt file updated throughout this progress by using  
  `pip freeze > requirements.txt`
- Run the code:
  ```bash
  python PythonDemo.py
  ```

## Generating Data:

As a first step, I generated a random sample of data that consists of 30 entries, using ChatGPT.

<img width="630" alt="image" src="https://github.com/user-attachments/assets/67a93ed6-9df0-4cd9-8797-af1b7e61d5ee">

## Reading data from CSV file:

### 1- Setting up the environment:

- I had to set up venv to properly use Python on my machine (Macbook Air M1, tool: Microsoft Visual Studio Code)
  ```bash
      python3 -m venv venv
      source venv/bin/activate
      pip install pandas
  ```
- To deactivate it, simply run: `deactivate`.
- To reactivate it: `source venv/bin/activate`.  
  The code successfully reads and prints the content of users.csv to the terminal:

  <br></br>
  <img width="630" alt="image" src="https://github.com/user-attachments/assets/a209260b-c26e-43ed-a2c7-166cbd2d7c82">

### 2-a. Number of Active Users:

- I used the pandas.DataFrame.loc method to filter the table for an Active Status.
  loc enables me to access a group of rows and columns by labels.
  ```bash
  active_users = df.loc[df['Status'] == 'Active']
  ```

### 2-b. Percentage of Female Users:

- Similar filtering approach to part 2.a
- To calculate the percentage of females, I used this equation:  
  `(# of Females / Total # of Users) * 100`

### 2-c. Age Groups:

- As an initial step, I defined the age groups that I want to use (age_bins & age_labels)
  **Age Labels should always be smaller than the bins by 1.**  
  Ex: If I want to create 2 age groups: Below 50 and Above 50,  
  I use: `age_bins = [0, 50, 100]`  
  and `age_labels = ['Below 50', 'Above 50']`  
  The groups would then be divided from 0-49, and 50-100 (Assuming right = False --> Left-Inclusive interval)
- Once age groups are set, I can categorize the ages into the defined groups by using:
  ```bash
  df['Age Group'] = pd.cut(df['Age'], bins=age_bins, labels=age_labels)
  ```
  This creates a new Column, `Age Group`, in my original table, and categorizes the ages into the bins defined by `age_bins`, and labels them with `age_labels`
- As a final step, I group my table by the `Age Group` column I had just created and count the number of users in each group:
  ```bash
  age_group_count = df.groupby('Age Group').size()
  ```

### 4. Bar Chart:

- To be able to create a chart, I had to install matplotlib:
  ```bash
  pip install matplotlib
  ```
- Once installed and imported, I could use its `bar` built-in function,  
  and set x-axis to the `age_labels` that I previously defined  
  and the y-axis to `age_group_count`
- Final result:  
  <img width="630" alt="image" src="https://github.com/user-attachments/assets/4dd39bb1-f497-4133-86ef-77982662d0bc">

## Different CSV files:
- I came up with an idea to generate more csv files, each with a specific characteristic, and test my code output respectively:
    - `users_higher_Active_freq.csv`: I asked chatGPT to generate another dataset but with a higher frequency for active users.
    - `users_higher_Male_freq.csv`: I asked chatGPT to generate another dataset but with a higher frequency for Male users.
    - `users_higher_Age_randomness.csv`: I asked chatGPT to generate another dataset but with higher Age randomness between users.
- For example, when using the file with **Higher Age Randomness**, here is how the final plot looks like:
  <img width="630" alt="image" src="https://github.com/user-attachments/assets/740ca68b-b454-4e73-8bc4-0843e0442e02">
- Feel free to test any of these files by uncommenting the corresponding line at the beginning of the code.

## Resources:

- https://stackoverflow.com/questions/54106071/how-can-i-set-up-a-virtual-environment-for-python-in-visual-studio-code
- https://www.geeksforgeeks.org/ways-to-filter-pandas-dataframe-by-column-values/
- https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html
- https://www.python4data.science/en/24.1.0/workspace/pandas/discretisation.html
- https://www.geeksforgeeks.org/bar-plot-in-matplotlib/
