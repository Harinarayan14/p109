import statistics
import random
import plotly.figure_factory as pff
import pandas as pd
import csv
import plotly.graph_objects as pgo

df = pd.read_csv("data.csv")
data = df["reading score"].tolist()
mean = sum(data) / len(data)
median = statistics.median(data)
mode = statistics.mode(data)
stdev = statistics.stdev(data)

stdev_start_1, stdev_end_1 = mean-stdev, mean+stdev
stdev_start_2, stdev_end_2 = mean-(2*stdev), mean+(2*stdev)
stdev_start_3, stdev_end_3 = mean-(3*stdev), mean+(3*stdev)

data_stdev_1 = [result for result in data if result > stdev_start_1 and result < stdev_end_1]
data_stdev_2 = [result for result in data if result > stdev_start_2 and result < stdev_end_2]
data_stdev_3 = [result for result in data if result > stdev_start_3 and result < stdev_end_3]

print(f"Mean = {mean}")
print(f"Median = {median}")
print(f"Mode = {mode}")
print(f"Standard Deviation = {stdev}")

percentage1 = len(data_stdev_1)*100.0/len(data)
percentage2 = len(data_stdev_2)*100.0/len(data)
percentage3= len(data_stdev_3)*100.0/len(data)

print(f"{percentage1}% of Data lies in First Standard Deviation Range.")
print(f"{percentage2}% of Data lies in Second Standard Deviation Range.")
print(f"{percentage3}% of Data lies in Third Standard Deviation Range.")

fig = pff.create_distplot([data], ["Reading Scores"], show_hist=False)
fig.add_trace(pgo.Scatter(x=[mean, mean], y=[0, 0.2], mode="lines", name="Mean"))
fig.add_trace(pgo.Scatter(x=[stdev_start_1, stdev_start_1], y=[0, 0.2], mode="lines", name="Standard Deviation 1 Start"))
fig.add_trace(pgo.Scatter(x=[stdev_end_1, stdev_end_1], y=[0, 0.2], mode="lines", name="Standard Deviation 1 End"))
fig.add_trace(pgo.Scatter(x=[stdev_start_2, stdev_start_2], y=[0, 0.2], mode="lines", name="Standard Deviation 2 Start"))
fig.add_trace(pgo.Scatter(x=[stdev_end_2, stdev_end_2], y=[0, 0.2], mode="lines", name="Standard Deviation 2 End"))
fig.show()