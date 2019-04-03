import cv2                         #using opencv version 4.0.0
import glob
import numpy as np
import matplotlib.pyplot as plt

#load all the images for stitching and make a list of them
images = []
for img in glob.glob("../input/path/folder/*.JPG"):
    image = cv2.imread(img)
    images.append(image)
    
stitcher = cv2.Stitcher_create(True)
status, stitched = stitcher.stitch(images)  #pass the list of all images

#if stiching is successful then status == 0 and we will save the stitched image
if status == 0:  
    # write the output stitched image to disk
	cv2.imwrite('stitched.jpg', stitched)
	cv2.imshow("Stitched", stitched)
	cv2.waitKey(0)
	
# otherwise the stitching failed, likely due to not enough keypoints being detected
else:
    print("[INFO] image stitching failed ({})".format(status))
    
