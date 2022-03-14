import numpy as np
#from matplotlib import image
from PIL import Image

'''
img0 = image.imread("t0.jpg")
img1 = image.imread("t1.jpg")
'''
t0 = np.array(Image.open('t0.jpg').convert('L'))
t1 = np.array(Image.open('t1.jpg').convert('L'))
car1 = np.array(Image.open('car1.png').convert('L'))
im = Image.fromarray(t0).save("t0Gray.jpg")
im = Image.fromarray(t1).save("t1Gray.jpg")
im = Image.fromarray(car1).save("car1Gray.jpg")
img3 = t0

linhas = t0.shape[0]
colunas = t0.shape[1]


print("t1 "+str(t1.shape))
print("car1 "+str(car1.shape))

for l in range(linhas):
    for c in range(colunas):
        if (car1[l][c] == t1[l][c]) & (t1[l][c] !=  255):
            img3[l][c] = 0
        #if img3[l][c] != 255:
         #   img3[l][c] = 0


print(img3.shape)
im = Image.fromarray(img3).save("t3.jpg")




print("End.")