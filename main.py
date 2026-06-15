"""
MAIN ORCHESTRATION SCRIPT
==========================
This script demonstrates the complete workflow of:
1. Data Engineer - Storing data
2. Data Analyst - Analyzing data
3. Data Scientist - Predicting data
"""

print("=" * 60)
print("DEMONSTRATING ROLES: DATA ENGINEER, ANALYST & SCIENTIST")
print("=" * 60)

# ==================== DATA ENGINEER ====================
print("\n[1] DATA ENGINEER - Storing sales data...")
print("-" * 60)

sales = [100, 120, 90, 150, 200]

file = open("sales.txt", "w")

for sale in sales:
    file.write(str(sale) + "\n")

file.close()

print("✓ Data Stored Successfully")

# ==================== DATA ANALYST ====================
print("\n[2] DATA ANALYST - Analyzing sales data...")
print("-" * 60)

file = open("sales.txt", "r")

sales = []

for line in file:
    sales.append(int(line))

file.close()

average = sum(sales) / len(sales)

print(f"✓ Average Sale = {average}")
print(f"✓ Highest Sale = {max(sales)}")
print(f"✓ Lowest Sale = {min(sales)}")

# ==================== DATA SCIENTIST ====================
print("\n[3] DATA SCIENTIST - Predicting next sale...")
print("-" * 60)

growth = sales[-1] - sales[-2]

prediction = sales[-1] + growth

print(f"✓ Predicted Next Sale = {prediction}")

print("\n" + "=" * 60)
print("WORKFLOW COMPLETED!")
print("=" * 60)
