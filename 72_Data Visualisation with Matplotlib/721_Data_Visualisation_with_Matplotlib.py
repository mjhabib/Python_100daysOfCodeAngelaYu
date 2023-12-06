import pandas as pd
import matplotlib.pyplot as plt

# to create charts and graphs alongside with pandas

# List of column names to use. If the file contains a header row, then you should explicitly pass header=0 to override the column names. Duplicates in this list are not allowed.
df = pd.read_csv("721_StackExchange_QueryResults.csv", header=0, names=['DATE', 'TAG', 'POSTS'])

print(f"\n {df.head()}")  # first five rows

print(f"\n {df.tail()}")  # last five rows

print(f"\n {df.shape}")  # (2496, 3)  ->  number of rows and columns

print(f"\n {df.count()}")  # the number of entries in each column

print(
    f"\n {df.groupby('TAG').sum()}")  # how many posts each programming language had since the creation of Stack Overflow

print(f"\n {df.groupby('TAG').count()}")  # how many months of entries exist per programming language

# convert str to datetime
print(f"\n {type(df['DATE'][1])}")  # <class 'str'>
date_time = pd.to_datetime(df['DATE'])  # only this column
print(f"\n {type(date_time[1])}")  # <class 'pandas._libs.tslibs.timestamps.Timestamp'>

df.DATE = pd.to_datetime(df.DATE)  # convert entire column
print(f"\n {df.head()}")

# The .pivot() method
reshaped_df = df.pivot(index='DATE', columns='TAG', values='POSTS')
print(f"\n {reshaped_df.tail()}")
print(f"\n {reshaped_df.shape}")
print(f"\n {reshaped_df.columns}")
print(f"\n {reshaped_df.count()}")

# Dealing with NaN Values:
# In this case, we don't want to drop the rows that have a NaN value. Instead, we want to substitute the number 0 for each NaN value in the DataFrame. We can do this with the .fillna() method.
reshaped_df = reshaped_df.fillna(0)
print(f"\n {reshaped_df.head()}")

# check if there are any NaN values left in the entire DataFrame
print(f"\n {reshaped_df.isna().values.any()}")  # False

# Matplotlib
# I moved the codes to Google Colab for better understanding
