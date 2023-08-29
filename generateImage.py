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
        npByteArray[i,j] = generateRandom()
        
        
    #npByteArray = np.reshape(npByteArray,(w,h))
    #print(npByteArray)
    generateImage(npByteArray)

def generateRandom():
    pixelArray = np.zeros(shape=(1,3),dtype=np.uint8)
    pixelArray[0][0] = np.random.randint(0,255)# R
    pixelArray[0][1] = np.random.randint(0,255)# G
    pixelArray[0][2] = np.random.randint(0,255)# B
    return pixelArray
def generateImage(array):
    img = Image.fromarray(array)
    img.save("image.png")

def main():
    

    while True:
        seed = int(random.random() * 1000000000)
        np.random.seed(int(seed))
        print(f"SEED: {int(seed)}")
        generateArray(32,32)
        time.sleep(0.3)

main()