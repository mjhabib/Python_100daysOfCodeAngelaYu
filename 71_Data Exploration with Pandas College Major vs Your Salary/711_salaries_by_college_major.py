import pandas as pd

df = pd.read_csv('711_salaries_by_college_major.csv')

print(df.head())  # peek at the top 5 rows of our dataframe.

print(f"\n{df.shape}")  # (51, 6)  ->  number of rows and columns

print(f"\n{df.columns}")  # column names

print(f"\n{df.isna()}")  # NaN (not a number) values

print(f"\n{df.tail()}")  # Check the last couple of rows in the dataframe

# row 50 was bad, so we're going to delete it (we're not messing with original csv file)
clean_df = df.dropna()
clean_df.tail()
print(f"\n{clean_df.tail()}")

print(f"\n{clean_df['Starting Median Salary']}")  # print a column

print(f"\n{clean_df['Starting Median Salary'].max()}")  # the highest starting salary

print(f"\n{clean_df['Starting Median Salary'].idxmax()}")  # the index of the highest starting salary

print(f"\n{clean_df['Undergraduate Major'].loc[43]}")  # the name of the major that corresponds to that particular row

print(f"\n{clean_df['Undergraduate Major'][43]}")  # same result

print(f"\n{clean_df.loc[43]}")  # entire row

# assignment
print(f"\n{clean_df['Mid-Career 10th Percentile Salary'].idxmax()}")
print(
    f"\n The highest mid-career salary: '{clean_df['Undergraduate Major'][8]}' with '${clean_df['Mid-Career 10th Percentile Salary'].loc[8]}'")
# ---
print(f"\n{clean_df['Starting Median Salary'].idxmin()}")
print(
    f"\n The lowest starting salary: '{clean_df['Undergraduate Major'][49]}' with '${clean_df['Starting Median Salary'].loc[49]}'")
# ---
print(f"\n{clean_df['Mid-Career Median Salary'].idxmin()}")
print(
    f"\n The lowest mid-career salary: '{clean_df['Undergraduate Major'][18]}' with '${clean_df['Mid-Career Median Salary'].loc[18]}'")

# Lowest Risk Majors:
lower_risk = clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']
print(f"\n {lower_risk}")
# or
lower_risk_method2 = clean_df['Mid-Career 90th Percentile Salary'].subtract(
    clean_df['Mid-Career 10th Percentile Salary'])
print(f"\n {lower_risk_method2}")
# inserting the output into our current DF:
clean_df.insert(1, 'Spread', lower_risk)
print(f"\n {clean_df.head()}")

# sorting top degrees that have the smallest spread
low_risk = clean_df.sort_values('Spread')
print(f"\n Low top 5: {low_risk[['Undergraduate Major', 'Spread']].head()}")

# top 5 degrees with the highest values in the 90th percentile
print(f"\n High top 5: {clean_df.sort_values('Mid-Career 90th Percentile Salary', ascending=False).head()}")

# Majors with the Greatest Spread in Salaries
highest_spread = clean_df.sort_values('Spread', ascending=False)
print(f"\n {highest_spread[['Undergraduate Major', 'Spread']].head()}")

# count how many majors we have in each category
print(f"\n {clean_df.groupby('Group').count()}")


# summery:

# Use .head(), .tail(), .shape and .columns to explore your DataFrame and find out the number of rows and columns as well as the column names.
#
# Look for NaN (not a number) values with .findna() and consider using .dropna() to clean up your DataFrame.
#
# You can access entire columns of a DataFrame using the square bracket notation: df['column name'] or df[['column name 1', 'column name 2', 'column name 3']]
#
# You can access individual cells in a DataFrame by chaining square brackets df['column name'][index] or using df['column name'].loc[index]
#
# The largest and smallest values, as well as their positions, can be found with methods like .max(), .min(), .idxmax() and .idxmin()
#
# You can sort the DataFrame with .sort_values() and add new columns with .insert()
#
# To create an Excel Style Pivot Table by grouping entries that belong to a particular category use the .groupby() method
