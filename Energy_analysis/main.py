import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl


mpl.rcParams['agg.path.chunksize'] = 10000  # need to overcome problem with plotting too many points

# Replace coma with dot
data = ""
with open('bb.txt', 'r+') as file:
    data = file.read().replace(',', '.').replace(" ", ";")

with open("bb.txt", "w") as out_file:
    out_file.write(data)

# Get column number for time axis
with open('bb.txt', 'r+') as file:
    Counter = 0

    Content = file.read()
    CoList = Content.split("\n")

    for i in CoList:
        if i:
            Counter += 1

    x = list(range(0, Counter))

data = np.loadtxt('bb.txt')

y = data[:, 0]

z = data[:, 1]

# Mean filter for data
y_axis_voltage_c1 = [(a + b) / 2 for a, b in zip(y[:1000], y[1::1000])]

z_axis_voltage_c2 = [(a + b) / 2 for a, b in zip(z[::1000], z[1::1000])]

x_axis_data_filter = [(a + b) / 2 for a, b in zip(x[::1000], x[1::1000])]

x_axis_time = [element / 1000 for element in x_axis_data_filter]

print(len(x_axis_time))

print(len(z_axis_voltage_c2))
plt.scatter(x_axis_time, z_axis_voltage_c2, s=2, color="blue", label="U(C2)")
plt.scatter(x_axis_time, y_axis_voltage_c1, s=2, color="orange", label="U(C1)")
plt.xlabel("Time(s)")
plt.ylabel("Voltage (V)")
plt.title("Voltage transfer")
plt.legend()

plt.show()
#
# #######################################
# ####### Comulative energy #############
# #######################################
#
#
# c2_energy = [((element * element)) / 2 for element in z_axis_voltage_c2]
#
# c1_energy = [((element * element)) / 2 for element in y_axis_voltage_c1]
#
# # Plot energy versus time
# plt.scatter(x_axis_time, c2_energy, s=2, color="blue", label="E(C2)")
# plt.scatter(x_axis_time, c1_energy, s=2, color="orange", label="E(C1)")
#
# plt.xlabel("Time(s)")
# plt.ylabel("Energy (J)")
# plt.legend()
# plt.title("Energy transfer")
# plt.show()
#
# # Plot energy versus energy
# plt.scatter(c1_energy, c2_energy, s=2, color="blue", label="E(C2/C1)")
#
# plt.xlabel("Depletion (J)")
# plt.ylabel("Accumulation (J)")
# plt.legend()
# plt.title("Energy")
# plt.show()
#
# plt.show()
#
# ###############################################
# ############### Differencial energy############
# ###############################################
#
# differencual_energy_c1 = np.diff(c1_energy)
# a = np.array_str(differencual_energy_c1)
# differencual_energy_c2 = np.diff(c2_energy)
#
# #####
# # Remove last point to make lists same size for plotting
# e1 = y_axis_voltage_c1[:-1]
# e2 = z_axis_voltage_c2[:-1]
# #####
#
# efficiency = [(i / j) * 100 for i, j in zip(differencual_energy_c2, differencual_energy_c1)]
#
# print(differencual_energy_c1[121])
# print(differencual_energy_c2[121])
# print(efficiency[121])
#
# efficiency2 = [abs(element) for element in efficiency]
#
# fig, ax = plt.subplots()
# my_scatter_plot = ax.scatter(
#     e1, e2,
#     s=30,
#     c=efficiency2,
# )
#
# cbar = fig.colorbar(my_scatter_plot)
# cbar.set_label("Efficiency %")
# ax.set_xlabel("Accumulation Voltage")
# ax.set_ylabel("Depletion Voltage ")
# ax.set_title("Differential efficiency")
#
# plt.show()
#
# ################################################
#
#
# ####################################################
