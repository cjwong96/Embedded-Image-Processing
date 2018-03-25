import cv2
import numpy as np





img = cv2.imread('2.png')
Threshold=150
#轉灰階
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

height = img.shape[0]
width = img.shape[1]

#畫sobel的圖
newImg = gray.copy()

#梯度kernal
gx=[[-1,0,1],[-2,0,2],[-1,0,1]]
gy=[[-1,-2,-1],[0,0,0],[1,2,1]]

# pixel by pixel
for h in range(0,height):
    for w in range(0,width):
            #Calculate sum of squares
        sobelx=0
        sobely=0
		# 3X3 捲積計算
        for j in range(0,3):
            for i in range(0,3):
                sobelx=sobelx+gray[h+j-2][w+i-2]*gx[j][i]
                sobely=sobely+gray[h+j-2][w+i-2]*gy[j][i]
                
        # sobel result 
        sobel= (sobelx**2+sobely**2)**0.5
            #If corner response is over threshold, color the point and add to corner list
		
		#成立畫白 不成立畫黑
        if sobel>Threshold:
            newImg.itemset((h, w), 255)
        else:
            newImg.itemset((h, w), 0)
            

            
#show img            
cv2.imshow('e',img)            
cv2.imshow('re',newImg)
           
                

cv2.waitKey(0)
cv2.destroyAllWindows()