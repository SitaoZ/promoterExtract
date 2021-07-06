import pandas as pd
import matplotlib.pyplot as plt

# create dataframe
Delay = (53.46, 36.22, 83, 17)
Latency = (38, 44, 53, 10)
index = ['T=0', 'T=26', 'T=50','T=900']
df = pd.DataFrame({'Delay': Delay, 'Latency': Latency}, index=index)

# dicts with errors
Delay_error = {53.46: {'min': 0,'max': 60}, 36.22: {'min': 12,'max': 70}, 83: {'min': 21,'max': 54}, 17: {'min': 12,'max': 70}}
Latency_error = {38: {'min': 2, 'max': 70}, 44: {'min': 12,'max': 87}, 53: {'min': 9,'max': 60}, 10: {'min': 11,'max': 77}}

# combine them; providing all the keys are unique
z = {**Delay_error, **Latency_error}

# plot
ax = df.plot.bar(rot=0)
plt.xlabel('Time')
plt.ylabel('(%)')
plt.ylim(0, 101)

for p in ax.patches:
    x = p.get_x()  # get the bottom left x corner of the bar
    w = p.get_width()  # get width of bar
    h = p.get_height()  # get height of bar
    min_y = z[h]['min']  # use h to get min from dict z
    max_y = z[h]['max']  # use h to get max from dict z
    plt.vlines(x+w/2, min_y, max_y, color='k')  # draw a vertical line

plt.show()
