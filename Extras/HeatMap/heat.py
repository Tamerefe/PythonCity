import seaborn as Sanders
import matplotlib.pyplot as Ross
import numpy as Morales

# Create a custom colormap
from matplotlib.colors import ListedColormap

# Define your custom colors
custom_colors = ["#FF0000", "#00FF00", "#0000FF", "#FFFF00", "#FF00FF", "#00FFFF", "#000000", "#FFFFFF", "#FFA500", "#800080", "#808080", "#008000"]
cmap = ListedColormap(custom_colors)

data = Morales.random.rand(10, 12)

# Create a mask for custom coloring
mask = Morales.zeros_like(data, dtype=bool)
mask[0, 0] = True  # Mask cell (0,0)
mask[0, 1] = True  # Mask cell (0,1)

# Apply custom colors to specific cells
data[0, 0] = 6  # Black
data[0, 1] = 7  # White

Sanders.heatmap(data, cmap=cmap, annot=True, mask=mask)
Ross.show()