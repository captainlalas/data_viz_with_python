# Importing the required libraries
import pandas as pd
import plotly.express as px
import dash
from dash import dcc
from dash import html

# Task 1 - Data Prepration
# Read the airline data into pandas dataframe
airline_data =  pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/airline_data.csv', 
                            encoding = "ISO-8859-1",
                            dtype={'Div1Airport': str, 'Div1TailNum': str, 
                                   'Div2Airport': str, 'Div2TailNum': str})

# Randomly sample 500 data points. Setting the random state to be 42 so that we get same result.
data_500 = airline_data.sample(n=500, random_state=42)
# Pie Chart Creation
fig = px.pie(data_500, values='Flights', names='DistanceGroup', title='Distance group proportion by flights')


# Task 2 - Dash application and the layout skeleton
# Create the dah app
app = dash.Dash(__name__)
# Get the layout, create outer div, add the title, a paragraph and add the graph component
# app.layout = html.Div(children=[html.H1(),
#                                 html.P(),
#                                 dcc.Graph(),])


# Task 3 - App the application title
# Update the app title html.H1()
app.layout = html.Div(children=[html.H1('Airline Dashboard',
                                        style={'textAlign':'center',
                                               'color':'#503D36',
                                               'font-size':40}),
                                               html.P('Proportion of distance group (250 mile distance interval group) by flights.', 
                                                      style={'textAlign':'center', 'color': '#F57241'}),
                                               dcc.Graph(figure=fig),
                    ])

# Run the app
if __name__ == '__main__':
    app.run_server()

# To run the app:
# 1- Go to the terminal, navigate the the folder of the file and type
# >python dash_basics.py
# Copy the the link on which the app is running (eg: Dash is running on http://127.0.0.1:8050/) and open in a browser