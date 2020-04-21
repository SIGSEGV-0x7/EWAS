import pyarrow as pa
import pyarrow.parquet as pq
import pandas as pd
import linecache
import csv
import numpy as np
import os
import psutil
import time


table = pq.read_table("sample_data.parquet")
df1 = table.to_pandas()
df2 = pd.read_csv('addColumn.csv')
df2 = df2.astype(str)
result = pd.concat([df1, df2], axis=1)
result.to_parquet('cityhash.parquet.gzip',compression='gzip')


print("Print\n")
print(result.info(verbose=True))






