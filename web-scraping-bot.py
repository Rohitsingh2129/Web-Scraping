from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd
import time


website = 'https://www.scrapethissite.com/pages/ajax-javascript/'
path = '/Users/rohit/Downloads/chromedriver' 

driver = webdriver.Chrome(path)
driver.get(website)
year_button = driver.find_element_by_xpath('//a[text()="2015"]')
year_button.click()
movies=driver.find_elements_by_tag_name('tr')

title=[]
nominations=[]
awards=[]

for movie in movies:
  title.append(movie.find_element_by_xpath('.td[1]').text)
  nominations.append(movie.find_element_by_xpath('.td[2]').text)
  awards.append(movie.find_element_by_xpath('.td[3]').text)
  

driver.quit()

df = pd.DataFrame({'title':title,'nominations':nominations,'awards':awards})
df.to_csv('oscars_data.csv', index=False)