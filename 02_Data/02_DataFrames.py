# Pandas DataFrames

# What is a DataFrame?
''' A Pandas DataFrame is a two-dimensional data structure, like a two-diemsional array, or a table with rows and columns. '''
# Example
# Create a simple Pandas DataFrame
import pandas as pd
data = {
    'calories': [420, 380, 390],
    'duration': [50, 30, 45]
}
# load data into a DataFrame object
df = pd.DataFrame(data)
print(df)

print('--------------')

# Locate Row
''' As you can see from the result above, the DataFrame is like a table with rows and columns.
Pandas use the loc attribute to return one or more specified rows. '''
# Example
# Return row 0
# refer to the row index
print(df.loc[1])

print('--------------')

""" Note: This example returns a Pandas Series. """
# Example
# Return row 0 to 1
# use a list of indexes
print(df.loc[[0, 1]])

print('--------------')

""" Note: When using [], the result is a Pandas DataFrame. """

# Named Indexes
''' With the index argument, you can name your own indexes. '''
# Example
# Add a list of names to give each row a name
import pandas as pd
data = {
    'calories': [380, 270, 170],
    'duration': [20, 40, 50]
}
df = pd.DataFrame(data, index = ['day1', 'day2', 'day3'])
print(df)

print('--------------')

# Locate Named Indexes
''' Use the named the index in the loc attribute to return the specified rows. '''
# Example
# Return 'day2'
# refer to the named index
print(df.loc['day2'])

print('--------------')

# Load Files Into a DataFrame
''' If your data sets are stored in a file, Pandas can load them into a DataFrame. '''
# Example
# Load a comma separated file (CSV file) into a DataFrame
import pandas as pd
df = pd.read_csv('data.csv')
print(df)

