# Differentiator of Tasks: Data Engineer vs Data Analyst vs Data Scientist

This is an **introductory project** to understand the **basic tasks** of:
- 🛠️ **Data Engineer**
- 📊 **Data Analyst**
- 🤖 **Data Scientist**

## Overview

Each role has distinct responsibilities in the data pipeline:

### 1. Data Engineer (`data_engineer.py`)
**Responsibility:** Data Storage & Pipeline Creation

```python
sales = [100, 120, 90, 150, 200]

file = open("sales.txt", "w")

for sale in sales:
    file.write(str(sale) + "\n")

file.close()

print("Data Stored Successfully")
```

- ✓ Collects raw data
- ✓ Stores data in files/databases
- ✓ Creates data pipelines
- ✓ Ensures data quality and accessibility

### 2. Data Analyst (`data_analyst.py`)
**Responsibility:** Data Analysis & Insights Generation

```python
file = open("sales.txt", "r")

sales = []

for line in file:
    sales.append(int(line))

file.close()

average = sum(sales) / len(sales)

print("Average Sale =", average)
print("Highest Sale =", max(sales))
print("Lowest Sale =", min(sales))
```

- ✓ Reads data from storage
- ✓ Analyzes data for patterns
- ✓ Generates statistical insights
- ✓ Creates reports and visualizations

### 3. Data Scientist (`data_scientist.py`)
**Responsibility:** Predictive Modeling & Forecasting

```python
growth = sales[-1] - sales[-2]

prediction = sales[-1] + growth

print("Predicted Next Sale =", prediction)
```

- ✓ Builds predictive models
- ✓ Uses statistical analysis
- ✓ Forecasts future trends
- ✓ Provides data-driven recommendations

## How to Run

### Run Individual Scripts:
```bash
python data_engineer.py
python data_analyst.py
python data_scientist.py
```

### Run Complete Workflow:
```bash
python main.py
```

## Sample Output

```
============================================================
DEMONSTRATING ROLES: DATA ENGINEER, ANALYST & SCIENTIST
============================================================

[1] DATA ENGINEER - Storing sales data...
------------------------------------------------------------
✓ Data Stored Successfully

[2] DATA ANALYST - Analyzing sales data...
------------------------------------------------------------
✓ Average Sale = 132.0
✓ Highest Sale = 200
✓ Lowest Sale = 90

[3] DATA SCIENTIST - Predicting next sale...
------------------------------------------------------------
✓ Predicted Next Sale = 250

============================================================
WORKFLOW COMPLETED!
============================================================
```

## Key Differences

| Aspect | Data Engineer | Data Analyst | Data Scientist |
|--------|--------------|--------------|----------------|
| **Focus** | Data Storage & Infrastructure | Descriptive Analysis | Predictive Modeling |
| **Tools** | Databases, ETL, Pipelines | Excel, SQL, BI Tools | Python, ML, Statistics |
| **Output** | Clean Data | Insights & Reports | Predictions & Models |
| **Questions** | "How to store this data?" | "What happened?" | "What will happen?" |

---

**Created by:** AayushMisra-labkernal  
**Purpose:** Learning the fundamentals of data roles
