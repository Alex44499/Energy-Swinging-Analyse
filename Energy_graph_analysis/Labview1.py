import nidaqmx
import matplotlib.pyplot as plt

with nidaqmx.Task() as task:
    task.ai_channels.add_ai_voltage_chan("Dev2/ai0")
    data = task.read(number_of_samples_per_channel=1)
    print(data)



