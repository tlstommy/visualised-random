import numpy as np
from PIL import Image
import random,time

SEED = ""
counter = 0

def generateArray(w,h,mode):
    pixelcount = w * h
    npByteArray = np.zeros((w,h,3), dtype=np.uint8)
    #print(npByteArray)
    for i in range(w):
       for j in range(h): 
        pix = generateRandom(mode)
        npByteArray[i,j] = pix

        
        
    #npByteArray = np.reshape(npByteArray,(w,h))
    #print(npByteArray)
    generateImage(npByteArray)

def generateRandom(mode):
    pixelArray = np.zeros(shape=(1,3),dtype=np.uint8)
    pixelArray[0][0] = randomPixel(0,256,mode)# R
    pixelArray[0][1] = randomPixel(0,256,mode)# G
    pixelArray[0][2] = randomPixel(0,256,mode)# B
    return pixelArray


def randomPixel(min,max,mode):

    return np.random.randint(min,max)

def generateImage(array):
    img = Image.fromarray(array)
    img.save("image.png")

def main():
    width=input("Width (px): ")
    height=input("Height(px): ")
    mode=input("mode: ")

    while True:
        counter = 0
        print(f"\n\n{width}px X {height}px")
        
        seedIn = input("---------------------------\nSeed?: ")
        if(len(seedIn) == 0):
            seed = int(random.random() * 1000000000) 
        else:
            seed = int(''.join(str(ord(c)) for c in seedIn))
        np.random.seed(seed)
        print(f"\nSEED: {seed}")
        print(f"Mode: {mode}")
        generateArray(int(height),int(width),int(mode))
        time.sleep(0.5)

main()