import pandas as pd
import re

# this file takes "origin_surt_url.csv" as input and exports "origin_simpleclean.csv" as output\

# read in original URL's dataset in CSV file
data = pd.read_csv("origin_surt_url.csv", names=["origin", "surt"], header=None)

# get rid of all special characters
data["origin_clean"] = data["origin"].apply(lambda url : re.sub('[^A-Za-z0-9]+', '', url[5:]))

# export cleaned URL to CSV
data.drop("surt", axis = 1).to_csv("origin_simpleclean.csv", header = False, index = False)