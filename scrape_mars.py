from bs4 import BeautifulSoup
from splinter import Browser
import requests
import os
import pandas as pd
import datetime
import time 


def init_browser():
    executable_path = {"executable_path": "/users/ryanb/downloads/chromedriver"}
    return Browser('chrome', **executable_path, headless=False)

# overall data dictionary 
mars_info = {}


def scrape_news():
    browser = init_browser()

    # URL of page to be scraped
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve elements
    news_title = soup.find('div', class_='content_title').find('a').text
    news_p = soup.find('div', class_='article_teaser_body').text
    
    # Store data in a dictionary
    mars_info['news_title'] = news_title
    mars_info['news_paragraph'] = news_p
    
    # Close the browser after scraping
    browser.quit()
    
    # Return results
    return mars_info

def scrape_image():
    browser = init_browser()

    # URL of page to be scraped
    url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url2)

    # Design an XPATH selector to grab the image
    xpath = '//*[@id="page"]/section[3]/div/ul/li[1]/a/div/div[2]/img'

    # Use splinter to Click the image 
    results = browser.find_by_xpath(xpath)
    img = results[0]
    img.click()

    time.sleep(2)

    # Click the 'more info' button on the page to pull up full image
    browser.click_link_by_partial_text('more info')

    # Design an XPATH selector to grab the image
    xpath2 = '//*[@id="page"]/section[1]/div/article/figure/a/img'

    # Use splinter to Click the image 
    results = browser.find_by_xpath(xpath2)
    img = results[0]
    img.click()

    # Scrape the browser into soup and use soup to find the full resolution image of mars
    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve elements
    featured_image_url = soup.find('img')['src']
    featured_image_url

    mars_info['featured_image_url'] = featured_image_url 

    browser.quit()
    
    return mars_info

def scrape_weather():
    browser = init_browser()

    # URL of page to be scraped
    twitter_url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(twitter_url)

    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve elements
    mars_weather = soup.find('div', class_='js-tweet-text-container').find('p').text
    mars_weather

    mars_info['mars_weather'] = mars_weather

    browser.quit()

    return mars_info


def scrape_facts():

    #dependencies and web page of facts
    facts_url = 'https://space-facts.com/mars/'

    # Use Panda's `read_html` to parse the url
    tables = pd.read_html(facts_url)
    
    # Find the data from tables and assign it to `df`
    mars_df = tables[0]
    mars_df.columns = ['Description', 'Value']

    #Pandas to_html method used to generate HTML tables from DataFrames.
    html_table = mars_df.to_html()
    
    #save dataframe to html file
    mars_df.to_html('table.html')

    mars_info['mars_facts'] = html_table

    return mars_info

hemisphere_image_urls = []

def scrape_hemi_1():
    browser = init_browser()

    astro_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(astro_url)

    # ### Cerberus 
    xpath1 = '//*[@id="product-section"]/div[2]/div[1]/a/img'

    results = browser.find_by_xpath(xpath1)
    img = results[0]
    img.click()

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    title_1 = soup.find('h2', class_='title').text
    title_1

    browser.click_link_by_partial_text('Open')

    # Scrape the browser into soup and use soup to find the full resolution image of mars
    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve elements
    image_1_url = soup.find('img', class_='wide-image')['src']
    image_1_url

    cerberus = {"title":title_1, "img_url": image_1_url}
    hemisphere_image_urls.append(cerberus)

    mars_info['mars_hemispheres'] = hemisphere_image_urls

    browser.quit()

    return mars_info

# ### Schiaparelli 

def scrape_hemi_2():
    browser = init_browser()
    astro_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(astro_url)
    xpath2 = '//*[@id="product-section"]/div[2]/div[2]/a/img'
    results = browser.find_by_xpath(xpath2)
    img = results[0]
    img.click()
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    title_2 = soup.find('h2', class_='title').text
    browser.click_link_by_partial_text('Open')
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    image_2_url = soup.find('img', class_='wide-image')['src']
    Schiaparelli = {"title":title_2, "img_url": image_2_url}
    hemisphere_image_urls.append(Schiaparelli)
    mars_info['mars_hemispheres'] = hemisphere_image_urls
    browser.quit()
    return mars_info

# ### Syrtis Major

def scrape_hemi_3():
    browser = init_browser()
    astro_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(astro_url)
    xpath3 = '//*[@id="product-section"]/div[2]/div[3]/a/img'
    results = browser.find_by_xpath(xpath3)
    img = results[0]
    img.click()
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    title_3 = soup.find('h2', class_='title').text
    browser.click_link_by_partial_text('Open')
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    image_3_url = soup.find('img', class_='wide-image')['src']
    syrtis_major = {"title":title_3, "img_url": image_3_url}
    hemisphere_image_urls.append(syrtis_major)
    mars_info['mars_hemispheres'] = hemisphere_image_urls
    browser.quit()
    return mars_info

# ### Valles Marineris
def scrape_hemi_4():
    browser = init_browser()
    astro_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(astro_url)
    xpath4 = '//*[@id="product-section"]/div[2]/div[4]/a/img'
    results = browser.find_by_xpath(xpath4)
    img = results[0]
    img.click()
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    title_4 = soup.find('h2', class_='title').text
    browser.click_link_by_partial_text('Open')
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    image_4_url = soup.find('img', class_='wide-image')['src']
    valles_marineris = {"title":title_4, "img_url": image_4_url}
    hemisphere_image_urls.append(valles_marineris)
    mars_info['mars_hemispheres'] = hemisphere_image_urls
    browser.quit()
    return mars_info




