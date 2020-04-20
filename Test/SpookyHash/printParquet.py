import pyarrow as pa
import pyarrow.parquet as pq
import pandas as pd
import linecache
import pyarrow.parquet as pq

#df = pq.read_pandas('sample_data.parquet').to_pandas()
#print(df.iloc[:5])


# print a specific column in parquet file by column header
df = pq.read_pandas('sample_data.parquet').to_pandas()
df['originalUrl'].to_csv('originalUrl.csv')