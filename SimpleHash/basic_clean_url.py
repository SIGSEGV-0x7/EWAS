import pandas as pd
import re

data = pd.read_csv("origin_surt_url.csv", names=["origin", "surt"], header=None)
data["origin_clean"] = data["origin"].apply(lambda url : re.sub('[^A-Za-z0-9]+', '', url[5:]))
data.drop("surt", axis = 1).to_csv("origin_simpleclean.csv", header = False, index = False)