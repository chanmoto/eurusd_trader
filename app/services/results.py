import matplotlib.animation as animation

import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

transform = transforms.PILToTensor()
fig = plt.figure()

ims = []

for item in img:
    v1,v2,d = getprice(item,transform)

    plt.title(d) 
    
    im1    = plt.plot(v1)
    im2 = plt.plot(v2)
    ims.append(im1+im2)  

ani = animation.ArtistAnimation(fig,ims,interval=100)
plt.show()
    
#imagemagickを使って，gif画像を保存
ani.save("test.gif", writer="imagemagick")