import numpy as np
from PIL import Image
import random

def generateArray(w,h):
    pixelcount = w * h
    npByteArray = np.arange(pixelcount)
    print(npByteArray)
    for i in range(w):
       for j in range(h): 
        np.put(npByteArray,[i,j],generateRandom(""))
        
        
    np.reshape(npByteArray,(w,h))
    print(npByteArray)
    generateImage(npByteArray)

def generateRandom(seed):
    return np.random.randint(0,250,size=3)
    
def generateImage(array):
    img = Image.fromarray(array)
    img.save("image.png")

def main():

    generateArray(512,512)

main()