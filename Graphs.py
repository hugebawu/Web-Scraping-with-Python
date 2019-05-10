# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
print sys.getdefaultencoding()
#-----------------------图1--------------------------------
# x = np.arange(1, 7)
# y1 = [0,         0, 60.92, 71.46, 75.52, 84.23]
# y2 = [0,     60.34, 78.25, 80.23, 85.45, 90.22]
# y3 = [64.03, 84.10, 92.93, 98.58, 99.85, 99.78]
# y4 = [66.12, 86.13, 93.55, 98.85, 99.82, 99.98]
#
# group_labels = ['±90', '±75', '±60', '±45', '±30', '±15']
#
# plt.style.use('grayscale') #bmh、ggplot、dark_background、fivethirtyeight、grayscale
# plt.title('recognition rates (%) across views')
# plt.xlabel('pose angle(º)')
# plt.ylabel('recognition rates(%)')
#
# plt.plot(x, y1,'r-', label='FF-GAN')
# plt.plot(x, y2,'g-',label='DR-GAN')
# plt.xticks(x, group_labels, rotation=0)
#
# plt.plot(x, y3, 'b*-', label='TP-GAN')
# plt.plot(x, y4, 'y*-', label='TPWGAN-GP')
# plt.xticks(x, group_labels, rotation=0)
#
# plt.legend(bbox_to_anchor=[1, 0.3])
# plt.grid() #加入网格
# plt.savefig('E:/study/crawler/Web-Scraping-with-Python/table1.png')
# plt.show()

#-----------------------图2--------------------------------
x = np.arange(1, 7)

y1 = [    0,     0, 64.12, 70.13, 75.23, 79.56]
y2 = [    0, 58.21, 69.14, 77.65, 79.70, 82.05]
# y3 = [40.12, 59.41, 72.45, 83.83, 84.74, 87.15]
# y4 = [45.23, 61.31, 75.24, 85.46, 87.14, 90.05]
y5 = [48.73, 68.91, 80.33, 87.71, 89.90, 91.22]
y6 = [50.28, 70.12, 81.26, 89.32, 91.70, 92.46]

group_labels = ['±90', '±75', '±60', '±45', '±30', '±15']

plt.style.use('grayscale') #bmh、ggplot、dark_background、fivethirtyeight、grayscale
plt.title(' recognition rates (%) across views')
plt.xlabel('pose angle(º)')
plt.ylabel('recognition rates(%)')

plt.plot(x, y1, 'b^-', label='FF-GAN')
plt.plot(x, y2,'g4-',label='DR-GAN')
# plt.plot(x, y3, 'cx-', label='I60')
# plt.plot(x, y4,'rs-', label='I128')
plt.plot(x, y5, 'r*-', label='TP-GAN')
plt.plot(x, y6, 'kv-', label='TPWGAN-GP')

plt.xticks(x, group_labels, rotation=0)

plt.legend(bbox_to_anchor=[1, 0.4])
plt.grid()
plt.savefig('E:/study/crawler/Web-Scraping-with-Python/table2.png')
plt.show()