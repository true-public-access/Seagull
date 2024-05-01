


import selenium
from selenium import webdriver
   
try:
    fireFoxoptions = webdriver.Firefox()
    #fireFoxoptions.set_headless()
    brower = webdriver.Firefox()
    
    brower.get('https://www.sec.gov/Archives/edgar/data/320193/000114036123023700/ny20007635x3_424b2.htm')
    print(brower.page_source)
    brower.close()
finally:
    brower.close()
    pass
   