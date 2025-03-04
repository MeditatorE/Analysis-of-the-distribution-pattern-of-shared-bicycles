# Analysis-of-the-distribution-pattern-of-shared-bicycles
The goal of this project is to analyze the existing (Washington, DC) bikeshare distribution patterns, identify features associated with the distribution patterns, and attempt to predict optimal future deployment strategies.

## 0. Quick Start
1. Clone this repo
```
git clone https://github.com/MeditatorE/Analysis-of-the-distribution-pattern-of-shared-bicycles.git
cd Analysis-of-the-distribution-pattern-of-shared-bicycles-main
```
2. Install dependency packages
```
pip install -r requirements.txt
```

3. Please download the corresponding data on **[Kaggle](https://www.kaggle.com/datasets/taweilo/capital-bikeshare-dataset-202005202408/data)** and put the data in the [sources folder](https://github.com/MeditatorE/Analysis-of-the-distribution-pattern-of-shared-bicycles/tree/main/sources).

4. Run the [data_analysis.py](https://github.com/MeditatorE/Analysis-of-the-distribution-pattern-of-shared-bicycles/blob/main/data_analysis.py) file, which will generate all the .csv files used for visualization and model training
```
python data_analysis.py
```

5. Download **[Jupyter notebook](https://jupyter.org)** and run
```
jupyter notebook
```

6. Run the [Visualization and Prediction Models.ipynb](https://github.com/MeditatorE/Analysis-of-the-distribution-pattern-of-shared-bicycles/blob/main/Visualization%20and%20Prediction%20Models.ipynb) file, which will visualize the analysis results and train a model that can be used to predict future bike rental volume.

## 1. File Description
- `data_analysis.py`: This file integrates all the modules for data analysis. It will generate all the .csv files for model training and data visualization.

- `Visualization and Prediction Models.ipynb`: This file integrates all the codes for data visualization and model training. Please run [data_analysis.py](https://github.com/MeditatorE/Analysis-of-the-distribution-pattern-of-shared-bicycles/blob/main/data_analysis.py) before running this file.

- `data_analysis.ipynb`: This file is the original file used for data analysis. It integrates all the codes in this project, including the abandoned parts. It also contains some conclusions of this analysis. If you are interested, you can take a look at it.

- `Member_new.ipynb`: This file is a supplementary file for membership analysis, and its content has been integrated into [Visualization and Prediction Models.ipynb](https://github.com/MeditatorE/Analysis-of-the-distribution-pattern-of-shared-bicycles/blob/main/Visualization%20and%20Prediction%20Models.ipynb).

- `sources`: This folder is used to store the original data. You should download the original data on **[Kaggle](https://www.kaggle.com/datasets/taweilo/capital-bikeshare-dataset-202005202408/data)** and put it in this folder.

- `csv`: This folder stores almost all (except those with huge amounts of data) csv files generated by [data_analysis.py](https://github.com/MeditatorE/Analysis-of-the-distribution-pattern-of-shared-bicycles/blob/main/data_analysis.py).

- `html`: This folder stores interactive visualization station data (marked on the map). They are in HTML format. You need to download the HTML file and open it with a browser.

- `result_picture`: This file stores the visualization results of all data analysis. All files are in png image format.

**All the dependent modules of this project are as follows:**
```
branca==0.8.0
folium==0.18.0
matplotlib==3.6.2
numpy==1.23.5
pandas==1.5.3
prophet==1.1.6
scikit_learn==1.3.2
scipy==1.9.1
seaborn==0.13.2
tqdm==4.64.1
xgboost==2.1.3
```

**The specific structure of all files is as follows:**
```
/main/
├── Member_new.ipynb
├── Visualization and Prediction Models.ipynb
├── csv file
│   ├── Difference.csv
│   ├── df_date_Clear.csv
│   ├── df_date_Cloudy.csv
│   ├── df_date_Partially_cloudy.csv
│   ├── df_date_Rain.csv
│   ├── df_date_Snow.csv
│   ├── df_date_Wind.csv
│   ├── df_date_rent_num.csv
│   ├── df_date_weather_num.csv
│   ├── df_member_casual.csv
│   ├── df_member_start.csv
│   ├── df_month_time.csv
│   ├── df_pro.csv
│   ├── df_station_time.csv
│   ├── start_percentage.csv
│   └── stats_with_type.csv
├── data_analysis.ipynb
├── data_analysis.py
├── html
│   ├── my_map_end.html
│   ├── my_map_start.html
│   ├── washington_map_in_out.html
│   ├── washington_map_member.html
│   └── washington_map_type.html
├── result_picture
│   ├── Actual vs Predicted Rental Counts.png
│   ├── Difference.png
│   ├── Feature Importance XGBoost.png
│   ├── Percentage of rentals.png
│   ├── Prophet_result.png
│   ├── Ride_duration.png
│   ├── Station_Type_rent.png
│   ├── full Difference.png
│   ├── full Percentage of rentals.png
│   ├── heatmap_rental_quantities.png
│   ├── heatmap_station_time.png
│   ├── member_barchart.png
│   ├── member_station.png
│   ├── new_heatmap_station_time.png
│   ├── total.png
│   ├── total_gaussian.png
│   ├── weather_avg.png
│   └── weather_rent_num.png
└── sources
    ├── daily_rent_detail.csv
    ├── station_list.csv
    ├── stations.csv
    ├── usage_frequency.csv
    └── weather.csv
```

## 2. Dataset Overview
The data volume of this project exceeds 10 million, about 16,000,000 data. We downloaded this data from **[Kaggle](https://www.kaggle.com/datasets/taweilo/capital-bikeshare-dataset-202005202408/data)**, including:

**File information:** 4 files /duration 2020/05~2024/08

**Daily rent data**

- `ride_id`: ride id

- `rideable_type`: ride type. I.e. docked_bike, electric_bike, classic_bike

- `started_at`: start date and time

- `ended_at`: end date and time

- `start_station_name`: starting station name

- `start_station_id`: starting station id

- `end_station_name`: ending station name

- `end_station_id`: ending station id

- `start_lat`: start latitude

- `start_lng`: start longitude

- `end_lat`: end latitude

- `end_lng`: end longitude

- `member_casual`: Indicates whether user was a "registered" member (Annual Member, 30-Day Member or Day Key Member) or a "casual" rider (Single Trip, 24-Hour Pass, 3-Day Pass or 5-Day Pass). I.e. casual, member

**Data source:** [https://capitalbikeshare.com/system-data](https://capitalbikeshare.com/system-data)

**Station list**

- `station_id`: station id

- `station_name`: station name

**Data source:** organized from Daily rent data

**Usage frequency**

- `date`: date

- `station_name`: station name

- `pickup_counts`: daily pickup of the station

- `dropoff_counts`: daily dropoff of the station

**Data source:** organized from Daily rent data

**Weather**

- `name`: location

- `datetime`: date

- `tempmax`: maximum temperature at the location.

- `tempmin`: minimum temperature at the location.

- `temp`: temperature at the location. Daily values are average values (mean) for the day.

- `feelslikemax`: maximum feels like temperature at the location.

- `feelslikemin`: minimum feels like temperature at the location.

- `feelslike`: what the temperature feels like accounting for heat index or wind chill. Daily values are average values (mean) for the day.

- `dew`: dew point temperature

- `humidity`: relative humidity in %

- `precip`: the amount of liquid precipitation that fell or is predicted to fall in the period.

- `precipprob`: the likelihood of measurable precipitation ranging from 0% to 100%

- `precipcover`: the proportion of hours where there was non-zero precipitation

- `preciptype`: an array indicating the type(s) of precipitation expected or that occurred.

- `snow`: the amount of snow that fell or is predicted to fall

- `snowdepth`: the depth of snow on the ground

- `windgust`: instantaneous wind speed at a location

- `windspeed`: the sustained wind speed measured as the average windspeed that occurs during the preceding one to two minutes. Daily values are the maximum hourly value for the day.

- `winddir`: direction from which the wind is blowing

- `sealevelpressure`: the sea level atmospheric or barometric pressure in millibars

- `cloudcover`: the sea level atmospheric or barometric pressure in millibars

- `visibility`: distance at which distant objects are visible

- `solarradiation`: (W/m2) the solar radiation power at the instantaneous moment of the observation (or forecast prediction)

- `solarenergy`: (MJ /m2 ) indicates the total energy from the sun that builds up over a day.

- `uvindex`: a value between 0 and 10 indicating the level of ultra violet (UV) exposure for that day.

- `severerisk:` a value between 0 and 100 representing the risk of convective storms

- `sunrise`: the formatted time of the sunrise

- `sunset`: the formatted time of the sunset

- `moonphase`: represents the fractional portion through the current moon lunation cycle ranging from 0 (the new moon) to 0.5 (the full moon) and back to 1 (the next new moon)

- `conditions`: textual representation of the weather conditions.

- `description`: longer text descriptions suitable for displaying in weather displays

- `icon`: a fixed, machine readable summary that can be used to display an icon

- `stations`: the weather stations used when collecting a historical observation record

**Parameters information:** [https://www.visualcrossing.com/resources/documentation/weather-api/timeline-weather-api/](https://www.visualcrossing.com/resources/documentation/weather-api/timeline-weather-api/)

**Data source:** [https://www.visualcrossing.com/](https://www.visualcrossing.com/)

## 3. Data analysis
### 3.1 Analysis of rental quantity
We analyzed the total rental data over the past four years and found that the data has seasonal cyclical changes and has been increasing over the past four years, so we Gaussian smoothed the data to calculate the growth rate. Finally, we found that the **annual growth rate was 12.5%**, which means that our first distribution strategy is that the total number of bicycles put into use should increase by 12.5% ​​each year.
![](https://github.com/MeditatorE/Analysis-of-the-distribution-pattern-of-shared-bicycles/blob/main/result_picture/total.png)
![](https://github.com/MeditatorE/Analysis-of-the-distribution-pattern-of-shared-bicycles/blob/main/result_picture/total_gaussian.png)


We then use heat maps to represent the periodic changes in the number of bicycle rentals over the course of a year and day. We aggregate rental records that fall within the same half-hour interval each month. It can be seen that during the year, the rental volume reaches the peak in summer and the trough in winter, **further indicating that the rental volume is greatly affected by the season**; in the daily cycle, the rental volume increases significantly during the morning peak and evening peak hours. Especially the evening peak is the most obvious peak period.
![](https://github.com/MeditatorE/Analysis-of-the-distribution-pattern-of-shared-bicycles/blob/main/result_picture/heatmap_rental_quantities.png)


### 3.2 Analyze the impact of weather on rental quantity
As can be seen from the bar chart, snowy days have the greatest impact on bicycle rental volume, which is only 28% of the average value. The second is windy days, with rental volume of 56% of the average value. In addition, cloudy and rainy days also have lower rental volume than the average, while sunny and cloudy days have higher rental volume than the average.
![](https://github.com/MeditatorE/Analysis-of-the-distribution-pattern-of-shared-bicycles/blob/main/result_picture/weather_avg.png)
![](https://github.com/MeditatorE/Analysis-of-the-distribution-pattern-of-shared-bicycles/blob/main/result_picture/8d43c3ce-263c-4713-83ce-6b617b9e48ab.png)

We also visualized the weather for each day and the number of rentals for that day.
![](https://github.com/MeditatorE/Analysis-of-the-distribution-pattern-of-shared-bicycles/blob/main/result_picture/weather_rent_num.png)


#### 3.2.1 Quantifying the impact of weather on rental numbers
To quantify the impact of weather on rental volume, we use **significance analysis** to evaluate the impact
```
# One-way ANOVA
f_stat, p_value = f_oneway(category_partially_cloudy, category_rain, category_clear_day, category_cloudy, category_snow, category_wind)
print(f"F-statistic: {f_stat:.3f}, P-value: {p_value:.3f}")

# Interpretation of results
alpha = 0.05
if p_value < alpha:
    print("Differences between categories are statistically significant (reject the null hypothesis)")
else:
    print("The difference between different categories is not significant (the null hypothesis cannot be rejected)")
```
```
F-statistic: 26.840, P-value: 0.000
Differences between categories are statistically significant (reject the null hypothesis)
```
**The conclusion is that weather has an impact on travel, and the F-statistic is 26, which means that the variance between groups is 26 times the variance within the group. This shows that the impact of weather on travel is relatively significant.**

In addition, we also counted the impact of different weather conditions on travel. The significance of the impact of different weather conditions on rental volume is as follows:
```
partially_cloudy    F-statistic: 0.560, P-value: 0.454
rain                F-statistic: 4.024, P-value: 0.045
cloudy              F-statistic: 10.340, P-value: 0.002
snow                F-statistic: 87.119, P-value: 0.000
wind                F-statistic: 2.299, P-value: 0.134
```


#### 3.2.2 Quantifying the importance of the impact of different weather features on leasing volumes
Now we know that the daily bicycle rental volume is affected by season (3.1 Conclusion) and weather (3.2 Conclusion), and we have weather data for each of the past four years. There are 24 features in total, namely
```
features = [
"tempmax", "tempmin", "temp", "feelslikemax", "feelslikemin", "feelslike",
"dew", "humidity", "precip", "precipprob", "precipcover", "preciptype",
"snow", "snowdepth", "windgust", "windspeed", "winddir", "sealevelpressure",
"cloudcover", "visibility", "solarradiation", "solarenergy", "uvindex",
"severerisk" ]
```


We need to evaluate the impact index of each feature on the weather. We use **importance evaluation** to quantify this indicator and use the **XGBoost** model to evaluate the importance of different features. The results are:
```
# Initialize the XGBoost regressor
xgb_model = XGBRegressor(
    n_estimators=1000,      # Number of trees
    learning_rate=0.01,     # Learning Rate
    max_depth=5,           # Maximum depth of the tree
    random_state=42
)
```
```
Feature: tempmax, Importance: 0.03388049080967903
Feature: tempmin, Importance: 0.012917473912239075
Feature: temp, Importance: 0.04539528116583824
Feature: feelslikemax, Importance: 0.006318486295640469
Feature: feelslikemin, Importance: 0.045982446521520615
Feature: feelslike, Importance: 0.12540742754936218
Feature: dew, Importance: 0.006908854469656944
Feature: humidity, Importance: 0.006303189788013697
Feature: precip, Importance: 0.017374780029058456
Feature: precipprob, Importance: 0.0
Feature: precipcover, Importance: 0.03359576687216759
Feature: preciptype, Importance: 0.006663008593022823
Feature: snow, Importance: 0.0011690628016367555
Feature: snowdepth, Importance: 0.0022235941141843796
Feature: windgust, Importance: 0.00928246509283781
Feature: windspeed, Importance: 0.006737611256539822
Feature: winddir, Importance: 0.0067607685923576355
Feature: sealevelpressure, Importance: 0.006391626317054033
Feature: cloudcover, Importance: 0.008458642289042473
Feature: visibility, Importance: 0.014334036037325859
Feature: solarradiation, Importance: 0.03705691918730736
Feature: solarenergy, Importance: 0.03428182005882263
Feature: uvindex, Importance: 0.3164701759815216
Feature: severerisk, Importance: 0.2160860151052475
```
![](https://github.com/MeditatorE/Analysis-of-the-distribution-pattern-of-shared-bicycles/blob/main/result_picture/Feature%20Importance%20XGBoost.png)


The error of this model is:
```
MSE: 4627447.087644517
RMSE: 2151.1501778454513
```
![](https://github.com/MeditatorE/Analysis-of-the-distribution-pattern-of-shared-bicycles/blob/main/result_picture/Actual%20vs%20Predicted%20Rental%20Counts.png)


### 3.3 Forecasting future rental volumes
After getting the importance of each feature, we try to use seasonal and weather data to predict future bicycle usage. Here we use the **Prophet** model

**Why use Prophet model?**

The Prophet model is a time series forecasting model designed for processing data with obvious seasonal components and trend changes. Our data is a seasonal periodic change data, which is very suitable for this model.

We then **add each important weather feature** as a regression variable for Prophet training. The training results are:
```
# Define the Prophet model
model = Prophet()

# Add all weather-related regressors
weather_features = [
"uvindex", "severerisk", "feelslike", "solarenergy", "temp",
"feelslikemin", "tempmax", "solarradiation", "precipcover",
"tempmin", "precip", "visibility", "preciptype", "cloudcover",
"windspeed" ]

# Add each feature as a regressor in Prophet
for feature in weather_features:
    model.add_regressor(feature)
```
```
Mean Squared Error (MSE): 3907222.9902083008
Mean Absolute Error (MAE): 1458.3266245041264
R² Score: 0.8432569983242107
```
This result shows that **the fit of our model can reach 84.3%**, the MAE is 1458, and the average rental volume for all days is 10156, so the **accuracy of our model can exceed 85%**.

![](https://github.com/MeditatorE/Analysis-of-the-distribution-pattern-of-shared-bicycles/blob/main/result_picture/Prophet_result.png)


### 3.4 The optimal bicycle distribution problem
We can already predict the daily bicycle usage based on the weather (this data can be known in advance because there is a weather forecast), so how do we allocate bicycles? (Optimal distribution problem)

We group the data by month and calculate the total rental volume for this month, and then calculate the proportion of each site to the total rental volume. The results are as follows (Since the amount of data is too huge, we choose the first 100 stations for display)
![](https://github.com/MeditatorE/Analysis-of-the-distribution-pattern-of-shared-bicycles/blob/main/result_picture/Percentage%20of%20rentals.png)

#### 3.4.1 Optimal Distribution Strategy
**Then, based on our predicted data and the rental volume share of each station each month, we can calculate the recommended number of bicycles to be deployed at any station on any given day, that is, the optimal distribution strategy.**

### 3.5 The best scheduling strategy for each month
#### 3.5.1 Why not schedule by day?

According to the following heat map, the peak hours of each station are in the same time period (morning peak, evening peak), so there is no need to schedule between different stations within a day.
![](https://github.com/MeditatorE/Analysis-of-the-distribution-pattern-of-shared-bicycles/blob/main/result_picture/new_heatmap_station_time.png)

The number changes for each site vary from month to month. **For example, in the heat map below, the number of leases for the sites in the red box in the heat map below was less than that of the sites in the blue box in January and February; however, it increased significantly in March and beyond, exceeding the number of sites in the blue box.** This illustrates the need to schedule between different sites each month.
![](https://github.com/MeditatorE/Analysis-of-the-distribution-pattern-of-shared-bicycles/blob/main/result_picture/heatmap_station_time_marked.png)

#### 3.5.2 Optimal Scheduling Strategy
We also calculated the proportion of returns to the total number of returns at each station (theoretically, the total number of returns should be equal to the total number of rentals), and then **subtracted the proportion of rentals to the total number of rentals at each station from the proportion of returns to the total number of returns at each station to find out whether the number of bicycles at each station is increasing or decreasing each month.** The figure below shows the data for the top 100 stations.
![](https://github.com/MeditatorE/Analysis-of-the-distribution-pattern-of-shared-bicycles/blob/main/result_picture/Difference.png)
In the figure, the blue part means that the number of bicycles at this station is decreasing, the red part means that the number of bicycles is increasing, and the white part means that there is no change. **According to this figure, if the data in a blue grid is 0.1%, it means that the number of bicycles at this station has decreased by 0.1% of the amount put in this month.**

We show the flow of bicycles in and out of each station on the map. **It can be seen that the stations with bicycle inflow are concentrated in the urban area, while the stations with bicycle outflow are concentrated in the suburbs (such as Columbia Heights, Woodley Park).** 

We have provided an interactive map for this section. Please download [washington_map_in_out.html](https://github.com/MeditatorE/Analysis-of-the-distribution-pattern-of-shared-bicycles/blob/main/html/washington_map_in_out.html) and open it in your browser.
![](https://github.com/MeditatorE/Analysis-of-the-distribution-pattern-of-shared-bicycles/blob/main/result_picture/washington_map_in_out.png)

#### 3.5.3 Conclusion
**So we get the best scheduling strategy: before the beginning of each month, the bicycles in the red station should be transferred to the blue station according to the predicted increase/decrease percentage of the month.**

### 3.6 Member/Non-member analysis
#### 3.6.1 Membership ratio analysis
In our data, each rental record also includes whether the user is a member. We analyze the behavioral differences between members and non-members to better help bicycle rental companies formulate marketing strategies, such as tapping into potential member users, optimizing member benefits, and personalized push messages.

Among all rental records, **60% are used by members and 40% are non-members.** Although members account for the majority, there are still a considerable number of non-members. **Our goal is to analyze the behavior patterns of members and find as many users as possible who are likely to become members among non-members.** Companies can push more discounts to these people to attract them to become members in order to gain greater profits.
![](https://github.com/MeditatorE/Analysis-of-the-distribution-pattern-of-shared-bicycles/blob/main/result_picture/member_barchart.png)

#### 3.6.2 User behavior analysis
We made statistics on the riding time of each record and drew a histogram. Most rides are under 20 minutes. There are significantly more members than non-members who ride for less than 30 minutes; and more non-members for more than 30 minutes.

![](https://github.com/MeditatorE/Analysis-of-the-distribution-pattern-of-shared-bicycles/blob/main/result_picture/Ride_duration_marked.png)

**Conclusion:** 

**It can be speculated that when users need to ride a lot of short distances (such as commuting to get off work every day), they are more inclined to join the membership. Users who occasionally go on long rides may not choose to become a member.**

**But there is still a large number of short-distance cyclists who are not members. For non-member users who often ride short distances, they should be attracted to become members. For example, advertisements can be placed at morning and evening peak hours at office area sites. Although the proportion is small, there are still a certain number of long-distance cyclists. Different strategies can be used, such as "you can enjoy discounts on membership fees if you ride for more than one hour" to attract users to gradually convert from a long-distance ride to a member.**

#### 3.6.3 Analysis of the number of members at different stations
This graph shows the number of members and non-members by starting site (sorted by the number of members in descending order, taking the top 100 sites). As you can see from the graph, most sites have more members. But there are also some sites that have more non-members.

![](https://github.com/MeditatorE/Analysis-of-the-distribution-pattern-of-shared-bicycles/blob/main/result_picture/member_station.png)

We further counted the stations with more non-member riders, accounting for **37.03%** of all stations
```
Percentage of such stations among all stations: 37.03%
```

On this map, we can see more intuitively that most of the sites have more members (orange), while a few sites with more non-members (blue) are concentrated around famous attractions in Washington DC, such as the Lincoln Memorial, which has the largest number of non-members. **It can be inferred that these non-members may include a large number of tourists from other places.**

We have provided an interactive map for this section. Please download [washington_map_member.html](https://github.com/MeditatorE/Analysis-of-the-distribution-pattern-of-shared-bicycles/blob/main/html/washington_map_member.html) and open it in your browser.

![](https://github.com/MeditatorE/Analysis-of-the-distribution-pattern-of-shared-bicycles/blob/main/result_picture/washington_map_member.png)

**Conclusion:** 

**For users who often ride at stations with a large number of members, targeted advertising can be placed to attract them to join. For stations near tourist attractions where the majority of users are non-members, other plans can be adopted, such as short-term membership plans and recommended routes to tourist attractions.**

#### 3.6.4 Summary
**In summary, through the analysis of member and non-member behaviors, car rental companies can target potential member users from different angles such as riding time and riding stations to gain more profits and visibility.**

### 3.7 Station Category Analysis
We also artificially divided the stations into three categories: work, entertainment, and life based on the facilities around the stations. The plan is to find out the possible influencing factors of the station type stack usage. The bar chart below shows that the usage of the three types of stations is not much different, among which work is the most, and life is slightly lower than the other two. **It can be seen that the number of the three types of stations is not much different.**

![](https://github.com/MeditatorE/Analysis-of-the-distribution-pattern-of-shared-bicycles/blob/main/result_picture/Station_Type_rent.png)

Draw three types of stations on the map:

We have provided an interactive map for this section. Please download [washington_map_type.html](https://github.com/MeditatorE/Analysis-of-the-distribution-pattern-of-shared-bicycles/blob/main/html/washington_map_type.html) and open it in your browser.

![](https://github.com/MeditatorE/Analysis-of-the-distribution-pattern-of-shared-bicycles/blob/main/result_picture/washington_map_type.png)

**Conclusion:** 

**From this figure, we can see that the station type has little effect on the number of car rentals. It is not necessary to use the station category as a feature to predict the number of car rentals.**

## 4. Conclusion
This project has fully analyzed the existing data and achieved prediction of future rental volume by training the Prophe model with an accuracy of over **85%** (**3.3**). Combined with our other analyses, we have given the corresponding **optimal distribution strategy** (**3.4.1**), **optimal scheduling strategy** (**3.5.3**), and **push strategy for non-member users** (**3.6.2 & 3.6.3 & 3.6.4**).

## Reference
Dataset: [https://www.kaggle.com/datasets/taweilo/capital-bikeshare-dataset-202005202408/data](https://www.kaggle.com/datasets/taweilo/capital-bikeshare-dataset-202005202408/data)





