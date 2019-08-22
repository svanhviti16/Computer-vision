import cv2
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

def showImg(img, title = ''):
    plt.figure(figsize = (20,15));
    plt.title(title)
    plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))

def showGrayScaleImg(img, title = ''):
    plt.figure(figsize = (20,15));
    plt.title(title)
    plt.imshow(img, cmap='gray')