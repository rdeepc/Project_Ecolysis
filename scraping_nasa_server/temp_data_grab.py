from urllib.request import urlretrieve
import ssl
folderName="tempa_image"
url="https://climate.nasa.gov/system/time_series_images/811_Gistemp_fahrenheit_4degrees2016update_nofades1884.jpg"
year="1884"
fileName=folderName+"/"+year+".jpg"
urlretrieve(url, fileName,verify=False)