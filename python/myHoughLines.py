import numpy as np
import cv2  # For cv2.dilate function

import copy



def myHoughLines(H, nLines):
    rhos=[]
    thetas=[]
    H1=copy.deepcopy(H)
    temp=copy.deepcopy(H)
    
    (picHigh,picLong)=H.shape
    temp=np.pad(temp,(1,),"edge")
    print(H.shape)

    ## non maximal cells part
    for x in range(1,picHigh+1):
        for y in range(1,picLong+1):
            for a in range(-1,2):
                for b in range(-1,2):
                    if temp[x+a][y+b]>temp[x][y]:
                        #offset the buffer
                        H1[x-1][y-1]=0


    ind=np.argpartition(H1.ravel(),H1.size-nLines)[-nLines:]          ##get the top"nLines"
    ind= np.column_stack(np.unravel_index(ind, H1.shape))
    print(ind)

    for x in range(nLines):
        rhos.append(int(ind[x][0]))
        thetas.append(int(ind[x][1]))
    return [np.array(rhos), np.array(thetas)]