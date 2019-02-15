import numpy as np
import pandas as pd

#these two syntaxes are the same

x_axis = np.arange(len(dataframe))

tick_locations = []
for value in x_axis:
    tick_locations.append(value)

tick_locations = [value for value in x_axis]
