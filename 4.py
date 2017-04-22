# The standard library modules
import os
import sys

# The wget module
import wget

# The BeautifulSoup module
from bs4 import BeautifulSoup
from PIL import Image

# The selenium module
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
url="https://mynasadata.larc.nasa.gov/las/UI.vm#panelHeaderHidden=false;differences=false;autoContour=false;globalMin=-0.339;globalMax=32.767;xCATID=E1FDD4E311E8690B16343A398E1B9E92;xDSID=ocean_data;varid=sea_level-id-cd469260cd;imageSize=auto;over=xy;compute=Nonetoken;tlo=04-Oct-1992%2000:00;thi=04-Oct-1992%2000:00;catid=E1FDD4E311E8690B16343A398E1B9E92;dsid=ocean_data;varid=sea_level-id-cd469260cd;avarcount=0;xlo=0.5;xhi=359.5;ylo=-89.5;yhi=89.5;operation_id=Plot_2D_XY_zoom;view=xy"
driver = webdriver.Firefox(executable_path=r'H:\soft\anacondapython\New folder\geckodriver.exe')
driver.get(url)

WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.TAG_NAME, "canvas"))) # waits till the element with the specific id appears
src = driver.page_source

parser = BeautifulSoup(src,"html.parser")

tag=parser.findAll('canvas')
tag=tag[0]

location = tag.location

print(location)
# size = tag.size
# driver.save_screenshot('screenshot.png') # saves screenshot of entire page
# driver.quit()
#
# im = Image.open('screenshot.png') # uses PIL library to open image in memory
#
# left = location['x']
# top = location['y']
# right = location['x'] + size['width']
# bottom = location['y'] + size['height']
#
#
# im = im.crop((left, top, right, bottom)) # defines crop points
# im.save('screenshot.png')

