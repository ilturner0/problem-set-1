PROBLEM SET #1: ETL Weather and Transit Data

This code package performs the extract, transform, and load process for weather data and transit data. 

1. The weather data is collected via visualcrossing's weather API, and the transit data is collected as a csv directly from the Chicago Transit Authority.

2. Both datasets are read as CSVs into separate pandas dataframes. Each dataframe then has the date field standardized using pd.to_datetime. This is to ensure that both date columns are in the same format.

3. The two datasets are then merged in an inner join using the date column as the field to join on. The merged dataset is then stored in /data.

4. A variety of visualizations are generated using the merged dataset and are printed to the screen.

5. Finally, a message containing insights derived from the visualizations is printed to the screen.



Instructions: 
- Clone the Problem Set 1 code package from GitHub into VS Code
- You should align the code package with your GitHub account 
- This problem set requires you to ETL two datasets: one is weather data and other is transit data
- - Remember to spend some time to get to know the data, its source, and any documentation
- Each of the two .py files in `/src` contain instructions for the exepected code you are to write
- The problem set you turn in needs to fully run from main.py in order to receive credit

Things to remember: 
- Make sure to setup a virtual environment as discussed in the Course Tech Setup lecture. Here's a short article as an additional resource: 
https://www.freecodecamp.org/news/python-requirementstxt-explained/
- All data file outputs (CSV, parquet, JSON, etc.) need to include a unique ID for each entity / row

When you are done:
- Don't forget to set your requirements.txt file using `pip freeze > requirements.txt`
- Commit and push to your GitHub account
- - You should have separate commit messages for each of the two analyses (at the very least)  

Submission: 
You will submit the URL for this repo in your GitHub in ELMS.

Grading: 
We will only run main.py, so make sure that you stucture this correctly and push your final code. We will look at your code, its output, and make sure you've output the correct CSV files. Credit will be given for adhering to the course's Code Standards and Data Standards, using GitHub correctly, and producing the correct output, among other considerations. 


