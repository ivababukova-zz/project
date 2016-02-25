"""
Demo of table function to display a table within a plot.
"""
import numpy as np
import matplotlib.pyplot as plt

# data for SIP0
data =  [[9.454,  22.222,   0,   0    ], # 1
         [4.315,   1.777,   0,   0    ], # 2
         [0,           0,   0,   0    ], # 3
         [0,           0,   0,   0    ], # 4
         [19.387, 12.444,   0,   3.75 ], # 5
         [66.844, 63.557, 100,   96.25]] # sip

#data = [[9.453,  22.222,   0,   0    ], # 1
#        [4.315,   1.777,   0,   0    ], # 2
#        [6.701,  12.444,   0,   0    ], # 3
#        [27.263,  4.444,   0,   3.75 ], # 4
#        [19.387,      0,   0,   0    ], # 5
#        [32.881, 59.113, 100,   96.25]] # sip

columns = ('AIDS', 'PCMS', 'PDBS', 'PPIGO')
rows = (" SIP", " Fail 5 ", " Fail 4 ", " Fail 3 ", " Fail 2 ", " Fail 1 ")

values = np.arange(0, 100, 5)

# Get some pastel shades for the colors
colors = plt.cm.BuPu(np.linspace(0, 0.8, len(rows))) # sip0
#colors = plt.cm.Reds(np.linspace(0, 0.8, len(rows)))
n_rows = len(data)

index = np.arange(len(columns)) + 0.3
bar_width = 0.4

# Initialize the vertical-offset for the stacked bar chart.
y_offset = np.array([0]*len(columns))

# Plot bars and create text labels for the table
cell_text = []
for row in range(n_rows):
    plt.bar(index, data[row], bar_width, bottom=y_offset, color=colors[row])
    y_offset = y_offset + data[row]
    y_offsetTable = data[row]
    cell_text.append([x for x in y_offsetTable])
# Reverse colors and text labels to display the last value at the top.
colors = colors[::-1]
cell_text.reverse()

# Adjust layout to make room for the table:
plt.subplots_adjust(left=0.2, bottom=0.2)

plt.ylabel("Percentage of the targets")
plt.yticks(values, ['%d' % val for val in values])
plt.xticks([])
plt.title('SIP0')

plt.show()
