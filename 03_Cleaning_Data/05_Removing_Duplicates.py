# Pandas - Removing Duplicates

# Discovering Duplicates
''' Duplicate rows are rows that have been registered more than one time. '''

''' By taking a look at our test data set, we can assume that row 11 and 12 are duplictes.
To discover duplicates, we can use the duplicated() method.
The duplicated() method returns a Boolean values for each row. '''
# Example
# Returns True for every row that is a duplicate, otherwise False
import pandas as pd
df = pd.read_csv('data2.csv')
print(df.duplicated())

print('-----------------------------------')

# Removing Duplicates
''' To remove duplicates, use the drop_duplictes() method. '''
# Example
# Remove all duplicates
import pandas as pd
df = pd.read_csv('data2.csv')
df.drop_duplicates(inplace = True)
print(df.to_string())

print('-----------------------------------')

""" Remember: The (inplace = True) will make sure that the method does NOT return a new
DataFrame, but it will remove all duplicates from the original DataFrame. """
