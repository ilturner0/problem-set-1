'''
You will run this problem set from main.py so set things up accordingly
'''

import src.extract
import src.transform_load
import pandas as pd

# Call functions / instanciate objects from the two analysis .py files
def main():
        """
        Executes the ETL processes defined in extract.py and transform_load.py. After ETL, generates a line plot, scatter plot, and heatmap. Finally, prints a message to screen detailing insights from the plot.

        Parameters:
                None
        
        Returns:
                N/A
        """
        # Call functions from extract.py
        weather=src.extract.extract_weather_data()
        transit=src.extract.extract_transit_data()

        # Call functions from transform_load.py
        joined=src.transform_load.joinTabs(weather, transit)
        src.transform_load.linePlot(joined)
        src.transform_load.scatterPlot(joined)
        src.transform_load.heatmap(joined)
        src.transform_load.printMessage()




if __name__ == "__main__":
    main()