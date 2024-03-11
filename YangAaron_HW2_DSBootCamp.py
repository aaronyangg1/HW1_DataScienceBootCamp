import numpy as np
import pandas as pd

#1) From df filter the 'Manufacturer', 'Model' and 'Type' for every 20th row starting from 1st (row 0).
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
filtered_df = df.iloc[::20, 0:3] # Filter the desired columns ('Manufacturer', 'Model', and 'Type') for every 20th row
print(filtered_df)

#2) Replace missing values in Min.Price and Max.Price columns with their respective mean (check documentation).
min_price_mean = df["Min.Price"].mean()
max_price_mean = df["Max.Price"].mean()

df["Min.Price"] = df["Min.Price"].fillna(min_price_mean)
df["Max.Price"] = df["Max.Price"].fillna(max_price_mean)
print(df["Min.Price"])
print(df["Max.Price"])
#3) How to get the rows of a dataframe with row sum > 100?
df1 = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))
print(df1)
row_sums = df1.sum(axis=1)
filtered_df = df1[row_sums>100]
print(filtered_df)

#4)Create a 4x4 NumPy array filled with random integers between 1 and 100.
#Then, reshape this array into two separate 2D arrays, 
#where one represents the rows and the other represents the columns. 
#Write a function, preferably using a lambda function, 
#to calculate the sum of each row and each column separately, 
#and return the results as two separate NumPy arrays
df2 = pd.DataFrame(np.random.randint(1, 101, size = (4,4)))
sum_rows = np.apply_along_axis(lambda row: np.sum(row), axis=1, arr=df2)
sum_columns = np.apply_along_axis(lambda col: np.sum(col), axis=0, arr=df2)
print("Original 4x4 array:")
print(df2)
print("\nsum of each row:")
print(sum_rows)
print("\nsum of each column:")
print(sum_columns)