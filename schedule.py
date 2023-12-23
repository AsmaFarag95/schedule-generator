"""
Schedule Generating file
Created by Gelovani Nodar
"""
import openpyxl as xl
from functions import yeardays, get_shiftset, Manager
import pandas as pd 
import os
   
 

def main(manager_file, yearInput, monthInput, teams_file):
 

    employees = pd.read_excel(manager_file)
    print(type(employees))

 

    managers = []

    # Store amount of rows in one variable
    max_row = len(employees)
    print(max_row)
    # Transfer information from Managers excel
#Sheet Names: Index(['Employee Name', 'Shift Type', 'Set', 'email'], dtype='object')

    for row in range(max_row):
        name = employees['Employee Name'].iloc[row]
        shift_type = employees['Shift Type'].iloc[row]
        mset = employees['Set'].iloc[row]
        email = employees['email'].iloc[row]
    # Now you can use these variables (name, shift_type, mset, email) as needed
   # Put Retreived info into the Manager class
        manager = Manager(name, shift_type, mset, email)
    # Append every manager into the managers List
        managers.append(manager)
    
    
    
    user_year = yearInput

    # Ask user to provide Year and Month
    while False:
      if user_year == None or type(user_year) != int():
        False
      else:
        True


    user_month = monthInput

    while False:
      if user_month == None or type(user_month) != int():
        False
      else:
        True 

# Now you have valid user input for year and month
    year = yearInput
    month = monthInput


# Generate set days of the given month of the given year
# Assign generated set-days to managers, which have the same set
 
    for manager in managers:
        for day in yeardays(year):
            if day.month == month and get_shiftset(day) == "Set 1" and manager.mset == 1:
                manager.shifts.append(day)
            elif day.month == month and get_shiftset(day) == "Set 2" and manager.mset == 2:
                manager.shifts.append(day)
                    # Change Python Date to Excel Date
    for manager in managers:
        for i in range(len(manager.shifts)):
            manager.shifts[i] = str(manager.shifts[i]).replace("-", "/")
                
                
                # Generate set days of the given month of the given year
# Assign generated set-days to managers, which have the same set
    
 
    team = pd.read_excel(teams_file)
    print("Sheet Names team  :", team.keys())

#Sheet Names team  : dict_keys(['Instructions', 'Shifts', 'Day Notes', 'Members'])
    Shifts = pd.read_excel(teams_file, sheet_name=1)
    Instructions = pd.read_excel(teams_file, sheet_name=0)
    DayNotes = pd.read_excel(teams_file, sheet_name=2)
    Members = pd.read_excel(teams_file, sheet_name=3)
  

    for manager in managers:
        amount = len(manager.shifts)

        for row in range(0, amount):

        # Append a new row to the DataFrame for each shift
            Shifts = Shifts._append({ # append method in panads is   _append searching for better solution "concat" maybe !! 
            'Member': manager.name,
            'Work Email': manager.email,
            'Shift Start Date': manager.shifts[row],
            'Shift End Date': manager.shifts[row],
            'Shift Start Time' :  '07:00',
            'Shift End Time' : '15:00',
            # Add more columns as needed
            'Shift Start Time': '07:00' if manager.shift_type.lower() == 'morning' else ('15:00' if manager.shift_type.lower() == 'afternoon' else '00:00'),
            'Shift End Time': '15:00' if manager.shift_type.lower() == 'morning' else ('23:00' if manager.shift_type.lower() == 'afternoon' else '07:00'),
            'Theme Color': '2. Blue' if manager.shift_type.lower() == 'morning' else ('3. Green' if manager.shift_type.lower() == 'afternoon' else '5. Pink'),
 
        }, ignore_index=True)
        
    Shifts.to_excel('TheShiftsDatasetOutput.xlsx', index=True)#create new file for the result

#Sheet Names team  : dict_keys(['Instructions', 'Shifts', 'Day Notes', 'Members'])
 
    team.to_sql("Instructions", 'sqlite:///TheShiftsDataset.sqlite', if_exists='replace', index=False)
    Shifts.to_sql("Shifts", 'sqlite:///TheShiftsDataset.sqlite', if_exists='replace', index=False)
    DayNotes.to_sql("Day Notes", 'sqlite:///TheShiftsDataset.sqlite', if_exists='replace', index=False)
    Members.to_sql("Members", 'sqlite:///TheShiftsDataset.sqlite', if_exists='replace', index=False)

import sqlite3

conn = sqlite3.connect('TheFrame.sqlite')

# List all tables in the database
cursor = conn.cursor()
cursor.execute('SELECT name FROM sqlite_master WHERE type="table";')
tables = cursor.fetchall()
print(tables)





'''
# Delete a specific table
table_name = "TTTT"  #I made this by mistake
cursor.execute('DROP TABLE {}'.format(table_name))

conn.commit()
conn.close()

conn = sqlite3.connect('TheFrame.sqlite')

# List all tables in the database
cursor = conn.cursor()
cursor.execute('SELECT name FROM sqlite_master WHERE type="table";')
tables = cursor.fetchall()
print(tables)

# Delete a specific table
table_name = "TTTT"  # Replace with the name of the table you want to delete
cursor.execute('DROP TABLE {}'.format(table_name))

conn.commit()
conn.close()'''

