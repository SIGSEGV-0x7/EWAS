import pyarrow as pa
import pyarrow.parquet as pq
import pandas as pd
import linecache
import csv
import numpy as np
import os
import psutil
import time
# need install psutil for calculate memory usage
# command: pip install psutil


# add header method, If needed
# with open('input.csv',newline='') as f:
#    r = csv.reader(f)
#    data = [line for line in r]
# with open('output.csv','w',newline='') as f:
#    w = csv.writer(f)
#    w.writerow(['beforeHash','afterHash'])
#    w.writerows(data)
    

# add tag column 0, 1, 2, 3...
# so it can merge by tag
# myfile1 = open("hash128bit.csv","r",encoding='utf-8')
# myfile2 = open("addColumn.csv","w",encoding='utf-8')
# counter = 0
# for i in myfile1:
#     myfile2.write(',' + i)
#     break
# for i in myfile1:
#     myfile2.write(str(counter)+',' + i)
#     counter = counter + 1
# myfile1.close()
# myfile2.close()


#merge in pandas and print the resulet first 5 row 
table = pq.read_table("sample_data.parquet")
df1 = table.to_pandas()
df2 = pd.read_csv('addColumn.csv')
result = pd.concat([df1, df2], axis=1)
# print(result.iloc[:5])
# Save merge result to csv, if needed
# result.to_csv('result.csv')


# Test Merge result: print first 5 row  
# df = pq.read_pandas('sample_data.parquet').to_pandas()
# print(df.iloc[:5])


# print a specific column by header:
# Print all originalUrl to CSV file for query 
# df = pq.read_pandas('sample_data.parquet').to_pandas()
# df['originalUrl'].to_csv('originalUrl.csv')




# Other example：
# df = pd.DataFrame({'A': range(1, 6), 'B': range(10, 0, -2),'C C': range(10, 5, -1)})
# print(df.query('A > B'))
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.query.html#pandas-dataframe-query







print("\n")
print("Query by 32 bit Hash Value:\n")
start_time = time.time()
process = psutil.Process(os.getpid())
print(result[result.hash32 == '2390256759'])
# print(psutil.virtual_memory())
print(process.memory_info().rss)
print("--- %s seconds ---" % (time.time() - start_time))
