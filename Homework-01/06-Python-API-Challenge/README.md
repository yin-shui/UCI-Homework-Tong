# Python API Challenge - What's the Weather Like?

## Part I - WeatherPy

In this example, I'll be creating a Python script to visualize the weather of 500+ cities across the world of varying distance from the equator. To accomplish this, I'll be utilizing a [simple Python library](https://pypi.python.org/pypi/citipy), the [OpenWeatherMap API](https://openweathermap.org/api), and a little common sense to create a representative model of weather across world cities.

First goal is to create a series of scatter plots to showcase the following relationships:

* Temperature (F) vs. Latitude
* Humidity (%) vs. Latitude
* Cloudiness (%) vs. Latitude
* Wind Speed (mph) vs. Latitude

After each plot adding a sentence or two explaining what the code is and analyzing.

Second goal is to run linear regression on each relationship, only this time separating them into Northern Hemisphere (greater than or equal to 0 degrees latitude) and Southern Hemisphere (less than 0 degrees latitude):

* Northern Hemisphere - Temperature (F) vs. Latitude
* Southern Hemisphere - Temperature (F) vs. Latitude
* Northern Hemisphere - Humidity (%) vs. Latitude
* Southern Hemisphere - Humidity (%) vs. Latitude
* Northern Hemisphere - Cloudiness (%) vs. Latitude
* Southern Hemisphere - Cloudiness (%) vs. Latitude
* Northern Hemisphere - Wind Speed (mph) vs. Latitude
* Southern Hemisphere - Wind Speed (mph) vs. Latitude

After each pair of plots explaining what the linear regression is modeling such as any relationships you notice and any other analysis I may have.

### Part II - VacationPy

Now let's use this skill in working with weather data to plan future vacations. Using jupyter-gmaps and the Google Places API for this part of the challenge.

* Create a heat map that displays the humidity for every city from the part I of the challenge.

* Narrow down the DataFrame to find my ideal weather condition. For example:

  * A max temperature lower than 80 degrees but higher than 70.

  * Wind speed less than 10 mph.

  * Zero cloudiness.

  * Drop any rows that don't contain all three conditions. I want to be sure the weather is ideal.

* Using Google Places API to find the first hotel for each city located within 5000 meters of my coordinates.

* Plotting the hotels on top of the humidity heatmap with each pin containing the **Hotel Name**, **City**, and **Country**.







