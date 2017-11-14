from selenium import webdriver
import link
import gc

from selenium.webdriver.chrome.options import Options

def fsearch(travel_airports, back_airports, travel_date, back_date):
        
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1366x768")
    """
    driver = webdriver.PhantomJS(executable_path='./phantomjs/bin/phantomjs')
    #driver = webdriver.Chrome(executable_path='./chromedriver_linux64/chromedriver')
    
    driver.implicitly_wait(10) #wait 10 seconds when doing a find_element before carrying on
    driver.get(link.search_link(travel_airports, back_airports, travel_date, back_date))
    
    link_list = driver.find_elements_by_xpath("//a[@elm='il']") # elm='il' is unique for the class containing the flight links
    price_class = link_list[0].get_attribute("class")[0:8] # Returns only the first 8 chars of the class name. This is the beggining of the name for all inner classes
    price_list =  driver.find_elements_by_class_name(price_class+"d-Ab") # A class name ending in 'd-Ab' is unique for classes containing a flight price

    return(price_list, link_list)
    
# Selects the lowest price and returns the price and corresponding flight link
def fsearch_lowprice(travel_airports, back_airports, travel_date, back_date):
    
    price_list, link_list = fsearch(travel_airports, back_airports, travel_date, back_date)
    
    counter = 0
    low_price = 999999999.0
    low_link = "N/A"
    for price in price_list:
        
        # Removes symbols from string and converts it to float for comparison
        float_price = float(price.text.translate({ord(i):None for i in '$,'})) 
        
        if float_price < low_price:
            low_price = float_price
            low_link = link_list[counter].get_attribute("href")
            
        counter += 1
    
    return(low_price,low_link)
    

            
        
