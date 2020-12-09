# ETL Challenge

New Film Project
Our group has decided to make a new film. But before we commit to a new project, we will gather data on past succesful films. We will look at starting budgets, gross revenue, genres and other relevant information displayed below in our panda data frames and postgres tables later on.

## Extract
All of our data was found on website Kaggle in CSV format:

* Blockbuster CSV

* IMDB CSV

* TMBD CSV

## Transform
After downloading our, data we used a Jupyter Notebook to import the CSVs and created data frames using the Pandas library.

Once they were in Panda dataframe form we did the following to clean and transform our data to make it useful:

* Drop columns we found irrelevant or were duplicates
* Renamed columns to make it look cleaner and match columns on postgres
* We dropped any possible duplicate records from our tables
* Set an index for each of our data frames
* Changed data type on certain columns to be able able to import onto postgres database tables

### After cleaning our data, we imported all dataframes onto postres database tables. Once on postress, we were able to run queries to find useful information like:

* Top 10 highest earning films
* Genre with the highest earnings
* Directors who made top films
* Return on films
* Studios with the higest revenue


