# So We will be using Line chart here
import pandas as pd
import plotly.express as px

# read the csv file and stored the data in dataframe
dataFrame = pd.read_csv("Covid_data.csv")

# created a figure using the dataframe
figure = px.line(dataFrame, x="date", y="cases",
                 color="country", title="Line chart of covid Data Across The Globe -Made By Swayam Sai Kar")

# Shown the figure on an ip
figure.show()
