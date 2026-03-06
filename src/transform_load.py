'''
PART 2: Merge and transform the data
- Read in the two datasets from /data into two separate dataframes
- Profile, clean, and standardize date fields for both as needed
- Merge the two dataframe for the date range 10/1/2024 - 10/31/2025
- Conduct EDA to understand the relationship between weather and transit ridership over time
-- Create a line plot of daily transit ridership and daily average temperature over the whole time period
-- For February 2025, create a scatterplot of daily transit ridership vs. precipitation
-- Create a correlation heatmap of all numeric features in the merged dataframe
-- Load the merged dataframe as a CSV into /data
-- In a print statement, summarize any interesting trends you see in the merged dataset

'''
import pandas as pd
import src.extract
import matplotlib.pyplot as plt
import seaborn as sns

#Write your code below
def joinTabs(weather, transit):
    """
    
    Merges the weather and transit dataframes by date
    ----------------------------------------------------

    Parameters: 
        weather : dataframe
            The extracted data from the visualcrossing API.
        transit : dataframe
            The extracted data from the Chicago Transit Authority.

    ----------------------------------------------------

    Returns:
        Merged dataframe
    """
    weather['datetime']=pd.to_datetime(weather['datetime'])
    transit['service_date']=pd.to_datetime(transit['service_date'])
    joined=weather.merge(transit, how='inner', left_on='datetime', right_on='service_date')
    joined.to_csv(r'src/data/joined.csv')
    return joined

def linePlot(joinedData):
    """
    Creates and displays a line plot of daily ridership and temperature for the date range 10/1/2024-10/31/2025.
    -----------------------------------------------------------------------------

    Parameters: 
        joinedData
    (joinedData is the resulting dataframe from merging the weather and transit data)
    ------------------------------------------------------------------------------

    Output:
    Prints line plot to screen.
    
    """
    plt.plot(joinedData['datetime'], joinedData['total_rides']/10000, label='Rides (ten thousands)') #To scale plot properly, total rides is displayed in tens of thousands.
    plt.plot(joinedData['datetime'], joinedData['temp'], label='Temp')
    plt.ylim(0, 150)
    plt.xlabel('Time')
    plt.legend()
    plt.show()


def scatterPlot(joinedData):
    """
    Creates and displays a scatter plot of daily ridership and precipitation for the month of February, 2025.
    -----------------------------------------------------------------------------

    Parameters: 
        joinedData : dataframe
            joinedData is the resulting dataframe from merging the weather and transit data in the joinTabs function.
    ------------------------------------------------------------------------------

    Output:
    Prints scatter plot to screen.
    
    """
    feb25=joinedData.loc[(joinedData['datetime'].dt.month==2)&(joinedData['datetime'].dt.year==2025)]
    plt.scatter(feb25['total_rides']/10000, feb25['precip'], color='blue', marker='o') #To scale plot properly, total rides is displayed in tens of thousands.
    plt.xlim(0, 150)
    plt.ylim(0, 0.1)
    plt.xlabel('Daily ridership (ten thousands)')
    plt.ylabel('Preciptation')
    plt.show()

def heatmap(joinedData):
    """
    Creates and displays a heatmap of all numeric features in the joined dataframe.
    -----------------------------------------------------------------------------

    Parameters: 
        joinedData : dataframe
            joinedData is the resulting dataframe from merging the weather and transit data in the joinTabs function.
    ------------------------------------------------------------------------------

    Output:
    Prints heatmap to screen.
    
    """
    joinedData2=joinedData.drop(columns=['name', 'datetime', 'preciptype', 'sunrise', 'sunset', 'conditions', 'description', 'icon', 'stations', 'service_date', 'day_type'])
    corrMat=joinedData2.corr()
    sns.heatmap(corrMat)
    plt.show()

def printMessage():
    """
    Prints a message to the screen detailing interesting trends in the merged data.
    -----------------------------------------------------------------------------

    Parameters: 
        None
    ------------------------------------------------------------------------------

    Output:
    Prints message to screen.
    
    """
    print("An interesting trend that I noticed when creating the line plot is the sort of inverse relationship taking place between ridership and temperature at the peaks and valleys of the lines. When temperature is at its local minimum, then ridership is at its peak. Normally this is what you'd expect, but what makes this more interesting is that ridership did not increase generally during the winter months when the temperature was lowest. The number of rides during this period are lower than the number of rides during the fall months.")
    print("\n The relationship between ridership and precipitation is also very interesting. From the plot we can see that there is a slight positive correlation between the two variables, but the data point with the highest precipitation is more in the center of the distribution. I am also unsure of the units that are being used for precipitation. I didn't see it shown in the API documentation. Knowing the units would make the plot more intelligible.")
