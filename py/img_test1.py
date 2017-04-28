import os
import cv2
from matplotlib import pyplot as plt
import matplotlib.pyplot as plt

print(os.getcwd())

os.chdir("..\\scraping_nasa_server\\tempa_image")

files = os.listdir()
j = 1
for image in files:
    i = cv2.imread(image)
    temp = i[204:271, 188:305]
    cv2.imwrite('%d.jpg' %j, temp)
    j+=1

