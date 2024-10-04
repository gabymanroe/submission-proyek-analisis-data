import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go

st.title("""
Bike Sharing Data Analysis Project
#### by Gabriel Olivia Yvonne Manurung (ML-35)
""")

st.write("## **Determining Business Question**")

st.write("""
1. How does bike-sharing demand vary across different seasons?
2. What impact do weather conditions have on bike sharing patterns?
3. Is there a significant difference in bike-sharing usage between working day and holiday?     
""")

st.write("## **Exploratory Data Analysis (EDA)**")

st.write("### Explore Season")
day_df = {
    'season': ['Spring', 'Summer', 'Fall', 'Winter'],
    'casual_mean': [334.928177, 1106.097826, 1202.611702, 729.112360],
    'registered_mean': [2269.204420, 3886.233696, 4441.691489, 3999.050562],
    'cnt_max': [7836, 8362, 8714, 8555],
    'cnt_min': [431, 795, 1115, 22],
    'cnt_mean': [2604.132597, 4992.331522, 5644.303191, 4728.162921]
}

day_df = pd.DataFrame(day_df)
day_df.set_index('season', inplace=True)
st.write('#### Seasonal Bike Rental Statistics')
st.table(day_df)
st.write("""
**Insight:**
- Fall has the highest peak day (8714 rides)
- Spring has the lowest peak (7836 rides)
- Winter has an extremely low minimum (22 rides), possibly due to severe weather
""")

st.write("### Explore Weather")
day_df = {
    'weathersit': ['Clear/Partly Cloudy', 'Light Snow/Rain', 'Misty/Cloudy'],
    'max': [8714, 4639, 8362],
    'min': [431, 22, 605],
    'mean': [4876.786177, 1803.285714, 4035.862348],
    'sum': [2257952, 37869, 996858]
}

day_df = pd.DataFrame(day_df)
day_df.set_index('weathersit', inplace=True)
st.write('#### Bike Rental Statistics based on Weather Situations')
st.table(day_df)
st.write("""
**Insight:**
- Clear days have the widest range (431 to 8714), suggesting other factors (like temperature or day of week) also play a role
- Rainy days have the smallest maximum, indicating it's hard to ride in poor weather
""")    

st.write("### Explore Working Day and Holiday Comparison")
day_df = {
    'workingday': ['Holiday', 'workingday'],
    'max': [8714, 8362],
    'min': [605, 22],
    'mean': [4330.168831, 4584.820000]
}
day_df = pd.DataFrame(day_df)
day_df.set_index('workingday', inplace=True)
st.write('#### Bike Rental Statistics: Holiday vs Working Day')
st.table(day_df)
st.write("""
**Insight:**
- Workdays show extreme difference (22 to 8362), potentially indicating severe weather or a unique event
- The difference in average usage between workdays and holidays is relatively small (about 250 rides)
- Both types of days can reach high usage levels, but for potentially different reasons (commuting or leisure)
""")    

st.write("## **Visualization & Explanatory Analysis**")

st.write('### 1. How does bike sharing demand vary across different seasons?')
day_df = {
    'Season': ['Fall', 'Spring', 'Summer', 'Winter'],
    'Registered': [840000, 410000, 710000, 710000],
    'Casual': [260000, 70000, 220000, 140000]
}

day_df = pd.DataFrame(day_df)

st.write('#### Bike Sharing Demand based on Season')

fig = go.Figure(data=[
    go.Bar(name='Registered', x=day_df['Season'], y=day_df['Registered'], marker_color='rgb(255, 192, 203)'),
    go.Bar(name='Casual', x=day_df['Season'], y=day_df['Casual'], marker_color='rgb(135, 206, 235)')
])

fig.update_layout(
    barmode='stack',
    xaxis_title='Season',
    yaxis_title='Number of Rentals',
    yaxis_range=[0, 1200000],
    legend_title_text='',
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    )
)
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGrey')
fig.update_layout(yaxis=dict(tickformat=".2s"))
st.plotly_chart(fig, use_container_width=True)

st.write("""
**Insight:**
- Fall has the highest overall demand for bike rentals
- Spring has the lowest overall demand
- Registered users consistently outnumber casual users across all seasons
- The proportion of casual users is highest in Summer and Fall
- Winter demand is surprisingly high, surpassing Spring
""")

st.write('### 2. What impact do weather conditions have on bike sharing patterns?')

day_df = {
    'Weather': ['Clear/Partly Cloudy', 'Light Snow/Rain', 'Misty/Cloudy'],
    'Rentals': [4900, 1800, 4050],
    'Error': [150, 600, 300]  
}

day_df = pd.DataFrame(day_df)

st.write('#### Bike Sharing Demand based on Weather Conditions')

fig = go.Figure(data=[
    go.Bar(
        name='Rentals',
        x=day_df['Weather'],
        y=day_df['Rentals'],
        marker_color=['rgb(255,192,203)', 'rgb(135,206,235)', 'rgb(144,238,144)'],
        error_y=dict(type='data', array=day_df['Error'])
    )
])

fig.update_layout(
    xaxis_title='Weather Conditions',
    yaxis_title='Number of Rentals',
    yaxis_range=[0, 5500],
    showlegend=False
)

fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGrey')
fig.update_layout(yaxis=dict(tickformat="d"))
st.plotly_chart(fig, use_container_width=True)

st.write("""
**Insight:**
- Clear/Partly Cloudy weather has the highest demand, with nearly 5000 rentals on average
- Misty/Cloudy weather with moderate demand, averaging about 4000 rentals
- Light Snow/Rain conditions significantly reduce demand to around 1800 rentals
- The error bars (black lines) suggest some variability within each weather category
""")

st.write('### 3. Is there a significant difference in bike-sharing usage between working days and holidays?')

day_df = {
    'Day': ['Holiday', 'Working Day'],
    'Rentals': [4040, 4326],
    'Error': [100, 100]  
}

day_df = pd.DataFrame(day_df)

st.write('#### Comparison of Bike Renters on Working Day and Holiday')

fig = go.Figure(data=[
    go.Bar(
        name='Rentals',
        x=day_df['Day'],
        y=day_df['Rentals'],
        marker_color=['rgb(255,192,203)', 'rgb(135,206,235)'],
        error_y=dict(type='data', array=day_df['Error'])
    )
])

fig.update_layout(
    xaxis_title='Day',
    yaxis_title='Number of Rentals',
    yaxis_range=[0, 5500],
    showlegend=False
)

fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGrey')
fig.update_layout(yaxis=dict(tickformat="d"))
st.plotly_chart(fig, use_container_width=True)

st.write("""
**Insight:**
- Working day had an average number of bike rentals that are slightly higher than holidays
- The difference of rentals during working days and those during holidays are relatively small
- There is a notable amount of variability in both categories, as shown by the error bar
""")

st.write("""
## **Conclusion**
### 1. How does bike sharing demand vary across different seasons?
- The seasonal influence on bike demand (Fall with the highest demand)
- Registered users are the most users throughout any season
- The service is remain popular even in Winter
- They should campaigning or promoting more in Spring    

### 2. What impact do weather conditions have on bike sharing patterns?  
- Clear or partly cloudy weather is optimal for bike sharing, likely encouraging the highest number of riders
- Misty or cloudy conditions cause a moderate decrease in ridership, but still maintain relatively high usage
- Light snow or rain dramatically reduces bike sharing demand, cutting usage by more than half compared to clear weather
- The variability within each category (shown by error bars) suggests that other factors (like temperature or day of the week) may also influence ridership within these weather conditions  

### 3. Is there a significant difference in bike-sharing usage between working day and holiday?
- While there is a difference, it may not significant. Working days show slightly higher usage
- The small difference in averages and the overlapping error bars indicate that factors such as weather, season, or special events might have a more pronounced impact on bikes sharing rentals
""")
