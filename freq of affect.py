import numpy as np
import pandas as pd

df1_name = input("Enter file name: ")
df1_name_strip = df1_name.strip('"')
df1 = pd.read_csv(df1_name_strip)
df1['Label'] = df1['Label'].str.lower()
df1['Label'] = df1['Label'].str.strip()
start_interval = int(input("Start interval: "))
end_interval = int(input("End Interval: "))
df1_unique_intervals = list(df1['Interval'].unique())
for i in range(start_interval, end_interval+1):
    if i not in df1_unique_intervals:
        time_pressed = (i-1) * 10 + 0.001
        time_released = i * 10
        label = "neutral"
        interval = i
        add_row = {"Time Pressed": time_pressed,
                   "Time Released": time_released, "Label": label, "Interval": interval}
        df1 = df1.append(add_row, ignore_index=True)
df1['zip'] = list(zip(df1['Label'], df1['Interval']))
df1.sort_values(by=['zip'])
unique_values_one = list(df1.zip.unique())
pos_df1 = 0
neg_df1 = 0
neut_df1 = 0
label_list = ["positive",
              "negative",
              "neutral",
              ]
for value in unique_values_one:
    if value[0] == label_list[0]:
        pos_df1 += 1
    elif value[0] == label_list[1]:
        neg_df1 += 1
    elif value[0] == label_list[2]:
        neut_df1 += 1
print("Name: ", df1_name_strip)
print('pos: ' + str(pos_df1))
print('neg: ' + str(neg_df1))
print('neut: ' + str(neut_df1))
print('Total int: ' + str((end_interval - start_interval + 1)))
