# Efficient Web Archive Searching

## Installation and Setup

1. 64-bit version of Python 3.7 or higher (32-bit will lead to a PEP517 Error during the Pyarrow installation process).

2. Clone this repository to local machine.

3. Install python requirements with **python -m pip install -r python_requirement.txt** command line.

## Project Structure

### Benchmark/

* CityHash/
  * CityHash.csv: CityHash results.
  * addColumn.csv: add column to CityHash results.
* Helper_Python_method/
  * createNewParquet.py: append CSV data to a Parquet file.
  * addHeader.py: add header to a CSV file.
  * printParquet.py: print Parquet file.
  * queryInPandas.py: query in Pandas data frame.
  * addColumnIndex.py: add column index to the CSV file.
* SimpleHash/
  * SimpleHash.csv: SimpleHash results.
  * addColumn.csv: add column to SimpleHash results.
* Spark_query_Script/
  * cs4624_parquet.json: Apache Spark query script.
* SpookyHash/
  * SpookyHash.csv: SpookyHash results.
  * addColumn.csv: add column to SpookyHash results.
* xxHash/
  * xxHash3264.csv: xxHash results.
  * addColumn.csv: add column to xxHash results.

### Data/

This directory is used to store any large file. It has been added to .gitignore in order to avoid long upload and download time. The read_this.txt file is used as a place holder file.

### Extract/

* Input file:
  * Apache Parquet file
* Output file:
  * original_url.csv
  * origin_surt_url.csv
* Jupyter Notebook file:
  * extract.ipynb

### SimpleHash/

* Input file:
  * origin_surt_url.csv
  * tld-list-basic.txt
* Simple Hash function:
  * simple_hash.py
* Output file:
  * origin_simplehash.csv

### SpookyMurmurHash/

* Input file:
  * origin_simpleclean.csv
* Main file:
  * main.cpp
* 64 bit Murmur hash function:
  * MurmurHash2.cpp
  * MurmurHash2.h
* 128 bit Murmur hash function:
  * MurmurHash3.cpp
  * MurmurHash3.h
* 32 bit, 64 bit, and 128 bit Spooky hash functions:
  * SpookyV2.cpp
  * SpookyV2.h
* Object file:
  * Hash.o
* Output file:
  * hash128.csv

### XXHash/

* Input file:
  * origin_simpleclean.csv
* xxHash function:
  * xxhash_parse.py
* Output file:
  * xxhash3264.csv

### basic clean/

* Input file:
  * origin_surt_url.csv
* Basic clean function:
  * basic_clean_url.py
* Output file:
  * origin_simpleclean.csv

### cityHash/

* Input file:
  * origin_simpleclean.csv
* Main file:
  * main.cc
* 32 bit and 64 bit city Hash function:
  * city.cc
  * city.h
* Object file:
  * city.o
* Output file:
  * hashValue.csv
