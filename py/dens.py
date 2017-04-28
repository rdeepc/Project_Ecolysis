import cv2
import os
import matplotlib.pyplot as plt

os.chdir("..\\scraping_nasa_server\\tempa_image\\amazon")

image = plt.imread('2.jpg')
l = []
for i in range(67):
    for j in range(117):
        l.append(image[i,j])

print(l)
# plt.imshow(i, cmap = 'gray')
# plt.show()
#
