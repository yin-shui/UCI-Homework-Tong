# Build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page.

# Step 1 - Scraping
* Completed initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

* Created a Jupyter Notebook file called mission_to_mars.ipynb and used this to complete all of my scraping and analysis tasks.


# NASA Mars News

* Scraped the NASA Mars News Site and collect the latest News Title and Paragraph Text. Assigned the text to variables that can be referenced.



# JPL Mars Space Images - Featured Image

 * Navigated to JPL Featured Space Image.


* Used splinter to navigate the site and find the image url for the current Featured Mars Image and assigned the url string to a variable called featured_image_url.


* Made sure to find the image full size url for .jpg image.


* Made sure to save a complete url string for this image.


# Mars Facts


* Visited the Mars Facts webpage and used Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.


* Used Pandas to convert the data to a HTML table string.



# Mars Hemispheres


* Visited the USGS Astrogeology site to obtain high resolution images for each of Mar's hemispheres.


* clicked each of the links to the hemispheres in order to find the image url to the full resolution image.


* Saved both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Used a Python dictionary to store the data using the keys img_url and title.


* Appended the dictionary with the image url string and the hemisphere title to a list. This list contains one dictionary for each hemisphere.


# Step 2 - MongoDB and Flask Application
* Used MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.


* Converted Jupyter notebook into a Python script called scrape_mars.py with a function called scrape that will execute all of my scraping code from above and return one Python dictionary containing all of the scraped data.


* Next, I created a route called /scrape that imports scrape_mars.py script and calls scrape function.

* Stored the returned values in Mongo as a Python dictionary.



* Created a root route / that queries my Mongo database and passes the mars data into an HTML template to display the data.


* Created an HTML file called index.html that takes the mars data dictionary and displays all of the data in the appropriate HTML elements. 


