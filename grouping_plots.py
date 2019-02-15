%matplotlib notebook

# Import Dependencies
import matplotlib.pyplot as plt
import pandas as pd

# Import our data into pandas from CSV
used_string = '../Resources/used_cars.csv'
used_car_df = pd.read_csv(used_string)

used_car_df

# Create a group based on the values in the 'maker' column
maker_group = used_car_df.groupby('maker')

# Count how many times each maker appears in our group
count_makers = maker_group['maker'].count()

count_makers

# Create a bar chart based off of the group series from before
count_chart = count_makers.plot(kind='bar')

# Set the xlabel and ylabel using class methods
count_chart.set_xlabel("Car Manufacturer")
count_chart.set_ylabel("Number of Cars")


plt.show()
plt.tight_layout()
