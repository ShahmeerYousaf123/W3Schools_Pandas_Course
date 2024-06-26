# Read CSV Files
''' A simple way to store big data sets is to use CSV files (comma separated files).
CSV files contains text and is a well know format that can be read by everyone including Pandas.
In our examples we will be using a CSV file called 'data.csv'. '''
# Example
# Load the CSV into a DataFrame
import pandas as pd
df = pd.read_csv('data.csv')
print(df.to_string())

print('--------------')

""" Tip: use to_string() to print the entire DataFrame. """
''' If you have a large DataFrame with many rows, Pandas will only return the first 5 rows, and the last 5 rows. '''
# Example
# print the DataFrame without the to_string() method
import pandas as pd
df = pd.read_csv('data.csv')
print(df)

print('--------------')

# max_rows
''' The number of rows returned is defined in Pandas option settings. You can check your system's maximum rows with the 
pd.options.display.max_rows statement. '''
# Example
# Check the number of maximum returned rows
import pandas as pd
print(pd.options.display.max_rows)

print('--------------')

''' In my system the number is 60, which means that if the DataFrame contains more than 60 rows, the print(df) statement will return only
the headers and the first and last 5 rows. You can change the maximum rows number with the same statement. '''
# Example
# Increase the maximum number of rows to display the entire DataFrame
import pandas as pd
pd.options.display.max_rows = 9999
df = pd.read_csv('data.csv')
print(df)

print('--------------')

