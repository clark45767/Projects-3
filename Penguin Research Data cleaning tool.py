# Penguin Research Data Cleaning Tool
 
# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
 
# Load Seaborn's built-in Penguins dataset
df = sns.load_dataset("penguins")
 
# Display the first 10 rows
print("Original Penguin Dataset:")
print(df.head(10))
 
 
# ---------------------------------
# PART 1: Detect Missing Values
# ---------------------------------
 
print("\nAre missing values present?")
print(df.isnull().any())
 
print("\nTotal missing values in each column:")
print(df.isnull().sum())
 
 
# ---------------------------------
# PART 2: Visualize Missing Values
# ---------------------------------
 
plt.figure(figsize=(10, 6))
 
sns.heatmap(
    df.isnull(),
    cbar=False,
    cmap="viridis"
)
 
plt.title("Missing Values in the Penguins Dataset")
plt.xlabel("Dataset Columns")
plt.ylabel("Penguin Records")
plt.show()
 
 
# ---------------------------------
# PART 3: Remove Empty Records
# ---------------------------------
 
# Remove rows where every value is missing
df = df.dropna(how="all")
 
print("\nDataset after removing completely empty rows:")
print(df.head())
 
 
# ---------------------------------
# PART 4: Handle Categorical Values
# ---------------------------------
 
categorical_columns = [
    "species",
    "island",
    "sex"
]
 
for column in categorical_columns:
    most_common_value = df[column].mode()[0]
 
    df[column] = df[column].fillna(
        most_common_value
    )
 
 
# ---------------------------------
# PART 5: Handle Numerical Values
# ---------------------------------
 
numerical_columns = [
    "bill_length_mm",
    "bill_depth_mm",
    "flipper_length_mm",
    "body_mass_g"
]
 
# Estimate values between existing measurements
df[numerical_columns] = (
    df[numerical_columns]
    .interpolate()
)
 
# Fill any remaining values at the beginning or end
df[numerical_columns] = (
    df[numerical_columns]
    .bfill()
    .ffill()
)
 
 
# ---------------------------------
# PART 6: Check the Cleaned Dataset
# ---------------------------------
 
print("\nMissing values after data cleaning:")
print(df.isnull().sum())
 
print("\nCleaned Penguin Dataset:")
print(df.head(10))
 
# Optional: create a dataset containing only complete rows
complete_penguins = df.dropna()
 
print("\nNumber of complete penguin records:")
print(len(complete_penguins))
