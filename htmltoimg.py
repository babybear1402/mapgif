import cv2
import pandas as pd
from itertools import cycle
from PIL import Image, ImageTk
from PIL import Image, ImageDraw, ImageFont
import os
import numpy as np
import imageio
cases = pd.read_csv('cbc.csv')
print(cases.columns)


images =[]
image_folder = "testpic"

for i in range(107):
    imagej = Image.open("pictures/"+str(i)+".png")
    draw = ImageDraw.Draw(imagej)

    (x, y) = (65, 5)
    message = cases.columns[i+1]

    font = ImageFont.truetype("Lato-Black.ttf", 50)

    color = 'rgb(0, 0, 0)'  # black color

        # draw the message on the background
    z = 8
    draw.rectangle([935,8,1378,25], fill="white")
    draw.text((x, y), message, fill=color, font=font)
    (x, y) = (1011, z)
    message = str(int(np.exp(2)))

    font = ImageFont.truetype("Lato-Black.ttf", 15)
    draw.text((x, y), message, fill=color, font=font)
    (x, y) = (940, z)
    message = "0"
    draw.text((x, y), message, fill=color, font=font)

    (x, y) = (1082, z)
    message = str(int(np.exp(4)))
    draw.text((x, y), message, fill=color, font=font)

    (x, y) = (1082+64, z)
    message = str(int(np.exp(6)))
    draw.text((x, y), message, fill=color, font=font)

    (x, y) = (1082 + 65 * 2, z)
    message = "2,980"
    draw.text((x, y), message, fill=color, font=font)

    (x, y) = (1082 + 60 * 3, z)
    message = "22,026"
    draw.text((x, y), message, fill=color, font=font)

    (x, y) = (1082 + 60 * 4, z)
    message = "59,874"
    draw.text((x, y), message, fill=color, font=font)
        # save the edited image

    imagej.save("testpic/"+str(i)+".png")
    print("running")



    images.append(imageio.imread("testpic/"+str(i)+".png"))


imageio.mimsave('movie.gif', images)