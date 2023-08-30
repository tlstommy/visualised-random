import numpy as np
from PIL import Image
import random,time

SEED = ""

def generateArray(w,h):
    pixelcount = w * h
    npByteArray = np.zeros((w,h,3), dtype=np.uint8)
    #print(npByteArray)
    for i in range(w):
       for j in range(h): 
        pix = generateRandom()
        npByteArray[i,j] = pix

        
        
    #npByteArray = np.reshape(npByteArray,(w,h))
    #print(npByteArray)
    generateImage(npByteArray)

def generateRandom():
    pixelArray = np.zeros(shape=(1,3),dtype=np.uint8)
    pixelArray[0][0] = (np.random.randint(0,256))# R
    pixelArray[0][1] = (np.random.randint(0,256)# G
    pixelArray[0][2] = (np.random.randint(0,256)# B
    return pixelArray


def randomPixel(min,max):


def generateImage(array):
    img = Image.fromarray(array)
    img.save("image.png")

def main():
    
    width=input("Width (px): ")
    height=input("Height(px): ")

    while True:
        print(f"\n\n{width}px X {height}px")
        seed = int(random.random() * 1000000000) 
        np.random.seed(int(seed))
        print(f"SEED: {int(seed)}")
        generateArray(int(height),int(width))
        #input("---------------------------\nPress enter to regenerate. ")
        time.sleep(0.3)

main()