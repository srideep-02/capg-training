# import pandas as pd
# file = open("./Day12/csvgen.csv","a+")
# num = int(input("Enter no of employees:"))
# data = []
# for i in range(num):
# 	name = input("Enter the name of employee: ")
# 	age = input("Enter the age of employee: ")
# 	salary = input("Enter the salary of employee: ")
# 	data.append([name,age,salary])

# for i in data:
# 	# file.write(",".join(i) + "\n")

# file.close()

# df = pd.read_csv("./Day12/csvgen.csv", names=['Name','Age','Salary'])

# print(df)

import pandas as pd

file=open("./pythonn/day12/.csv","a+")
num=int(input("Enter the no of employees"))
data=[]

for i in range(num):
    name=input("Enter name :")
    age=input("Enter age:")
    salary=input("Enter salary :")
    data.append([name,age,salary])
    
for i in data:
    file.write(",".join(i) + "\n")
    
file.close()
dff=pd.DataFrame(data)
csv_filename = "data.csv"
dff.to_csv(csv_filename, index=False)
print(f"Filename :{csv_filename} sreated successfully")
print("Employees data from csv")
dff_read=pd.read_csv(csv_filename)
print(dff_read)


df=pd.read_csv("./day12/gen.csv",names=['name','age','salary'])
print(df)


# import pandas as pd

# # Step 1: Create an empty list to store employee data
# employees = []

# # Step 2: Ask the user how many employees they want to enter
# num_employees = int(input("Enter the number of employees: "))

# # Step 3: Collect employee details using a loop
# for i in range(num_employees):
#     print(f"\nEnter details for Employee {i+1}:")
#     emp_id = input("Employee ID: ")
#     first_name = input("First Name: ")
#     last_name = input("Last Name: ")
#     age = int(input("Age: "))
#     department = input("Department: ")
    
#     # Append data to the list as a dictionary
#     employees.append([emp_id,first_name,last_name,age,department])

# # Step 4: Convert the list to a DataFrame
# df = pd.DataFrame(employees)

# # Step 5: Save to CSV
# csv_filename = "employees.csv"
# df.to_csv(csv_filename, index=False)

# print(f"\nCSV file '{csv_filename}' created successfully!")

# # Step 6: Read and Display the CSV File
# print("\nEmployee Data from CSV:")
# df_read = pd.read_csv(csv_filename)
# print(df_read)














# #creating a dataset for taking the input of the employess and creating a csv file and reading it