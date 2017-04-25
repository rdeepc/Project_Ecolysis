import requests
from PIL import Image
import io

folderName="tempa_image"
year=1884
serial=811
for i in range(1884,2017):
    url="https://climate.nasa.gov/system/time_series_images/"+str(serial)+"_Gistemp_fahrenheit_4degrees2016update_nofades"+str(year)+".jpg"
    fileName=folderName+"/"+str(i)+".jpg"
    resp = requests.get(url, verify=False)
    image = Image.open(io.BytesIO(resp.content))
    image.save(str(fileName))
    year = year + 1
    serial = serial + 1