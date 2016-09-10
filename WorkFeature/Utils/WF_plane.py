# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 22:10:41 2016

@author: laurent
"""

import numpy as np
import scipy.optimize

def fitPLaneLTSQ(XYZ):
    # Fits a plane to a point cloud, 
    # Where Z = aX + bY + c        ----Eqn #1
    # Rearanging Eqn1: aX + bY -Z +c =0
    # Gives normal (a,b,-1)
    # Normal = (a,b,-1)
    [rows,cols] = XYZ.shape
    G = np.ones((rows,3))
    G[:,0] = XYZ[:,0]  #X
    G[:,1] = XYZ[:,1]  #Y
    Z = XYZ[:,2]
    (a,b,c),resid,rank,s = np.linalg.lstsq(G,Z) 
    normal = (a,b,-1)
    nn = np.linalg.norm(normal)
    normal = normal / nn
    return normal


def fitPlaneSVD(XYZ):
    [rows,cols] = XYZ.shape
    # Set up constraint equations of the form  AB = 0,
    # where B is a column vector of the plane coefficients
    # in the form b(1)*X + b(2)*Y +b(3)*Z + b(4) = 0.
    p = (np.ones((rows,1)))
    AB = np.hstack([XYZ,p])
    [u, d, v] = np.linalg.svd(AB,0)        
    B = v[3,:];                    # Solution is last column of v.
    nn = np.linalg.norm(B[0:3])
    B = B / nn
    return B[0:3]


def fitPlaneEigen(XYZ):
    # Works, in this case but don't understand!
    average=sum(XYZ)/XYZ.shape[0]
    covariant=np.cov(XYZ - average)
    eigenvalues,eigenvectors = np.linalg.eig(covariant)
    want_max = eigenvectors[:,eigenvalues.argmax()]
    (c,a,b) = want_max[3:6]    # Do not understand! Why 3:6? Why (c,a,b)?
    normal = np.array([a,b,c])
    nn = np.linalg.norm(normal)
    return normal / nn  

def fitPlaneSolve(XYZ):
    X = XYZ[:,0]
    Y = XYZ[:,1]
    Z = XYZ[:,2] 
    npts = len(X)
    A = np.array([ [sum(X*X), sum(X*Y), sum(X)],
                   [sum(X*Y), sum(Y*Y), sum(Y)],
                   [sum(X),   sum(Y), npts] ])
    B = np.array([ [sum(X*Z), sum(Y*Z), sum(Z)] ])
    normal = np.linalg.solve(A,B.T)
    nn = np.linalg.norm(normal)
    normal = normal / nn
    return normal.ravel()

def fitPlaneOptimize(XYZ):
    def residiuals(parameter,f,x,y):
        return [(f[i] - model(parameter,x[i],y[i])) for i in range(len(f))]


    def model(parameter, x, y):
        a, b, c = parameter
        return a*x + b*y + c

    X = XYZ[:,0]
    Y = XYZ[:,1]
    Z = XYZ[:,2]
    p0 = [1., 1.,1.] # initial guess
    result = scipy.optimize.leastsq(residiuals, p0, args=(Z,X,Y))[0]
    normal = result[0:3]
    nn = np.linalg.norm(normal)
    normal = normal / nn
    return normal


if __name__=="__main__":
    XYZ = np.array([
        [0,0,1],
        [0,1,2],
        [0,2,3],
        [1,0,1],
        [1,1,2],
        [1,2,3],
        [2,0,1],
        [2,1,2],
        [2,2,3]
        ])
    print "Solve: ",fitPlaneSolve(XYZ)
    print "Optim: ",fitPlaneOptimize(XYZ)
    print "SVD:   ",fitPlaneSVD(XYZ)
    print "LTSQ:  ",fitPLaneLTSQ(XYZ)
    print "Eigen: ",fitPlaneEigen(XYZ)