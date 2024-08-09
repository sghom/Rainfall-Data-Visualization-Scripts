# sitka_temps_rainfall
Visualization of Sitka's Temperature and Rainfall Fluctuations in 2018

Data Visualization Scripts
This repository contains Python scripts for visualizing weather data from various sources. The scripts use matplotlib to create line plots of temperature and precipitation data.

Overview
The repository includes three scripts for plotting weather data:

1. Daily High and Low Temperatures - Death Valley (2018)
File: death_valley_2018_simple.csv
Description: This script reads daily high and low temperatures from a CSV file and plots them using a line graph. The high temperatures are plotted in red, and the low temperatures are plotted in blue. The area between the high and low temperatures is shaded in blue with 10% opacity.
Output: A line plot showing daily high and low temperatures for Death Valley, CA, in 2018.

2. Daily High and Low Temperatures - Sitka (2018)
File: sitka_weather_2018_simple.csv
Description: This script reads daily high and low temperatures from a CSV file for Sitka, Alaska, and plots them using a line graph. Similar to the Death Valley plot, high temperatures are in red, and low temperatures are in blue. The area between the high and low temperatures is shaded in blue with 10% opacity.
Output: A line plot showing daily high and low temperatures for Sitka, AK, in 2018.

3. Amount of Rainfall - Sitka (2018)
File: sitka_weather_2018_simple.csv
Description: This script reads daily rainfall data from a CSV file and plots it using a line graph. The amount of rainfall is plotted in green.
Output: A line plot showing daily rainfall amounts for Sitka, AK, in 2018.

- Requirements
Python 3.x
matplotlib library
CSV files for input data

- Usage
Download or clone the repository.
Ensure the CSV files are located in the specified paths.
Run the scripts using Python. Each script will display a plot based on the data from the corresponding CSV file.

- Notes
Adjust the file paths in the scripts to match your local directory structure.
Each script includes basic error handling to manage missing or malformed data.
