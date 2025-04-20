import pandas as pd

# Task 1.1 create a dataframe from a dictionary
data1 = {
    "Name": ['Alice', 'Bob', 'charlie'],
    "Age": [25, 30, 35],
    "City": ['New York', 'Los Angeles', 'Chicago']
}

task1_data_frame = pd.DataFrame(data1)
print("\nOriginal DataFrame:")
print(task1_data_frame)

# Task 1.2: Add a new column
task1_with_salary = task1_data_frame.copy()
task1_with_salary['Salary'] = [70000, 80000, 90000]
print("\nDataFrame with Salary:")
print(task1_with_salary)

# Task 1.3 Modify an existing column
task1_older = task1_with_salary.copy()
task1_older['Age'] = task1_older['Age']+1
print("\nModified DataFrame with Age incremented by 1:")
print(task1_older)

# Task 1.4: save the Dataframe as a CVS file
task1_older.to_csv('employees.csv', index=False)

# -------------------------------------------------------------
# Task 2.1: Loading data from CSV and JSON
# Read data from a CSV file
task2_employees = pd.read_csv('employees.csv')
print('\nLoaded DataFrame from Enployee.csv')
print(task2_employees)

# Task 2.2: Read data from JSON file
additional_employees = pd.DataFrame(
    {
        "Name": ["Eve", "Frank"],
        "Age": [28, 40],
        "City": ["Miami", "Seattle"],
        "Salary": [60000, 95000],
    }
)
additional_employees.to_json(
    'additional_employees.json', orient="records", indent=4)
json_employees = pd.read_json("additional_employees.json")
# 2.3 Load the JSON file into a new DataFrame
more_employees = pd.concat(
    [task2_employees, json_employees], ignore_index=True)
print('\nMore:')
print(more_employees)

# Task 3.1: Data Inspection - Using Head, Tail, and Info Methods
# Use the head() method:
first_three = more_employees.head(3)
print("\nFirst three rows of more_employees:")
print(first_three)

# 3.2 Use the tail():
last_two = more_employees.tail(2)
print("\nLast 2 rows of more_employees:")
print(last_two)

# 3.3 Get the shape of a dataFrame
employee_shape = more_employees.shape
print("\nShape of the more_employees DataFrame:", employee_shape)

# 3.4: Get a concise summary using info()
print("\nSummary of the DataFrame:")
more_employees.info()

# Task 4: Data Cleaning:
# Task 4.1:
dirty_data = pd.read_csv('dirty_data.csv')
print('\nOriginal dirty Data:')
print(dirty_data)

clean_data = dirty_data.copy()

# Task 4.2: Remove Duplicate rows:
clean_data = clean_data.drop_duplicates()
print('\nRemove Duplicates:')
print(clean_data)

# Task 4.3: Convert Age
clean_data['Age'] = pd.to_numeric(clean_data["Age"], errors='coerce')
print('\nAge converted:')
print(clean_data)

# Taks 4.4: Convert Salary
clean_data["Salary"].replace(["unknown", "n/a"], pd.NA, inplace=True)
clean_data['Salary'] = pd.to_numeric(clean_data['Salary'], errors='coerce')
print('\nSalary converetd:')
print(clean_data)

# Task 4.5: Fill missing values in age and salary
mean_score = clean_data["Age"].mean()
clean_data["Age"] = clean_data["Age"].fillna(mean_score)
median_score = clean_data["Salary"].median()
clean_data["Salary"] = clean_data["Salary"].fillna(median_score)
print("\nDataFrame after filling missing Age Salary:")
print(clean_data)

# Task 4.6: Convert Hire Date to Datetime:
clean_data['Hire Date'] = pd.to_datetime(
    clean_data['Hire Date'], errors='coerce')
print("\nDataFrame with 'Hire Date' converted to datetime:")
print(clean_data)

# Task 4.7: Strip estra white space
clean_data['Name'] = clean_data["Name"].str.strip()
clean_data['Name'] = clean_data["Name"].str.upper()

clean_data['Department'] = clean_data['Department'].str.upper()
print('\nFinal Data:')
print(clean_data)
