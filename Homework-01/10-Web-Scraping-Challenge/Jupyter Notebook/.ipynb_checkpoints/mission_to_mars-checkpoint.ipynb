{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from bs4 import BeautifulSoup as bs\n",
    "import requests\n",
    "from splinter import Browser\n",
    "from webdriver_manager.chrome import ChromeDriverManager"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## NASA Mars News\n",
    "\n",
    "* Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[WDM] - Current google-chrome version is 87.0.4280\n",
      "[WDM] - Get LATEST driver version for 87.0.4280\n",
      "[WDM] - There is no [win32] chromedriver for browser 87.0.4280 in cache\n",
      "[WDM] - Get LATEST driver version for 87.0.4280\n",
      "[WDM] - Trying to download new driver from http://chromedriver.storage.googleapis.com/87.0.4280.88/chromedriver_win32.zip\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " \n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[WDM] - Driver has been saved in cache [C:\\Users\\codyt\\.wdm\\drivers\\chromedriver\\win32\\87.0.4280.88]\n"
     ]
    }
   ],
   "source": [
    "executable_path = {'executable_path': ChromeDriverManager().install()}\n",
    "browser = Browser('chrome', **executable_path, headless=False)\n",
    "\n",
    "url = 'https://mars.nasa.gov/news/'\n",
    "browser.visit(url)\n",
    "\n",
    "html = browser.html\n",
    "soup = bs(html, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<li class=\"slide\"><div class=\"image_and_description_container\"><a href=\"/news/8805/moxie-could-help-future-rockets-launch-off-mars/\" target=\"_self\"><div class=\"rollover_description\"><div class=\"rollover_description_inner\">NASA's Perseverance rover carries a device to convert Martian air into oxygen that, if produced on a larger scale, could be used not just for breathing, but also for fuel.</div><div class=\"overlay_arrow\"><img alt=\"More\" src=\"/assets/overlay-arrow.png\"/></div></div><div class=\"list_image\"><img alt=\"Engineers lower MOXIE into the belly of NASA's Perseverance rover.\" src=\"/system/news_items/list_view_images/8805_1-MOXIE-PIA24176-320.gif\"/></div><div class=\"bottom_gradient\"><div><h3>MOXIE Could Help Future Rockets Launch Off Mars</h3></div></div></a><div class=\"list_text\"><div class=\"list_date\">November 24, 2020</div><div class=\"content_title\"><a href=\"/news/8805/moxie-could-help-future-rockets-launch-off-mars/\" target=\"_self\">MOXIE Could Help Future Rockets Launch Off Mars</a></div><div class=\"article_teaser_body\">NASA's Perseverance rover carries a device to convert Martian air into oxygen that, if produced on a larger scale, could be used not just for breathing, but also for fuel.</div></div></div></li>"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "grab_news = soup.select_one('ul.item_list li.slide')\n",
    "grab_news"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'MOXIE Could Help Future Rockets Launch Off Mars'"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "news_title = grab_news.find('div', class_='content_title').a.text\n",
    "news_title"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\"NASA's Perseverance rover carries a device to convert Martian air into oxygen that, if produced on a larger scale, could be used not just for breathing, but also for fuel.\""
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "news_p = grab_news.find('div', class_= 'article_teaser_body').text\n",
    "news_p"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## JPL Mars Space Images - Featured Image\n",
    "\n",
    "\n",
    "* Visit the url for JPL Featured Space Image here.\n",
    "\n",
    "\n",
    "* Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called featured_image_url.\n",
    "\n",
    "\n",
    "* Make sure to find the image url to the full size .jpg image.\n",
    "\n",
    "\n",
    "* Make sure to save a complete url string for this image."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[WDM] - Current google-chrome version is 87.0.4280\n",
      "[WDM] - Get LATEST driver version for 87.0.4280\n",
      "[WDM] - Driver [C:\\Users\\codyt\\.wdm\\drivers\\chromedriver\\win32\\87.0.4280.88\\chromedriver.exe] found in cache\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " \n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "'https://www.jpl.nasa.gov/spaceimages/images/wallpaper/PIA19039-1920x1200.jpg'"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Navigates to featured image website\n",
    "executable_path = {'executable_path': ChromeDriverManager().install()}\n",
    "browser = Browser('chrome', **executable_path, headless=False)\n",
    "\n",
    "featured_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'\n",
    "browser.visit(featured_url)\n",
    "\n",
    "# HTML object\n",
    "html_img = browser.html\n",
    "\n",
    "# Create parser and img url string\n",
    "soup = bs(html_img, 'html.parser')\n",
    "image_url = soup.find('article')['style'].replace('background-image: url(','').replace(');','')[1:-1]\n",
    "\n",
    "featured_url = 'https://www.jpl.nasa.gov' + image_url\n",
    "featured_url\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Mars Facts\n",
    "\n",
    "\n",
    "* Visit the Mars Facts webpage here and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.\n",
    "\n",
    "\n",
    "* Use Pandas to convert the data to a HTML table string."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>0</th>\n",
       "      <th>1</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Equatorial Diameter:</td>\n",
       "      <td>6,792 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Polar Diameter:</td>\n",
       "      <td>6,752 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Mass:</td>\n",
       "      <td>6.39 × 10^23 kg (0.11 Earths)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Moons:</td>\n",
       "      <td>2 (Phobos &amp; Deimos)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Orbit Distance:</td>\n",
       "      <td>227,943,824 km (1.38 AU)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Orbit Period:</td>\n",
       "      <td>687 days (1.9 years)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Surface Temperature:</td>\n",
       "      <td>-87 to -5 °C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>First Record:</td>\n",
       "      <td>2nd millennium BC</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>Recorded By:</td>\n",
       "      <td>Egyptian astronomers</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                      0                              1\n",
       "0  Equatorial Diameter:                       6,792 km\n",
       "1       Polar Diameter:                       6,752 km\n",
       "2                 Mass:  6.39 × 10^23 kg (0.11 Earths)\n",
       "3                Moons:            2 (Phobos & Deimos)\n",
       "4       Orbit Distance:       227,943,824 km (1.38 AU)\n",
       "5         Orbit Period:           687 days (1.9 years)\n",
       "6  Surface Temperature:                   -87 to -5 °C\n",
       "7         First Record:              2nd millennium BC\n",
       "8          Recorded By:           Egyptian astronomers"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# pulls table from website\n",
    "mars_table = pd.read_html('https://space-facts.com/mars/')\n",
    "\n",
    "df = mars_table[0]\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<table border=\"1\" class=\"dataframe\">\n",
      "  <thead>\n",
      "    <tr style=\"text-align: right;\">\n",
      "      <th></th>\n",
      "      <th>0</th>\n",
      "      <th>1</th>\n",
      "    </tr>\n",
      "  </thead>\n",
      "  <tbody>\n",
      "    <tr>\n",
      "      <th>0</th>\n",
      "      <td>Equatorial Diameter:</td>\n",
      "      <td>6,792 km</td>\n",
      "    </tr>\n",
      "    <tr>\n",
      "      <th>1</th>\n",
      "      <td>Polar Diameter:</td>\n",
      "      <td>6,752 km</td>\n",
      "    </tr>\n",
      "    <tr>\n",
      "      <th>2</th>\n",
      "      <td>Mass:</td>\n",
      "      <td>6.39 × 10^23 kg (0.11 Earths)</td>\n",
      "    </tr>\n",
      "    <tr>\n",
      "      <th>3</th>\n",
      "      <td>Moons:</td>\n",
      "      <td>2 (Phobos &amp; Deimos)</td>\n",
      "    </tr>\n",
      "    <tr>\n",
      "      <th>4</th>\n",
      "      <td>Orbit Distance:</td>\n",
      "      <td>227,943,824 km (1.38 AU)</td>\n",
      "    </tr>\n",
      "    <tr>\n",
      "      <th>5</th>\n",
      "      <td>Orbit Period:</td>\n",
      "      <td>687 days (1.9 years)</td>\n",
      "    </tr>\n",
      "    <tr>\n",
      "      <th>6</th>\n",
      "      <td>Surface Temperature:</td>\n",
      "      <td>-87 to -5 °C</td>\n",
      "    </tr>\n",
      "    <tr>\n",
      "      <th>7</th>\n",
      "      <td>First Record:</td>\n",
      "      <td>2nd millennium BC</td>\n",
      "    </tr>\n",
      "    <tr>\n",
      "      <th>8</th>\n",
      "      <td>Recorded By:</td>\n",
      "      <td>Egyptian astronomers</td>\n",
      "    </tr>\n",
      "  </tbody>\n",
      "</table>\n"
     ]
    }
   ],
   "source": [
    "# Converts table to html string\n",
    "mars_table_string = df.to_html()\n",
    "print(mars_table_string)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Mars Hemispheres\n",
    "\n",
    "\n",
    "* Visit the USGS Astrogeology to obtain high resolution images for each of Mar's hemispheres.\n",
    "\n",
    "\n",
    "* You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.\n",
    "\n",
    "\n",
    "* Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys img_url and title.\n",
    "\n",
    "\n",
    "* Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[WDM] - Current google-chrome version is 87.0.4280\n",
      "[WDM] - Get LATEST driver version for 87.0.4280\n",
      "[WDM] - Driver [C:\\Users\\codyt\\.wdm\\drivers\\chromedriver\\win32\\87.0.4280.88\\chromedriver.exe] found in cache\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " \n"
     ]
    }
   ],
   "source": [
    "# Navigates to featured image website\n",
    "executable_path = {'executable_path': ChromeDriverManager().install()}\n",
    "browser = Browser('chrome', **executable_path, headless=False)\n",
    "\n",
    "hemisphere_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'\n",
    "browser.visit(hemisphere_url)\n",
    "\n",
    "# HTML object\n",
    "html_hemisphere = browser.html\n",
    "\n",
    "# Create parser and img url string\n",
    "soup = bs(html_hemisphere, 'html.parser')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "cerb_img = 'https://astrogeology.usgs.gov/cache/images/f5e372a36edfa389625da6d0cc25d905_cerberus_enhanced.tif_full.jpg'\n",
    "schi_img = 'https://astrogeology.usgs.gov/cache/images/3778f7b43bbbc89d6e3cfabb3613ba93_schiaparelli_enhanced.tif_full.jpg'\n",
    "syr_img = 'https://astrogeology.usgs.gov/cache/images/555e6403a6ddd7ba16ddb0e471cadcf7_syrtis_major_enhanced.tif_full.jpg'\n",
    "val_img = 'https://astrogeology.usgs.gov/cache/images/b3c7c6c9138f57b4756be9b9c43e3a48_valles_marineris_enhanced.tif_full.jpg'\n",
    "\n",
    "hemisphere_image_url = [\n",
    "    {'title':'Cerberus Hemisphere', 'img_url': cerb_img},\n",
    "    {'title':'Schiaparelli Hemisphere', 'img_url': schi_img},\n",
    "    {'title':'Syrtis Major Hemisphere', 'img_url': syr_img},\n",
    "    {'title':'Valles Marineris Hemisphere', 'img_url': val_img}\n",
    "]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:PythonData] *",
   "language": "python",
   "name": "conda-env-PythonData-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
