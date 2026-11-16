from pyOpenBCI import OpenBCICyton
import time
import numpy as np
import threading
import pandas as pd

data = [[0,0,0,0,0,0,0,0]]
index = [0]
times = [[0,0]]
COLUMN_NAMES = ['index', 'P3', 'P5', 'CP3', 'CP5', 'P4', 'P6', 'CP4', 'CP6', 'timestamp', 'timeFormat']
# COLUMN_NAMES = ['index', 'Pz', 'P2', 'P4', 'P6', 'CPz', 'CP2', 'CP4', 'CP6', 'timestamp', 'timeFormat']
df = pd.DataFrame(columns=COLUMN_NAMES)

def print_raw(sample):
	print(sample.channels_data)

SCALE_FACTOR = (4500000)/24/(2**23-1)

def save_data(sample):
    global data
    data.append([i*SCALE_FACTOR for i in sample.channels_data])
    index.append(index[-1]+1)
    current_timestamp = int(time.time())
    date_string = time.strftime("%H-%M-%S", time.localtime(current_timestamp))
    times.append([time.time(), date_string])

board = OpenBCICyton(daisy=False)

def start_cyton():
    board.start_stream(save_data)
    
y = threading.Thread(target=start_cyton)
y.daemon = True
y.start()

print("start1")
time.sleep(60) #Second

print("beark")
data.append([0, 0, 0, 0, 0, 0, 0, 0])
index.append(0)
current_timestamp = int(time.time())
date_string = time.strftime("%H-%M-%S", time.localtime(current_timestamp))
times.append([time.time(), date_string])
time.sleep(30) #Second

print("start2")
data.append([0, 0, 0, 0, 0, 0, 0, 0])
index.append(0)
current_timestamp = int(time.time())
date_string = time.strftime("%H-%M-%S", time.localtime(current_timestamp))
times.append([time.time(), date_string])
time.sleep(60) #Second

print("beark")
data.append([0, 0, 0, 0, 0, 0, 0, 0])
index.append(0)
current_timestamp = int(time.time())
date_string = time.strftime("%H-%M-%S", time.localtime(current_timestamp))
times.append([time.time(), date_string])
time.sleep(30) #Second

print("start3")
data.append([0, 0, 0, 0, 0, 0, 0, 0])
index.append(0)
current_timestamp = int(time.time())
date_string = time.strftime("%H-%M-%S", time.localtime(current_timestamp))
times.append([time.time(), date_string])
time.sleep(60) #Second

print("beark")
data.append([0, 0, 0, 0, 0, 0, 0, 0])
index.append(0)
current_timestamp = int(time.time())
date_string = time.strftime("%H-%M-%S", time.localtime(current_timestamp))
times.append([time.time(), date_string])
time.sleep(30) #Second

print("start4")
data.append([0, 0, 0, 0, 0, 0, 0, 0])
index.append(0)
current_timestamp = int(time.time())
date_string = time.strftime("%H-%M-%S", time.localtime(current_timestamp))
times.append([time.time(), date_string])
time.sleep(60) #Second

print("beark")
data.append([0, 0, 0, 0, 0, 0, 0, 0])
index.append(0)
current_timestamp = int(time.time())
date_string = time.strftime("%H-%M-%S", time.localtime(current_timestamp))
times.append([time.time(), date_string])
time.sleep(30) #Second

print("start5")
data.append([0, 0, 0, 0, 0, 0, 0, 0])
index.append(0)
current_timestamp = int(time.time())
date_string = time.strftime("%H-%M-%S", time.localtime(current_timestamp))
times.append([time.time(), date_string])
time.sleep(60) #Second

print("beark")
data.append([0, 0, 0, 0, 0, 0, 0, 0])
index.append(0)
current_timestamp = int(time.time())
date_string = time.strftime("%H-%M-%S", time.localtime(current_timestamp))
times.append([time.time(), date_string])
time.sleep(30) #Second


board.disconnect()
print("Save file...")

df['index'] = index
df[['P3', 'P5', 'CP3', 'CP5', 'P4', 'P6', 'CP4', 'CP6']] = data #r
# df[['Pz', 'P2', 'P4', 'P6', 'CPz', 'CP2', 'CP4', 'CP6']] = data #l
df[['timestamp', 'timeFormat']] = times
# print(df.head())


current_timestamp = int(time.time())
date_string = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime(current_timestamp))
# file_name = f"{date_string}_8channelsFlatL.txt"
# file_name = f"{date_string}_8channelsRoughL.txt"
file_name = f"{date_string}_8channelsFurryL.txt"
df.to_csv(file_name, sep=',', index=False)
print("Successful   " + file_name)