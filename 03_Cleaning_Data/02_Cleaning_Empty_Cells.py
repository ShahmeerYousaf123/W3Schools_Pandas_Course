# Pandas - Cleaning Empty Cells 

# Empty Cells
''' Empty cells can potentially give you a wrong result when you analyze data. '''

# Remove Rows
''' One way to deal with empty cells is to remove rows that contain empty cells.
This is usually OK, since data sets can be very big, and removing a few rows will not have 
a big impact on the result. '''
# Example
# Return a new DataFrame with no empty cells
import pandas as pd
df = pd.read_csv('data2.csv')
new_df = df.dropna()
print(new_df.to_string())

print('-----------------------------------')

""" Note: By default, the dropna() method returns a new DataFrame, and will not change the original. """
''' If you want to change the original DataFrame, use the inplace = True argument. '''
# Example
# Remove all rows with NULL values
import pandas as pd
df = pd.read_csv('data2.csv')
df.dropna(inplace = True)
print(df.to_string())

print('-----------------------------------')

""" Note: Now, the dropna(inplace = True) will NOT  return a new DataFrame, but it will remove all rows 
containing NULL values from the original DataFrame. """

# Replace Empty Values
''' Another way of dealing with empty cells is to insert a new value instead. 
This way you do not have to delete entire rows just because of some empty cells.

The fillna() method allows us to replace empty cells with a value. '''
# Example
# Replace NULL values with the number 130
import pandas as pd
df = pd.read_csv('data2.csv')
df.fillna(130, inplace = True)
print(df.to_string())

print('-----------------------------------')

# Replace Only For Specified Columns
''' The example above replaces all empty cells in the whole DataFrame. 
To only replace empty values for one column, specify the column name for the DataFrame. '''
# Example
# Replace NULL values in the "Calories" columns with the number 130
import pandas as pd
df = pd.read_csv('data2.csv')
df.fillna({"Calories": 130}, inplace = True)
print(df.to_string())

print('-----------------------------------')

# Replace Using Mean, Median, or Mode
''' A common way to replace empty cells, is to calculate the mean, median or mode value of the column.
Pandas uses the mean(), median() and mode() methods to calculate the respective values for a specified column. '''
# Example
# Calculate the MEAN and replace any empty values with it
import pandas as pd
df = pd.read_csv('data2.csv')
x = df["Calories"].mean()
df.fillna({"Calories": x}, inplace = True)
print(df.to_string())

print('-----------------------------------')

""" Mean = the average value (the sum of all values divided by number of values). """

# Example
# Calculate the MEDIAN and replace any empty values with it
import pandas as pd
df = pd.read_csv('data2.csv')
x = df["Calories"].median()
df.fillna({"Calories": x}, inplace = True)
print(df.to_string())

print('-----------------------------------')

""" Median = the value in the middle, after you have sorted all values ascending. """

# Example
# Calculate the MODE and replace any empty values with it
import pandas as pd
df = pd.read_csv('data2.csv')
x = df["Calories"].mode()[0]
df.fillna({"Calories": x}, inplace = True)
print(df.to_string())

print('-----------------------------------')

""" Mode = the value that appears most frequently. """
