# Excel Challenge:

## Background

Over $2 billion has been raised using the massively successful crowdfunding service, Kickstarter, but not every project has found success. Of the more than 300,000 projects launched on Kickstarter, only a third have made it through the funding process with a positive outcome.

Getting funded on Kickstarter requires meeting or exceeding the project's initial goal, so many organizations spend months looking through past projects in an attempt to discover some trick for finding success. For this week's homework, you will organize and analyze a database of 4,000 past projects in order to uncover any hidden trends.

## Project

Using the Excel table I modified and analyze the data of 4,000 past Kickstarter projects in attempt to uncover some market trends.

* Using conditional formatting to fill each cell in the `state` column with a different color, depending on whether the associated campaign was successful, failed, canceled, or is currently live.

  * Created a new column O called `Percent Funded` that uses a formula to uncover how much money a campaign made to reach its initial goal.

* Using conditional formatting to fill each cell in the `Percent Funded` column using a three-color scale. The scale starts at 0 and be a dark shade of red, transitioning to green at 100, and blue at 200.

  * Created a new column P called `Average Donation` that uses a formula to uncover how much each backer for the project paid on average.

  * Created two new columns, one called `Category` at Q and another called `Sub-Category` at R, which use formulas to split the `Category and Sub-Category` column into two parts.

  * Created a new sheet with a pivot table that will analyze initial worksheet to count how many campaigns were successful, failed, canceled, or are currently live per **category**.

  * Created a stacked column pivot chart that can be filtered by country based on the created table.

  * Created a new sheet with a pivot table that analyzes initial sheet to count how many campaigns were successful, failed, or canceled, or are currently live per **sub-category**.

  * Created a stacked column pivot chart that can be filtered by country and parent-category based on the created table.
  
 * The dates stored within the `deadline` and `launched_at` columns use Unix timestamps. [Using this formula](https://www.extendoffice.com/documents/excel/2473-excel-timestamp-to-date.html) to convert these timestamps to a normal date.

  * Created a new column named `Date Created Conversion` that uses [this formula](https://www.extendoffice.com/documents/excel/2473-excel-timestamp-to-date.html) to convert the data contained within `launched_at` into Excel's date format.

  * Created a new column named `Date Ended Conversion` that uses [this formula](https://www.extendoffice.com/documents/excel/2473-excel-timestamp-to-date.html) to convert the data contained within `deadline` into Excel's date format.
  
  * Created a new sheet with a pivot table with a column of `state`, rows of `Date Created Conversion`, values based on the count of `state`, and filters based on `parent category` and `Years`.

  * Then created a pivot chart line graph that visualizes this new table.
  
