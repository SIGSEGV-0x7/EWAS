import pyarrow as pa
import pyarrow.parquet as pq
import numpy as np
import pandas as pd
import os
import psutil
import time

# need install psutil for calculate memory usage
# pip install psutil


# df = pq.read_pandas('../Data/sample_data.parquet').to_pandas()
# header = ["key"]
# df.to_csv('output.csv', columns = header)

# sample example：
# df = pd.DataFrame({'A': range(1, 6), 'B': range(10, 0, -2),'C C': range(10, 5, -1)})
# print(df.query('A > B'))
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.query.html#pandas-dataframe-query

# query BY key
start_time = time.time()
process = psutil.Process(os.getpid())
df = pq.read_pandas('../Data/sample_data.parquet').to_pandas()
print(df[df.key == 'http://(com,d046,1333,)/220395CC-MAIN-20160524002110-00006-ip-10-185-217-139.ec2.internal.warc.gz.parquet'])
print(psutil.virtual_memory())
print(process.memory_info().rss)
print("--- %s seconds ---" % (time.time() - start_time))

print("\n")
print("Print\n")
print(result.info(verbose=True))


# Read data from file 'filename.csv' 
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later) 
# CSV to pandas
# import pandas as pd 
# data = pd.read_csv("filename.csv") 