
import csv
import traceback
import os
import custom_module
from datetime import datetime

# Task 10
def get_this_value():
    return os.getenv('THISVALUE')

# Task 11
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)
    
# Task 2
print('------------------------Task 2-------------------------------------------------------')
def read_employees():
    employees_data = {"fields": [], "rows": []}
    try:
        with open("../csv/employees.csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader):
                if index == 0:
                    employees_data["fields"] = row  
                else:
                    employees_data["rows"].append(row) 
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = [
            f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}'
            for trace in trace_back
        ]
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        return None  
    return employees_data

# # Call function and store result in global variable
employees = read_employees()
print(employees)

#Task 3
print('------------------------Task 3-------------------------------------------------------')
def column_index(column_name):
    try:
        return employees["fields"].index(column_name)
    except ValueError:
        print(f"Column '{column_name}' not found.")
        return None

# Call function and store result in global variable
employees = read_employees()
print(employees)

# # Get column index for 'employee_id'
employee_id_column = column_index("employee_id")
print(f"Employee ID Column Index: {employee_id_column}")

# Task 4
print('------------------------Task 4-------------------------------------------------------')
def first_name(row_number):
    first_name_col = column_index("first_name")
    if first_name_col is not None and 0 <= row_number < len(employees["rows"]):
        return employees["rows"][row_number][first_name_col]
    else:
        print("Invalid row number or column not found.")
        return None

# # Call function and store result in global variable
employees = read_employees()

# # Get column index for 'employee_id'
employee_id_column = column_index("employee_id")
print(f"Employee ID Column Index: {employee_id_column}")

# Task 5
print('------------------------Task 5-------------------------------------------------------')
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    
    matches = list(filter(employee_match, employees["rows"]))
    return matches

# Call function and store result in global variable
employees = read_employees()
print(employees)

# # Get column index for 'employee_id'
employee_id_column = column_index("employee_id")
print(f"Employee ID Column Index: {employee_id_column}")

#Task 6
print('------------------------Task 6-------------------------------------------------------')
def employee_find_2(employee_id):
    matches = list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]))
    return matches

# # Call function and store result in global variable
employees = read_employees()
print(employees)

# # Get column index for 'employee_id'
employee_id_column = column_index("employee_id")
print(f"Employee ID Column Index: {employee_id_column}")

# Task 7
print('------------------------Task 7-------------------------------------------------------')
def sort_by_last_name():
    last_name_col = column_index("last_name")
    if last_name_col is not None:
        employees["rows"].sort(key=lambda row: row[last_name_col])
    return employees["rows"]

# Call function and store result in global variable
employees = read_employees()
print(employees)

# Get column index for 'employee_id'
employee_id_column = column_index("employee_id")
print("Employee ID Column Index: {employee_id_column}")

# Sort employees by last name
sorted_employees = sort_by_last_name()
print("Sorted Employees:", sorted_employees)

# Task 8
# Test employee_dict function
print('------------------------Task 8-------------------------------------------------------')
def employee_dict(row):
    emp_dict = {key: value for key, value in zip(employees["fields"], row) if key != "employee_id"}
    return emp_dict

if employees["rows"]:
    test_employee = employee_dict(employees["rows"][0])
    print("Test Employee Dict:", test_employee)

# Task 9
print('------------------------Task 9-------------------------------------------------------')
def all_employees_dict():
    emp_dicts = {row[employee_id_column]: employee_dict(row) for row in employees["rows"]}
    return emp_dicts

all_employees = all_employees_dict()
print("All Employees Dict:", all_employees)

# Task 10
print('------------------------Task 10-------------------------------------------------------')
def get_this_value():
    return os.getenv('THISVALUE')

this_value = get_this_value()
print(f"The value of THISVALUE is: {this_value}")

# Task 11:
print('------------------------Task 11-------------------------------------------------------')
set_that_secret("new_secret_value")
print(custom_module.secret)  

# Task 12:
print('------------------------Task 12-------------------------------------------------------')

# Helper function to read a CSV file and return a dictionary with fields and rows
def read_csv_to_dict(file_path):
    data = {"fields": [], "rows": []}
    try:
        with open(file_path, "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader):
                if index == 0:
                    data["fields"] = row 
                else:
                    data["rows"].append(tuple(row))  
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = [
            f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}'
            for trace in trace_back
        ]
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        return None
    return data

# Function to read both minutes1.csv and minutes2.csv
def read_minutes():
    minutes1 = read_csv_to_dict("../csv/minutes1.csv")
    minutes2 = read_csv_to_dict("../csv/minutes2.csv")
    return minutes1, minutes2
minutes1, minutes2 = read_minutes()
print("Minutes1 Data:", minutes1)
print("Minutes2 Data:", minutes2)

# Task 13:
print('------------------------Task 13-------------------------------------------------------')

def create_minutes_set():
    set_minutes1 = set(minutes1["rows"])
    set_minutes2 = set(minutes2["rows"])
    combined_set = set_minutes1.union(set_minutes2)
    return combined_set
minutes_set = create_minutes_set()
print("Combined Minutes Set:", minutes_set)

# Task 14:
print('------------------------Task 14-------------------------------------------------------')

def create_minutes_list():
    minutes_list = list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_set))
    return minutes_list
minutes_list = create_minutes_list()
print("Minutes List with datetime objects:", minutes_list)

# Task 15:
print('------------------------Task 15-------------------------------------------------------')

# Function to write out the sorted list to a CSV file
def write_sorted_list():
    sorted_minutes = sorted(minutes_list, key=lambda x: x[1])
    formatted_minutes = list(map(lambda x: (x[0], x[1].strftime("%B %d, %Y")), sorted_minutes))
    try:
        with open('./minutes.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(minutes1["fields"])
            writer.writerows(formatted_minutes)
        return formatted_minutes  
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")
        return None
sorted_minutes_list = write_sorted_list()
print("Sorted Minutes List Written to File:", sorted_minutes_list)