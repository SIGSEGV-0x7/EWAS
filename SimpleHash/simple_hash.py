import pandas as pd
import numpy as np
import re

# this python file take "origin_surt_url.csv" and "tld-list-basic.txt" as input and output "origin_simplehash.csv". It is used to generate result for Simple Hash value


data = pd.read_csv("origin_surt_url.csv", names=["origin", "surt"], header=None)
data["cur_clean"] = data["surt"].apply(lambda url : (",".join(url.split("(")[1].split(")")[0].split(",")[:-1])))
content = []

import codecs   
reader = codecs.open("tld-list-basic.txt",'r', encoding='ascii', errors='ignore')

# read all the first-level domain name into one list
for reading in reader:
    content.append(reading.strip())
ltd_list = list(set(content))
num = []

# generate two bytes values 0-9, a-z, A-Z
for i in range(0, 10):
    num.append(str(i))
alpha = 'a'
for i in range(0, 26):
    num.append(alpha)
    alpha = chr(ord(alpha) + 1)
alpha = 'a'
for i in range(0, 26):
    num.append(alpha.capitalize())
    alpha = chr(ord(alpha) + 1)

num_list = []
for x in num:
    for k in num:
        num_list.append(x + k)
num_list = num_list[:len(ltd_list)]
tld_dictionary = dict(zip(ltd_list, num_list))

# mach every first-level-domain with its index bytes
data["ltd"] = data["cur_clean"].apply(lambda x : tld_dictionary.get((x.split(","))[0]) if tld_dictionary.get((x.split(","))[0]) != None else "ZZ")
data = data.drop("surt", axis = 1)

data["header"] = data["origin"].apply(lambda x : "0" if x[:5] == "https" else ("1" if x[:5] == "http:" else "2"))
data["simple_hash"] = data.header + data.ltd + data["cur_clean"].apply(lambda x : "".join(x.split(",")[1:]))

# export data to CSV
data.drop(["cur_clean", "ltd", "header"], axis = 1).to_csv("origin_simplehash.csv", header = False, index = False)