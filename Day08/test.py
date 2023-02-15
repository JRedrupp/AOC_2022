import pandas

# Create test dataframe
df = pandas.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})

# Create another DF
df2 = pandas.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})

# merge the 2 dfs
df3 = pandas.merge(df, df2, on='a', suffixes=('', '_y'))

# print the result
print(df3)