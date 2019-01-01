import pandas as pd

## series object
data = pd.Series([0.25, 0.5, 0.75, 1.0])
data = pd.Series([0.25, 0.5, 0.75, 1.0],
                  index=['a', 'b', 'c', 'd'])
data = pd.Series(dict)

data.values
data.index
data.keys()
data.items()



## DataFrames object
pd.DataFrame({'population': population,
              'area': area})
pd.DataFrame(population, columns=['population'])
data = [{'a': i, 'b': 2 * i} for i in range(3)]
pd.DataFrame(np.random.rand(3, 2),
             columns=['foo', 'bar'],
             index=['a', 'b', 'c'])



planets.describe()


## data selection
data['a':'c'] # by explicit index
data[0:2] # by implicit integer index
data[(data > 0.3) & (data < 0.8)] # masking

data.loc[1:3] # always references the explicit index
data.iloc[1:3] # always references the implicit Python-style index

data['area'] # equivalent to :
data.area

data['density'] = data['pop'] / data['area']


data.isnull() # deteting null values (NaN, None)
data.notnull() # l'inverse
data.dropna(axis='columns', how='all') # removes NaN, None, colonnes avec que des Nas
data.dropna(thresh=3) # removes NaN, None, garde lignes avec au moins 3 valeurs non nulles
data.fillna(0) #method='ffill', 'bfill' (axis=1 ou 0)


## Combining Datasets: Merge and Join
df3 = pd.merge(df1, df2)
pd.merge(df1, df2, on='employee')
pd.merge(df1, df3, left_on="employee", right_on="name")
pd.merge(df6, df7, how='outer') #'inner', 'left'...
df1a.join(df2a)

## Aggregation and Grouping
df.mean(axis='columns') # count, first, last, median, min, max, std, var, prod, sum
df.describe()

## GroupBy: Split, Apply, Combine
df.groupby('key').sum()
planets.groupby('method')['orbital_period'].median()
planets.groupby('method')['year'].describe().unstack()
df.groupby('key').aggregate(['min', np.median, max])
df.groupby('key').transform(lambda x: x - x.mean())
df.groupby('key').apply(norm_by_data2)

## Pivot Table Syntax
titanic.pivot_table('survived', index='sex', columns='class')
titanic.pivot_table('survived', ['sex', 'age'], 'class')

## Vectorized String Operations
names.str.capitalize() # lower, len, startwith('T'), match, extract... 


## times series
date = pd.to_datetime("4th of July, 2015")
date + pd.to_timedelta(np.arange(12), 'D')
dates.to_period('D') # convert to PeriodIndex
pd.date_range('2015-07-03', '2015-07-10')
pd.date_range('2015-07-03', periods=8)
pd.period_range('2015-07', periods=8, freq='M')
pd.timedelta_range(0, periods=10, freq='H')

rolling = goog.rolling(365, center=True)
data = pd.DataFrame({'input': goog,
                     'one-year rolling_mean': rolling.mean(),
                     'one-year rolling_std': rolling.std()})
weekly = data.resample('W').sum()
daily = data.resample('D').sum()
daily.rolling(30, center=True).sum()
daily.rolling(50, center=True, win_type='gaussian').sum(std=10) # gaussian window


## eval and query
result = pd.eval('-df1 * df2 / (df3 + df4) - df5')
result = pd.eval('df1 < df2 <= df3 != df4')
result = pd.eval("(df.A + df.B) / (df.C - 1)")
result = df.query('A < 0.5 and B < 0.5')

