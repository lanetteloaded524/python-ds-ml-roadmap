# Pandas Cheat Sheet

> **Quick Reference** — `import pandas as pd`

---

## 📦 Creating DataFrames & Series

```python
# From dict
df = pd.DataFrame({'a': [1, 2], 'b': [3, 4]})

# From list of dicts
df = pd.DataFrame([{'a': 1, 'b': 2}, {'a': 3, 'b': 4}])

# Series
s = pd.Series([10, 20, 30], name='values')
```

| Function | Description |
|---|---|
| `pd.DataFrame(data, columns, index)` | Create DataFrame |
| `pd.Series(data, name, index)` | Create Series |
| `pd.read_csv('file.csv')` | Read CSV |
| `pd.read_excel('file.xlsx')` | Read Excel |
| `pd.read_json('file.json')` | Read JSON |
| `pd.read_sql(query, conn)` | Read from SQL |
| `pd.read_parquet('file.parquet')` | Read Parquet |

---

## 🔍 Inspection

| Method | Description |
|---|---|
| `df.head(n)` | First n rows (default 5) |
| `df.tail(n)` | Last n rows |
| `df.info()` | Column types, non-null counts, memory |
| `df.describe()` | Summary statistics |
| `df.shape` | `(rows, cols)` |
| `df.dtypes` | Data type of each column |
| `df.columns` | Column names |
| `df.index` | Row index |
| `df.nunique()` | Unique values per column |
| `df.value_counts()` | Frequency counts |
| `df.sample(n)` | Random n rows |
| `df.memory_usage()` | Memory per column |

---

## 🎯 Selection

| Syntax | Description | Example |
|---|---|---|
| `df['col']` | Single column (Series) | `df['name']` |
| `df[['a', 'b']]` | Multiple columns | `df[['name', 'age']]` |
| `df.loc[row, col]` | By label | `df.loc[0:5, 'name':'age']` |
| `df.iloc[row, col]` | By position | `df.iloc[0:5, 0:3]` |
| `df[df['col'] > x]` | Boolean indexing | `df[df['age'] > 30]` |
| `df.query()` | SQL-like filter | `df.query('age > 30 & city == "NYC"')` |
| `df.at[idx, col]` | Single value (label) | `df.at[0, 'name']` |
| `df.iat[r, c]` | Single value (position) | `df.iat[0, 1]` |

```python
# Chained conditions
df[(df['age'] > 25) & (df['city'] == 'NYC')]

# isin
df[df['city'].isin(['NYC', 'LA'])]

# between
df[df['age'].between(20, 30)]
```

---

## ❓ Missing Data

| Method | Description | Example |
|---|---|---|
| `df.isna()` | Boolean mask of NaNs | `df.isna().sum()` |
| `df.notna()` | Boolean mask of non-NaNs | `df[df['col'].notna()]` |
| `df.fillna(value)` | Fill NaNs | `df.fillna(0)` or `df.fillna(method='ffill')` |
| `df.dropna()` | Drop rows with NaNs | `df.dropna(subset=['col'])` |
| `df.interpolate()` | Interpolate missing | `df.interpolate(method='linear')` |
| `df.replace()` | Replace values | `df.replace({-999: np.nan})` |

---

## 🔄 Data Types

```python
df['col'] = df['col'].astype(int)
df['col'] = pd.to_numeric(df['col'], errors='coerce')
df['date'] = pd.to_datetime(df['date'])
df['cat'] = pd.Categorical(df['cat'], categories=['low', 'mid', 'high'], ordered=True)
```

---

## 🔤 String Methods

Access via `.str` accessor on a string column:

| Method | Description | Example |
|---|---|---|
| `.str.lower()` | Lowercase | `df['name'].str.lower()` |
| `.str.upper()` | Uppercase | `df['name'].str.upper()` |
| `.str.contains()` | Pattern match | `df['name'].str.contains('john', case=False)` |
| `.str.replace()` | Replace substring | `df['col'].str.replace('old', 'new')` |
| `.str.split()` | Split by delimiter | `df['col'].str.split(',', expand=True)` |
| `.str.strip()` | Trim whitespace | `df['col'].str.strip()` |
| `.str.len()` | String length | `df['name'].str.len()` |
| `.str.extract()` | Regex extract | `df['col'].str.extract(r'(\d+)')` |
| `.str.startswith()` | Prefix check | `df['col'].str.startswith('A')` |

---

## 📊 GroupBy

```python
# Basic groupby
df.groupby('city')['salary'].mean()

# Multiple aggregations
df.groupby('city')['salary'].agg(['mean', 'median', 'count'])

# Named aggregation
df.groupby('city').agg(
    avg_salary=('salary', 'mean'),
    max_age=('age', 'max'),
    count=('name', 'count')
)

# Transform — returns same-shaped output
df['salary_zscore'] = df.groupby('city')['salary'].transform(
    lambda x: (x - x.mean()) / x.std()
)

# Apply — flexible group-wise function
df.groupby('city').apply(lambda g: g.nlargest(3, 'salary'))

# Multiple group keys
df.groupby(['city', 'dept'])['salary'].mean()
```

---

## 🔗 Merging & Joining

### merge()

```python
pd.merge(left, right, on='key')                  # inner join (default)
pd.merge(left, right, on='key', how='left')       # left join
pd.merge(left, right, on='key', how='right')      # right join
pd.merge(left, right, on='key', how='outer')      # outer join
pd.merge(left, right, left_on='a', right_on='b')  # different column names
```

### concat()

```python
pd.concat([df1, df2], axis=0)              # stack vertically (rows)
pd.concat([df1, df2], axis=1)              # stack horizontally (columns)
pd.concat([df1, df2], ignore_index=True)   # reset index
```

### join()

```python
df1.join(df2, on='key', how='left')  # join on index by default
```

---

## 🔀 Reshaping

| Function | Description | Example |
|---|---|---|
| `df.pivot_table()` | Pivot + aggregate | `df.pivot_table(values='val', index='row', columns='col', aggfunc='mean')` |
| `pd.melt()` | Wide → long | `pd.melt(df, id_vars=['id'], value_vars=['a', 'b'])` |
| `df.stack()` | Columns → rows | `df.stack()` |
| `df.unstack()` | Rows → columns | `df.unstack()` |
| `pd.crosstab()` | Cross tabulation | `pd.crosstab(df['a'], df['b'])` |
| `df.explode('col')` | List → rows | `df.explode('tags')` |

---

## ↕️ Sorting

| Method | Description | Example |
|---|---|---|
| `df.sort_values('col')` | Sort by column | `df.sort_values('age', ascending=False)` |
| `df.sort_values(['a','b'])` | Multi-column sort | `df.sort_values(['city', 'age'])` |
| `df.sort_index()` | Sort by index | `df.sort_index()` |
| `df.nlargest(n, 'col')` | Top n rows | `df.nlargest(10, 'salary')` |
| `df.nsmallest(n, 'col')` | Bottom n rows | `df.nsmallest(5, 'age')` |
| `df.rank()` | Rank values | `df['score'].rank(method='dense')` |

---

## ⚙️ Apply & Transform

```python
# apply — row or column-wise
df['col'].apply(lambda x: x * 2)
df.apply(lambda row: row['a'] + row['b'], axis=1)

# map — element-wise on Series (or dict mapping)
df['grade'] = df['score'].map({1: 'A', 2: 'B', 3: 'C'})

# applymap (pandas < 2.1) / map (pandas >= 2.1) — element-wise on DataFrame
df[['a', 'b']].map(lambda x: round(x, 2))       # pandas >= 2.1
df[['a', 'b']].applymap(lambda x: round(x, 2))   # pandas < 2.1
```

---

## 💾 I/O — Writing Data

| Method | Description | Example |
|---|---|---|
| `df.to_csv()` | Write CSV | `df.to_csv('out.csv', index=False)` |
| `df.to_excel()` | Write Excel | `df.to_excel('out.xlsx', index=False)` |
| `df.to_json()` | Write JSON | `df.to_json('out.json', orient='records')` |
| `df.to_sql()` | Write to SQL | `df.to_sql('table', conn, if_exists='replace')` |
| `df.to_parquet()` | Write Parquet | `df.to_parquet('out.parquet')` |
| `df.to_clipboard()` | Copy to clipboard | `df.to_clipboard()` |

---

## 📅 Time Series

```python
# Convert to datetime
df['date'] = pd.to_datetime(df['date'])

# Accessors
df['date'].dt.year
df['date'].dt.month
df['date'].dt.day_name()
df['date'].dt.quarter

# Set datetime index
df = df.set_index('date')

# Resample (requires datetime index)
df.resample('M').mean()       # monthly mean
df.resample('W').sum()        # weekly sum
df.resample('Q').first()      # quarterly first value

# Rolling window
df['rolling_avg'] = df['value'].rolling(window=7).mean()

# Shifting
df['prev'] = df['value'].shift(1)       # lag
df['next'] = df['value'].shift(-1)      # lead
df['pct_change'] = df['value'].pct_change()

# Date range
pd.date_range('2024-01-01', periods=30, freq='D')
```

---

## 💡 Quick Tips

1. **Use `query()` for readable filters:** `df.query('age > 30 and city == "NYC"')` is cleaner than chained boolean masks.
2. **Avoid iterating rows:** Use vectorized operations or `.apply()` instead of `iterrows()` — it's 100× faster.
3. **Chain methods:** `df.dropna().sort_values('col').head(10)` — Pandas methods return DataFrames so you can chain.
4. **Reduce memory:** Use `pd.read_csv('f.csv', dtype={'id': 'int32'})` or `df.astype('category')` for repeated strings.
5. **Copy when needed:** `df2 = df[['col']].copy()` to avoid `SettingWithCopyWarning`.
