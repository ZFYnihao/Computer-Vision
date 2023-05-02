import numpy as np

import math

##def myHoughTransform(Im, rhoRes, thetaRes):
    # YOUR CODE HERE

def myHoughTransform(Im, rhoRes, thetaRes):

    (picHigh,picLong)=Im.shape

    #output 
    thetaScale=np.arange(0,np.pi*2,thetaRes)
    rhoAmount=((picHigh**2+picLong**2)**(0.5)) ##根号 x^2+y^2

    maxRho=int(math.ceil((rhoAmount/rhoRes)))
    maxTheta=math.ceil(math.pi*2/thetaRes)

    rhoScale=np.arange(0,rhoAmount,rhoRes)
    #Initialize the acc 
    acc=np.zeros((maxRho,maxTheta))



    ##hough transform algorithm
    for x in range(picHigh):
        for y in range(picLong):
            if Im[x][y]!=0:
                for theta in range(maxTheta):
                    thetaReal=theta*thetaRes
                    rho=x*math.sin(thetaReal)+y*math.cos(thetaReal)    ## p=xsin(*)+ycos(*)  *:theta
                    #ignore negative value
                    if rho>=0:
                        rhoReal=rho//rhoRes

                        acc[int(rhoReal)][theta]+=1 


    return [acc, rhoScale, thetaScale]