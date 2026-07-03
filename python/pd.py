import pandas as pd

s=pd.Series([10,20,30])
print(s)

# ## 🐼 **What is Pandas?**

# # Pandas is a **powerful library for data analysis**. It provides:

# # * `DataFrame`: A 2D table-like structure (like a table in Excel).
# # * `Series`: A 1D array-like structure (one column).
# # * Tools for data cleaning, filtering, and analysis.



# ## ⚡️ **1️⃣ Install and Import Pandas**

# # Install
# # pip install pandas

# # Import
# # import pandas as pd


# ## 🔥 **2️⃣ Creating Series and DataFrames**

# #### Series

import pandas as pd

# Creating a Series
s = pd.Series([10, 20, 30, 40])
print(s)

# Creating a Series with custom index
s = pd.Series([100, 200, 300], index=['a', 'b', 'c'])
print(s)

#### DataFrame

# Creating a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['Delhi', 'Mumbai', 'Bangalore']
}
df = pd.DataFrame(data)

print(df)


## 📋 **3️⃣ Viewing and Inspecting the Data**

# First 5 rows
print(df.head())

# Last 5 rows
print(df.tail())

# Columns
print(df.columns)

# Info about data types
print(df.info())

# Statistical summary
print(df.describe())


## 👇 **4️⃣ Selecting and Indexing**

# Selecting a column
print(df['Name'])
print(df.Name)

# Selecting multiple columns
print(df[['Name','Age']])

# Selecting by position
print(df.iloc[0])           # First row
print(df.iloc[0, 1])        # First row, second column
print(df.iloc[0:2, 1:3])    # First two rows, columns 1–2

# Selecting by label
print(df.loc[0])            # First row
print(df.loc[0, 'Name'])    # Name of first person
print(df.loc[0:1, ['Name','City']]) 


## 🛠️ **5️⃣ Adding and Modifying Columns**

# Add a new column
df['Country'] = 'India'
print(df)

# Modify an existing column
df['Age'] = df['Age'] + 1
print(df)

# Drop a column
df = df.drop(columns=['Country'])


## 🗂️ **6️⃣ Filtering and Conditional Selection**

# Get people older than 30
print(df[df['Age'] > 30])

# Multiple conditions
print(df[(df['Age'] > 25) & (df['City'] == 'Mumbai')])


## 🔥 **7️⃣ Sorting and Grouping**

# Sort by Age
print(df.sort_values(by='Age'))

# Group by City
print(df.groupby('City')['Age'].mean())

## 🐞 **8️⃣ Handling Missing Data**

data = {'Name': ['Alice','Bob','Charlie'], 'Age': [25, None, 35]}
df = pd.DataFrame(data)

# Check for null values
print(df.isnull())

# Fill null values
df['Age'] = df['Age'].fillna(df['Age'].mean())

# Drop rows with null
df = df.dropna()


## 💾 **9️⃣ Reading and Writing Files**

# Read a CSV
# df = pd.read_csv('filename.csv')

# # Read an Excel file
# df = pd.read_excel('filename.xlsx')

# # Export to CSV
# df.to_csv('new_file.csv', index=False)

# # Export to Excel
# df.to_excel('new_file.xlsx', index=False)


## ⚡️ **10️⃣ Advanced Techniques**

#### Applying a function

# Apply a custom function
def add_five(x): return x + 5
df['Age'] = df['Age'].apply(add_five)


#### Merging and Joining

df1 = pd.DataFrame({'ID': [1,2], 'Name': ['Alice','Bob']})
df2 = pd.DataFrame({'ID': [1,2], 'City': ['Delhi','Mumbai']})
merged = pd.merge(df1, df2, on='ID')
print(merged)

# #### Pivot Table

# table = df.pivot_table(index='City', values='Age', aggfunc='mean')
# print(table)

import pandas as pd

# Creating a Series of temperatures
temperatures = pd.Series([22.5, 25.0, 27.3, 30.1, 28.4], name="Temp", index=False)

# Display the Series
print(temperatures)


import pandas as pd

# Creating the DataFrame
data = {
    "Product": ["Laptop", "Smartphone", "Headphones", "Keyboard", "Mouse"],
    "Price": [1200, 800, 150, 60, 25],
    "Stock": [5, 12, 30, 25, 100]
}

df = pd.DataFrame(data)

# Display the DataFrame
print(df.to_string(index=False))



import pandas as pd

# Sample data
data = {
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Ethan"],
    "Age": [25, 30, 35, 28, 40],
    "City": ["New York", "Paris", "London", "Tokyo", "Sydney"]
}
df = pd.DataFrame(data)

# 1️⃣ Select only the Name column
print("Names:\n", df["Name"])

# 2️⃣ Select the first 3 rows using .iloc
print("\nFirst 3 rows:\n", df.iloc[:3])

# 3️⃣ Select people older than 30
print("\nPeople older than 30:\n", df[df["Age"] > 30])


