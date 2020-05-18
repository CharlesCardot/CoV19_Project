# CoV19_Project

# Introduction
This project includes the python script and corresponding csv file needed to perform a linear fit of daily new CoV19 cases within the United States. 
Data is pulled from https://www.worldometers.info/coronavirus/country/us/. The linear fit is performed via least squares refinement through the scipy python library.

# Notes
The output of the python script is the predicted number of days remianing and the date on which the daily new cases will reach zero.

# UPDATE
Previously a manually updated csv file was used, but due to the tedium of manually checking daily updates on the worldometer website a webscraper using beautifulsoup has
been implimented to automatically pull the information from the worldometer website.

