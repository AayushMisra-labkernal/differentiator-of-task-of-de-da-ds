"""
DATA ENGINEER
=============
Role: Responsible for data storage and pipeline creation
Task: Store sales data into a file for further processing
"""

# Sales data to be stored
sales = [100, 120, 90, 150, 200]

# Open file in write mode
file = open("sales.txt", "w")

# Write each sale value to the file
for sale in sales:
    file.write(str(sale) + "\n")

# Close the file
file.close()

print("Data Stored Successfully")
