import pyarrow as pa
import pyarrow.parquet as pq
import numpy as np
import pandas as pd

# df = pd.DataFrame({'one': [-1, np.nan, 2.5],
#                 'two': ['foo', 'bar', 'baz'],
#                 'three': [True, False, True]},
#                 index=list('abc'))
# table = pa.Table.from_pandas(df)
# pq.write_table(table, './temp.parquet')



# table2 = pq.read_table('./temp.parquet')
# print(table2.to_pandas())

# Test parquet file read
# example = pq.read_table('./sample_data.parquet')
# print(example)

# read sample data as pandas DataFrame
df = pq.read_pandas('./sample_data.parquet').to_pandas()
df.to_csv('sample_data.csv')
print(df.info())
print(df.head())