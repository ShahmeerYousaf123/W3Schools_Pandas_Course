# Pandas Series

# What is a Series?
''' A Pandas Series is like a column in a table. It is a one-dimensional array holding data of any type. '''
# Example
# Create a simple Pandas Series from a list
import pandas as pd
a = [1, 7, 3]
var = pd.Series(a)
print(var)

print('------------------')

# Labels
''' If nothing else is specified, the values are labeled with their index number. First value has index 0,
second value has index 1 etc. This label can be used to access a specified value.
'''
# Example
# Return the first value of the Series
import pandas as pd
a = [3, 4, 5]
var = pd.Series(a)
print(var[0])

print('------------------')

# Create Labels
''' With the index argument, you can name your own labels. '''
# Example
# Create your own labels
import pandas as pd
a = [1, 2, 3]
var = pd.Series(a, index = ["x", "y", "z"])
print(var)

print('------------------')

''' When you have created labels, you can access an item by referring to the label. '''
# Example
# Return the value of "y"
import pandas as pd
a = [1, 2, 3]
var = pd.Series(a, index = ["x", "y", "z"])
print(var["y"])

print('------------------')

# Key/Value Objects as Series
''' You can also use a key/value object, like a dictionary, when creating a Series. '''
# Example
# Create a simple Pandas Series from a dictionary
import pandas as pd
calories = {"day1": 103, "day2": 739, "day3": 203}
var = pd.Series(calories)
print(var)

print('------------------')

""" Note: The keys of the dictionary become the labels. """
''' To select only some of the items in the dictionary, use the index argument and specify only the items
you want to include in the Series. '''
# Example
# Create a Series using only data from "day1" and "day2"
import pandas as pd
calories = {"day1": 103, "day2": 739, "day3": 203}
var = pd.Series(calories, index = ["day1", "day2"])
print(var)

print('------------------')

# DataFrames
''' Data sets in Pandas are usually multi-dimensional tables, called DataFrames.
Series is like a Column, a DataFrame is the whole table. '''
# Example
# Create a DataFrame from two Series
import pandas as pd
data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}
var = pd.DataFrame(data)
print(var)

