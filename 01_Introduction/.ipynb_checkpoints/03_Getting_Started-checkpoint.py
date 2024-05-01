# Installation of Pandas
''' If you have Python and PIP already installed on a system, then installation of Pandas is very easy. Install it using this command:
                    pip install pandas
If this command fails, then use a python distribution that already has Pandas installed like, Anaconda, Spyder etc.
'''

# Import Pandas
''' Once Pandas is installed, import it in your applications by adding the import keyword:
                    import pandas
Now Pandas is imported and ready to use.
'''
# Example
import pandas
data_set = {
    'cars': ["BMW", "Volvo", "Ford"],
    'passings': [3, 7, 2]
}
var = pandas.DataFrame(data_set)
print(var)

# Pandas as pd
''' Pandas is usually imported under the pd alias.
" alias:    In Python alias are an alternate name for referring to the same thing. "
Create an alias with the as keyword while importing:
                    import pandas as pd
Now the Pandas package can be referred to as pd instead of pandas.
'''
# Example
import pandas as pd
data_set = {
    'cars': ["BMW", "Volvo", "Ford"],
    'passings': [3, 7, 2]
}
var = pd.DataFrame(data_set)
print(var)
# Checking Pandas Version
''' The version string is stored under __version__ attribute. '''
# Example
import pandas as pd
print(pd.__version__)



