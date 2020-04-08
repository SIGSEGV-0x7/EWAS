import pandas as pd
import xxhash

simpleclean = pd.read_csv("origin_simpleclean.csv", names=["origin", "cleaned"], header=None)
simpleclean["xxhash32"] = simpleclean["cleaned"].apply(lambda x : xxhash.xxh32(x).hexdigest())
simpleclean["xxhash64"] = simpleclean["cleaned"].apply(lambda x : xxhash.xxh64(x).hexdigest())
simpleclean.drop(["cleaned"], axis = 1).to_csv("xxhash3264.csv", header = False, index = False)

# print("32 list  has length: " + str(len(list(simpleclean.xxhash32))))
# print("32 duplicate set has length: " + str(len(set(simpleclean.xxhash32))))

# print("64 list  has length: " + str(len(list(simpleclean.xxhash64))))
# print("64 duplicate set has length: " + str(len(set(simpleclean.xxhash64))))