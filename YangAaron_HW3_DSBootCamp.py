import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Brooklyn_Bridge_Automated_Pedestrian_Counts_Demonstration_Project.csv")

df['hour_beginning'] = pd.to_datetime(df['hour_beginning'])

df['hour'] = df['hour_beginning'].dt.hour
df['month'] = df['hour_beginning'].dt.month
df['year']= df['hour_beginning'].dt.year
df['date'] = df['hour_beginning'].dt.date
df['day_name'] = df['hour_beginning'].dt.day_name()

df['temperature'] = df['temperature'].ffill()
df['precipitation'] = df['precipitation'].ffill()
df['weather_summary'] = df['weather_summary'].ffill()

print(df.dtypes)

#Work on the Brooklyn Pedestrian Dataset: https://data.cityofnewyork.us/api/views/6fi9-q3ta/rows.csv?accessType=DOWNLOAD

#1)Filter the data to include only weekdays (Monday to Friday) and plot a line graph showing the pedestrian counts for each day of the week.
weekdays_df = df[df['day_name'].isin(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])] # Filter data for weekdays (Monday to Friday)
pedestrian_counts_by_day = weekdays_df.groupby('day_name')['Pedestrians'].sum() # Aggregate pedestrian counts by day of the week

days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday','Saturday','Sunday']
pedestrian_counts_by_day = pedestrian_counts_by_day.reindex(days_order)

#plot line graph
pedestrian_counts_by_day.plot(kind='line', marker='o', linestyle='-',color='b')
plt.xlabel('Day of the Week')
plt.ylabel('Pedestrian Count')
plt.title('Pedestrian Counts by Day of the Week')
plt.grid(True)

#2) Track pedestrian counts on the Brooklyn Bridge for the year 2019 and analyze how different weather conditions influence pedestrian activity in that year. Sort the pedestrian count data by weather summary to identify any correlations( with a correlation matrix) between weather patterns and pedestrian counts for the selected year.
yr2019_df = df[df['year'].isin([2019])] #Filtered data for points in year 2019
#pedestrian_counts_by_weather = yr2019_df.groupby('weather_summary')['Pedestrians'].sum()

plt.figure(figsize=(10, 6))
sns.boxplot(data=yr2019_df,x='weather_summary', y='Pedestrians')
plt.title('Pedestrian Counts by Weather Summary')
plt.xlabel('Weather Summary')
plt.ylabel('Pedestrian Count')
plt.xticks(rotation=45)
plt.tight_layout()

#3) Implement a custom function to categorize time of day into morning, afternoon, evening, and night, and create a new column in the DataFrame to store these categories. Use this new column to analyze pedestrian activity patterns throughout the day.
def categorize_time(hour):
    if 5 <= hour < 12:
        return 'Morning'
    elif 12 <= hour < 17:
        return 'Afternoon'
    elif 17 <= hour < 22:
        return 'Evening'
    else:
        return 'Night'

df['time_category'] = df['hour'].apply(categorize_time)
pedestrian_counts_by_time_category = df.groupby('time_category')['Pedestrians'].sum() # Aggregate pedestrian counts by time category
time_category_order = ['Morning', 'Afternoon', 'Evening', 'Night']
pedestrian_counts_by_time_category = pedestrian_counts_by_time_category.reindex(time_category_order)

plt.figure(figsize=(12,6))
pedestrian_counts_by_time_category.plot(kind='bar', color='blue')
plt.title('Total Pedestrian Counts by Time Category')
plt.xlabel('Time Category')
plt.ylabel('Pedestrian Count')
plt.grid(axis='y')  #grid created along y axis
plt.tight_layout()
plt.show()
