import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib as mpl

mpl.rcParams['agg.path.chunksize'] = 10000

# Replace coma with dot
data = ""
with open('2500sR.txt', 'r+') as file:
    data = file.read().replace(',', '.').replace(' ', ';')

with open("2500sR.txt", "w") as out_file:
    out_file.write(data)

# Plot data
data = np.loadtxt('2500sR.txt')

y = data[:, 5]
x = data[:, 0]
gate1 = data[:, 1]
gate2 = data[:, 3]
# Mean filter for data
y = [(a + b) / 2 for a, b in zip(y[::8], y[1::8])]

x = [(a + b) / 2 for a, b in zip(x[::8], x[1::8])]

g1_nofilter = [(a + b) / 2 for a, b in zip(gate1[::8], gate1[1::8])]
g1 = [element / 50 for element in g1_nofilter]

g2_no_filter = [(a + b) / 2 for a, b in zip(gate2[::8], gate2[1::8])]
g2 = [element / 5 for element in g2_no_filter]

y2 = [element / 3 for element in y]
plt.plot(x, y2, label="current", color="maroon")

plt.plot(x, g1, label="Q1,3", color="yellow", linestyle='-')

plt.plot(x, g2, label="Q2,4", color="blue", linestyle='-')

plt.axhline(y=0, color='black', linestyle='-')
plt.xlabel("Time (us)")
plt.ylabel("Current (A)")
plt.legend(loc=(0.8, 0.8))
plt.title("Inductor current")
plt.show()
