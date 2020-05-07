import pandas as pd
import xxhash

# this file take a input as "origin_simpleclean.csv" and export result to "xxhash3264.csv"

simpleclean = pd.read_csv("origin_simpleclean.csv", names=["origin", "cleaned"], header=None)

# apply xxh32() and xxh64() to all cleaned URL
simpleclean["xxhash32"] = simpleclean["cleaned"].apply(lambda x : xxhash.xxh32(x).hexdigest())
simpleclean["xxhash64"] = simpleclean["cleaned"].apply(lambda x : xxhash.xxh64(x).hexdigest())
simpleclean.drop(["cleaned"], axis = 1).to_csv("xxhash3264.csv", header = False, index = False)
