import pyarrow as pa
import pyarrow.parquet as pq
import pandas as pd
import linecache
import pyarrow.parquet as pq
table = pq.read_table("sample_data.parquet")

df1 = table.to_pandas()
df2 = pd.read_csv('addColumn.csv')
result = pd.concat([df1, df2], axis=1)
print(result.iloc[:5])
# result.to_csv('combine.csv')