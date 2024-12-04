import pandas as pd

df_rent=pd.read_csv("sources/daily_rent_detail.csv")
df_frequency=pd.read_csv("sources/usage_frequency.csv")
df_weather=pd.read_csv("sources/weather.csv")
df_station=pd.read_csv("sources/station_list.csv")
station_name = df_station['station_name'].unique()
df_station_start = df_rent['start_station_name'].value_counts()
df_station_end = df_rent['end_station_name'].value_counts()

# delete milliseconds to avoid ValueError
df_rent['started_at'] = df_rent['started_at'].str.replace(r'\.\d+', '', regex=True)
df_rent['ended_at'] = df_rent['ended_at'].str.replace(r'\.\d+', '', regex=True)

# convert each entry of to pandas._libs.tslibs.timestamps.Timestamp
df_rent['started_at'] = pd.to_datetime(df_rent['started_at'], format='%Y-%m-%d %H:%M:%S')
df_rent['ended_at'] = pd.to_datetime(df_rent['ended_at'], format='%Y-%m-%d %H:%M:%S')

df_rent_only_date=df_rent.copy()

# for each entry of 'started/ended_at,' deletes the time of renting and only keep the date
df_rent_only_date['started_at'] = df_rent_only_date['started_at'].dt.date
df_rent_only_date['ended_at'] = df_rent_only_date['ended_at'].dt.date

# creates a subset that lists each date with the amount of rentals that occurred
df_date_rent_num = df_rent_only_date['started_at'].value_counts()

# converts 'df_date_rent_num' to DataFrame
df_date_rent_num = df_date_rent_num.sort_index() # sort by date instead of rental quantity
df_date_rent_num = df_date_rent_num.to_frame(name='rental quantity') # 
df_date_rent_num.columns = ['rental quantity']
df_date_rent_num['datetime'] = df_date_rent_num.index
df_date_rent_num = df_date_rent_num[['datetime', 'rental quantity']]
df_date_rent_num=df_date_rent_num.reset_index()

# creates various subsets of weather conditions paired with their dates
df_date_Partially_cloudy=df_weather[df_weather['icon'] == 'partly-cloudy-day'][['datetime','icon']]
df_date_Rain=df_weather[df_weather['icon'] == 'rain'][['datetime','icon']]
df_date_Cloudy=df_weather[df_weather['icon'] == 'cloudy'][['datetime','icon']]
df_date_Snow=df_weather[df_weather['icon'] == 'snow'][['datetime','icon']]
df_date_Wind=df_weather[df_weather['icon'] == 'wind'][['datetime','icon']]
df_date_Clear=df_weather[df_weather['icon'] == 'clear-day'][['datetime','icon']]

df_date_Partially_cloudy['datetime']=pd.to_datetime(df_date_Partially_cloudy['datetime'], format='%Y-%m-%d')
df_date_Rain['datetime']=pd.to_datetime(df_date_Rain['datetime'], format='%Y-%m-%d')
df_date_Cloudy['datetime']=pd.to_datetime(df_date_Cloudy['datetime'], format='%Y-%m-%d')
df_date_Clear['datetime']=pd.to_datetime(df_date_Clear['datetime'], format='%Y-%m-%d')
df_date_Snow['datetime']=pd.to_datetime(df_date_Snow['datetime'], format='%Y-%m-%d')
df_date_Wind['datetime']=pd.to_datetime(df_date_Wind['datetime'], format='%Y-%m-%d')

df_date_rent_num['datetime']=pd.to_datetime(df_date_rent_num['datetime'], format='%Y-%m-%d') # converts each datetime object to type `datetime64`

# adds 'rental quantity' to each date/weather subset
df_date_Partially_cloudy=pd.merge(df_date_Partially_cloudy, df_date_rent_num, on='datetime', how='left')
df_date_Rain=pd.merge(df_date_Rain, df_date_rent_num, on='datetime', how='left')
df_date_Cloudy=pd.merge(df_date_Cloudy, df_date_rent_num, on='datetime', how='left')
df_date_Clear=pd.merge(df_date_Clear, df_date_rent_num, on='datetime', how='left')
df_date_Snow=pd.merge(df_date_Snow, df_date_rent_num, on='datetime', how='left')
df_date_Wind=pd.merge(df_date_Wind, df_date_rent_num, on='datetime', how='left')

df_date_Partially_cloudy.to_csv("df_date_Partially_cloudy.csv", index=False)
df_date_Rain.to_csv("df_date_Rain.csv", index=False)
df_date_Cloudy.to_csv("df_date_Cloudy.csv", index=False)
df_date_Clear.to_csv("df_date_Clear.csv", index=False)
df_date_Snow.to_csv("df_date_Snow.csv", index=False)
df_date_Wind.to_csv("df_date_Wind.csv", index=False)
df_date_rent_num.to_csv("df_date_rent_num.csv", index=False)

stations=df_station_start.index.tolist()
membership_counts = df_rent.groupby(['start_station_name', 'member_casual']).size().unstack(fill_value=0)
bike_type_counts = df_rent.groupby(['start_station_name', 'rideable_type']).size().unstack(fill_value=0)
df_station_bike_type_member = pd.concat([membership_counts, bike_type_counts], axis=1).fillna(0)
df_new_weather=df_weather.copy()
df_new_weather['datetime']=pd.to_datetime(df_new_weather['datetime'], format='%Y-%m-%d')
df_new_weather=pd.merge(df_new_weather,df_date_rent_num,on='datetime',how='left')
del(df_new_weather["description"])
del(df_new_weather["conditions"])
del(df_new_weather["icon"])
del(df_new_weather["stations"])
del(df_new_weather["name"])
del(df_new_weather["sunrise"])
del(df_new_weather["sunset"])
del(df_new_weather["moonphase"])
df_rent_only_time=df_rent.copy()
df_rent_only_time['month'] = df_rent_only_time['started_at'].dt.month
df_rent_only_time['started_at'] = df_rent_only_time['started_at'].dt.time
df_rent_only_time['ended_at'] = df_rent_only_time['ended_at'].dt.time

# Define a function to group time into half-hour intervals
def classify_time_to_half_hour(time_obj):
    hour = time_obj.hour
    minute = time_obj.minute
    # Count minutes to the nearest half hour
    if minute < 30:
        return f"{hour:02d}:00 - {hour:02d}:30"
    else:
        return f"{hour:02d}:30 - {hour+1:02d}:00"

# Applying functions for classification
df_rent_only_time['started_at_half_hour'] = df_rent_only_time['started_at'].apply(classify_time_to_half_hour)
df_rent_only_time['ended_at_half_hour'] = df_rent_only_time['ended_at'].apply(classify_time_to_half_hour)

df_rent_only_time['started_month_time'] = df_rent_only_time['month'].astype(str) + " "+ df_rent_only_time['started_at_half_hour']
df_rent_only_time['ended_month_time'] = df_rent_only_time['month'].astype(str) + " " + df_rent_only_time['ended_at_half_hour']
df_station_time=df_rent_only_time[['started_month_time','start_station_name']]
df_station_time = df_station_time.groupby(['started_month_time', 'start_station_name']).size().unstack(fill_value=0)
df_station_time = df_station_time.reset_index()
df_station_time[['month', 'started_time']] = df_station_time['started_month_time'].str.split(' ', n=1, expand=True)
del(df_station_time['started_month_time'])
df_station_time['month']=df_station_time['month'].astype(int)
df_station_time=df_station_time.sort_values(by=['month', 'started_time'])
df_station_time = df_station_time.reset_index()
columns = df_station_time.columns.tolist()
rearranged_columns = columns[-2:] + columns[:-2]
df_station_time = df_station_time[rearranged_columns]
del df_station_time['index']
df_station_time.to_csv('df_station_time.csv', index=False)

df_month_time = df_rent_only_time[['month','started_at_half_hour']]
df_month_time = df_month_time.groupby(['month', 'started_at_half_hour']).size().unstack(fill_value=0)
df_month_time.to_csv('df_month_time.csv', index=False)
df_member_casual = df_rent.groupby(["member_casual"]).size().reset_index(name="count")
df_member_casual.to_csv('df_member_casual.csv', index=False)

df_member_start = df_rent.groupby(['start_station_name', 'member_casual']).size().reset_index(name='count')
df_member_start = df_member_start.pivot_table(index='start_station_name', columns='member_casual', values='count', aggfunc='sum', fill_value=0)

df_member_start.columns = ['casual_count', 'member_count']
df_member_start = df_member_start.reset_index()
df_member_start = df_member_start.sort_values(by='member_count', ascending=False)
df_member_start.to_csv('df_member_start.csv', index=False)

df_date_weather_num=df_new_weather.copy()
df_date_weather_num['severerisk']=df_date_weather_num['severerisk'].fillna(0)
df_date_weather_num['preciptype'] = df_date_weather_num['preciptype'].map({'rain':1})
df_date_weather_num['preciptype'] = df_date_weather_num['preciptype'].fillna(0)
df_date_weather_num = df_date_weather_num.drop(columns='index')
df_date_weather_num.to_csv('df_date_weather_num.csv', index=False)

df_pro = df_date_weather_num.copy()
# Make sure the date is in datetime format
df_pro['datetime'] = pd.to_datetime(df_pro['datetime'])
# Rename the date column and target variable column
df_pro.rename(columns={'datetime': 'ds', 'rental quantity': 'y'}, inplace=True)
df_pro.to_csv('df_pro.csv', index=False)


df_end_station_time=df_rent_only_time[['ended_month_time','end_station_name']]
df_end_station_time = df_end_station_time.groupby(['ended_month_time', 'end_station_name']).size().unstack(fill_value=0)
df_end_station_time = df_end_station_time.reset_index()
df_end_station_time[['month', 'ended_time']] = df_end_station_time['ended_month_time'].str.split(' ', n=1, expand=True)
del(df_end_station_time['ended_month_time'])
df_end_station_time['month']=df_end_station_time['month'].astype(int)
df_end_station_time=df_end_station_time.sort_values(by=['month', 'ended_time'])
df_end_station_time = df_end_station_time.reset_index()
columns = df_end_station_time.columns.tolist()
rearranged_columns = columns[-2:] + columns[:-2]
df_end_station_time = df_end_station_time[rearranged_columns]
del df_end_station_time['index']

new_df_end_station_time = df_end_station_time.groupby('month', as_index=False).sum()
new_df_end_station_time = new_df_end_station_time.set_index('month')
new_df_start_station_time = df_station_time.groupby('month', as_index=False).sum()
new_df_start_station_time = new_df_start_station_time.set_index('month')

start_monthly_totals = new_df_start_station_time.sum(axis=1)
# Calculate the proportion of each site
df_start_percentage = new_df_start_station_time.div(start_monthly_totals, axis=0)
df_start_percentage = df_start_percentage*100

df_start_percentage.to_csv('start_percentage.csv')

end_monthly_totals = new_df_end_station_time.sum(axis=1)
# Calculate the proportion of each site
df_end_percentage = new_df_end_station_time.div(end_monthly_totals, axis=0)
df_end_percentage = df_end_percentage*100

df_Difference = df_end_percentage - df_start_percentage
df_Difference = df_Difference.dropna(axis=1)

df_Difference.to_csv('Difference.csv')

start_stats = (
    df_rent.groupby("start_station_name")
    .agg(
        # start_station_id=("start_station_id", "first"),
        start_count=("ride_id", "count"),
        start_member_count=("member_casual", lambda x: (x == "member").sum()),
        start_casual_count=("member_casual", lambda x: (x == "casual").sum()),
        avg_lat=("start_lat", "mean"),
        avg_lng=("start_lng", "mean")
    )
    .reset_index()
)
end_stats = (
    df_rent.groupby("end_station_name")
    .agg(
        end_count=("ride_id", "count"),
        end_member_count=("member_casual", lambda x: (x == "member").sum()),
        end_casual_count=("member_casual", lambda x: (x == "casual").sum()),
        avg_lat=("end_lat", "mean"),
        avg_lng=("end_lng", "mean")
    )
    .reset_index()
)
stats = pd.merge(
    start_stats,
    end_stats,
    left_on=["start_station_name"],
    right_on=["end_station_name"],
    how="inner",
    suffixes=("_start", "_end")
)
stats["avg_lat"] = (stats["avg_lat_start"] + stats["avg_lat_end"]) / 2
stats["avg_lng"] = (stats["avg_lng_start"] + stats["avg_lng_end"]) / 2
stats.drop(columns=["avg_lat_start", "avg_lat_end", "avg_lng_start", "avg_lng_end"], inplace=True)
stats = stats.rename(columns={
    "start_station_name": "station_name"
}).drop(columns=["end_station_name"])

stations = pd.read_csv('sources/stations.csv')
stats_with_type = pd.merge(
    stats,
    stations[['stations', 'type', 'public transportation']],  # Select only relevant columns
    left_on="station_name",  # Match by site name
    right_on="stations",  # Matches the station name column in stations.csv
    how="left"  # Left join, keep all rows in stats
)
stats_with_type = stats_with_type.drop(columns=["stations"])
stats_with_type.to_csv("stats_with_type.csv", index=False)


df_rent_duration = df_rent.copy()
df_rent_duration['started_at'] = pd.to_datetime(df_rent_duration['started_at'])
df_rent_duration['ended_at'] = pd.to_datetime(df_rent_duration['ended_at'])

df_rent_duration['ride_duration'] = (df_rent_duration['ended_at'] - df_rent_duration['started_at']).dt.total_seconds() / 60 # Convert to minutes
df_rent_duration = df_rent_duration[df_rent_duration['ride_duration'] >= 0]
df_rent_duration = df_rent_duration[df_rent_duration['ride_duration'] <= 120]
df_rent_duration.to_csv("df_rent_duration.csv", index=False)
