import pandas as pd

path_normal = "2024-03-10_19-44-55_8channelsNormalR.txt"
path_Flat = "2024-03-10_19-56-22_8channelsFlatR.txt"
path_Furry = "2024-03-10_20-06-29_8channelsFurryR.txt"
path_Rough = "2024-03-10_20-16-07_8channelsRoughR.txt"

df1 = pd.read_csv(path_normal, header=0)
print(df1.head(10))

df2 = pd.read_csv(path_Flat, header=0)
print(df2.head(10))

df3 = pd.read_csv(path_Furry, header=0)
print(df3.head(10))

df4 = pd.read_csv(path_Rough, header=0)
print(df4.head(10))