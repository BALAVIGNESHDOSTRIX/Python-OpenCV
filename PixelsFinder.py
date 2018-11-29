'''
            DEVELOPERNAME : BALAVIGNESH.M

            SCOPE OF IMPLEMENTATION : To finding the image pixels (Height,Width)

            IMPLEMENTED DATE : 29/11/2018
'''

import cv2

import argparse as args



ap = args.ArgumentParser()

ap.add_argument("-i","--image",required=True,help="Path to image")

argument = vars(ap.parse_args())



image = cv2.imread(argument["image"])

cv2.imshow("Image",image)



print("Height {} pixels".format(image.shape[0]))

print("Width {} pixels".format(image.shape[1]))

print("Channels {} pixels".format(image.shape[2]))



cv2.waitKey(0)