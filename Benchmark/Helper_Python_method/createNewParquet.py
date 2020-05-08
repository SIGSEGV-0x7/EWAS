import pyarrow as pa
import pyarrow.parquet as pq
import pandas as pd
import numpy as np



table = pq.read_table("sample_data.parquet")
df1 = table.to_pandas()
df2 = pd.read_csv('addColumn.csv')
df2 = df2.astype(str)
result = pd.concat([df1, df2], axis=1)
result.to_parquet('xxhash3264.parquet.gzip',compression='gzip')


print("Print\n")
print(result.info(verbose=True))






