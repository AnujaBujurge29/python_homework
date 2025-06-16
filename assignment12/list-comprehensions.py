import pandas as pd

# Task 3.1: Read CSV file into DataFrame
df = pd.read_csv('../csv/employees.csv')

# Task 3.2: Create list of full names using list comprehension
full_names = [f"{row['first_name']} {row['last_name']}" for _,
              row in df.iterrows()]
print("All employee names:")
print(full_names)

# Task 3.3: Create list of names containing 'e'
names_with_e = [name for name in full_names if 'e' in name.lower()]
print("\nNames containing 'e':")
print(names_with_e)
