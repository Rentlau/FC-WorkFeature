# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 06:59:10 2016

@author: laurent
"""
from __future__ import division
from math import factorial


# Pascal's triangle 
p_t = [      [1],           # n=0
            [1,1],          # n=1
           [1,2,1],         # n=2
          [1,3,3,1],        # n=3
         [1,4,6,4,1],       # n=4
        [1,5,10,10,5,1],    # n=5
       [1,6,15,20,15,6,1]]  # n=6

#==============================================================================
# binomial(n,k):
#   while(n >= lut.length):
#     s = lut.length
#     nextRow = new array(size=s+1)
#     nextRow[0] = 1
#     for(i=1, prev=s-1; i&ltprev; i++):
#       nextRow[i] = lut[prev][i-1] + lut[prev][i]
#     nextRow[s] = 1
#     lut.add(nextRow)
#   return lut[n][k]
#==============================================================================
def binomial(n, i):
    """ return binomial terms from Pascal triangle from predefined list or
    calculate the terms if not already in the list.
    """
    global p_t
    m_l = len(p_t)
    while n >= m_l:
        m_next_row = []
        m_next_row.append(1)
        for m_i in range(1,m_l):
            m_next_row.append(p_t[m_l-1][m_i-1]+p_t[m_l-1][m_i])
        m_next_row.append(1)
        # print m_next_row
        p_t.append(m_next_row)
        m_l = len(p_t)
        
    return p_t[n][i]
    
    
def binomial_term(n, i):
    """ binomial coefficient = n! / (i!(n - i)!)
    """
    return factorial(n) / (factorial(i) * factorial(n - i))


#==============================================================================
# function Bezier(n,t):
#   sum = 0
#   for(k=0; k<n; k++):
#     sum += n!/(k!*(n-k)!) * (1-t)^(n-k) * t^(k)
#   return sum
#==============================================================================
def bezier_base(n, t):
    """ Basis Bezier function.
    """    
    m_sum = 0.
    m_C = binomial_term
    for i in range(n):
        m_sum += m_C(n, i) * (1 - t)**(n - i) * t**i
    return m_sum
    
    
#==============================================================================
# function Bezier(2,t):
#   t2 = t * t
#   mt = 1-t
#   mt2 = mt * mt
#   return mt2 + 2*mt*t + t2
#==============================================================================
def bezier_quadratic_terms(t):
    """ Simplified Bezier quadratic curve.
    Return 3 terms in list ()
    """    
    m_terms = list()
    # n=2 i=0
    # m_C(n, i) * (1 - t)**(n - i) * t**i
    # m_C(2, 0) * (1 - t)**(2 - 0) * t**0
    # 1 * (1 - t)*(1 - t) * 1
    m_terms.append((1 - t)*(1 - t))
    # n=2 i=1
    # m_C(n, i) * (1 - t)**(n - i) * t**i    
    # m_C(2, 1) * (1 - t)**(2 - 1) * t**1
    # 2 * (1 - t) * t
    m_terms.append(2 * (1 - t) * t)
    
    m_terms.append(t*t)
    return m_terms
 
 
#==============================================================================
# function Bezier(3,t):
#   t2 = t * t
#   t3 = t2 * t
#   mt = 1-t
#   mt2 = mt * mt
#   mt3 = mt2 * mt
#   return mt3 + 3*mt2*t + 3*mt*t2 + t3   
#==============================================================================
def bezier_cubic_terms(t):
    """ Simplified Bezier cubic curve.
    Return 4 terms in list ()
    """ 
    m_terms = list()
    # n=3 i=0
    # m_C(n, i) * (1 - t)**(n - i) * t**i
    # m_C(3, 0) * (1 - t)**(3 - 0) * t**0
    # (1 - t)*(1 - t)*(1 - t)
    m_terms.append((1 - t)*(1 - t)*(1 - t))
    # n=3 i=1
    # m_C(n, i) * (1 - t)**(n - i) * t**i
    # m_C(3, 1) * (1 - t)**(3 - 1) * t**1
    # 3 * (1 - t)*(1 - t) * t
    m_terms.append(3 * (1 - t)*(1 - t) * t)
    # n=3 i=2
    # m_C(n, i) * (1 - t)**(n - i) * t**i
    # m_C(3, 2) * (1 - t)**(3 - 2) * t**2
    # 3 * (1 - t) * t * t
    m_terms.append(3 * (1 - t) * t * t)
    
    m_terms.append(t * t * t) 
    return m_terms

def bezier_terms(n, t):
    """ Bezier curve.
    Return n+1 terms in list ()
    """
    m_terms = list()
    m_C = binomial_term
    for i in range(n):
        m_terms.append( m_C(n, i) * (1 - t)**(n - i) * t**i )
    m_terms.append(t ** n) 
    return m_terms

#==============================================================================
# function Bezier(n,t,w[]):
#   sum = 0
#   for(k=0; k<n; k++):
#     sum += w[k] * binomial(n,k) * (1-t)^(n-k) * t^(k)
#   return sum
#==============================================================================
def bezier_curve(n, t, weigths):
    """ Basis Bezier function.
    """    
    m_sum = 0.
    m_C = binomial_term

    for i,w in zip(range(n+1),weigths):
        m_sum += m_C(n, i) * (1 - t)**(n - i) * t**i * w
    return m_sum
    
    
#==============================================================================
# function Bezier(2,t,w[]):
#   t2 = t * t
#   mt = 1-t
#   mt2 = mt * mt
#   return w[0]*mt2 + w[1]*2*mt*t + w[2]*t2
#==============================================================================
def bezier_quadratic_curve(t, weigths):
    if len(weigths) != 3:
        return None
    t2 = t * t
    mt = 1-t
    mt2 = mt * mt
    return weigths[0]*mt2 + weigths[1]*2*mt*t + weigths[2]*t2


#==============================================================================
# function Bezier(3,t,w[]):
#   t2 = t * t
#   t3 = t2 * t
#   mt = 1-t
#   mt2 = mt * mt
#   mt3 = mt2 * mt
#   return w[0]*mt3 + 3*w[1]*mt2*t + 3*w[2]*mt*t2 + w[3]*t3
#==============================================================================
def bezier_cubic_curve(t, weigths):
    if len(weigths) != 4:
        return None
    t2 = t * t
    t3 = t2 * t
    mt = 1-t
    mt2 = mt * mt
    mt3 = mt2 * mt
    return weigths[0]*mt3 + weigths[1]*3*mt2*t + weigths[2]*3*mt*t2 + weigths[3]*t3    


class Bezier():
    """ bezier curve object
    
    points : list of control points
    points = [(-1,-1,0.0),(0,3,0.0)]
    """
    def __init__(self, points):
        if (None in [points]) :
            print "\nERROR in : bezier.__init__"
            print "'points' not defined !"
            return None
        
        n = len(t)
        pass
    
if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import numpy as np
    t = np.arange(0.0, 1.0, 0.01)
    b1 = bezier_base(1, t)
    plt.plot(t, b1)
    b2 = bezier_base(2, t)
    plt.plot(t, b2)
    b3 = bezier_base(3, t)
    plt.plot(t, b3)
    plt.xlabel('t values')
    plt.ylabel('')
    plt.title('Bezier basis functions : b1(blue), b2(green) and b3(red)')
    plt.grid(True)
    plt.show()
    
#    print str(binomial(0, 0))
#    print str(binomial(1, 0)),
#    print str(binomial(1, 1))
    
    print ("Pascal's triangle :") 
    for j in range(0,10):        
        for i in range(0,j+1):
            print str(binomial(j, i)),
        print ""
        
#    m_points = [(-1,-1,0.0),(0,3,0.0)]
#    bz=Bezier(m_points)    t = np.arange(0.0, 1.0, 0.01)
    t = np.arange(0.0, 1.0, 0.01)
    b12,b22,b32 = bezier_quadratic_terms(t)
    plt.plot(t, b12)
    plt.plot(t, b22)
    plt.plot(t, b32)

    plt.xlabel('t values')
    plt.ylabel('')
    plt.title('Bezier basis functions terms : quadratic')
    plt.grid(True)
    plt.show()
    
    t = np.arange(0.0, 1.0, 0.01)
    b13,b23,b33,b43 = bezier_cubic_terms(t)
    plt.plot(t, b13)
    plt.plot(t, b23)
    plt.plot(t, b33)
    plt.plot(t, b43)
    plt.title('Bezier basis functions terms : cubic')
    plt.show()
    
    t = np.arange(0.0, 1.0, 0.01)
    m_terms = list()
    m_terms = bezier_terms(15,t)
    for term in m_terms:
        plt.plot(t, term)
    plt.title('Bezier basis functions terms : 15')
    plt.show() 
    pt1 = (120,160)
    pt2 = (35,200) 
    pt3 = (220,260) 
    pt4 = (220,40)   
    x = (120,35,220,220)
    y = (160,200,260,40)
    
    t = np.arange(0.0, 1.0, 0.01)
    m_dim = len(x)-1
    m_Xs = bezier_curve(m_dim, t, x)
    m_Xs = bezier_cubic_curve(t, x)
    plt.plot(t, m_Xs)
    plt.title('Bezier curve : X')
    plt.show()
    m_dim = len(y)-1
    m_Ys = bezier_curve(m_dim, t, y)
    m_Ys = bezier_cubic_curve(t, y)
    plt.plot(t, m_Ys)
    plt.title('Bezier curve : Y')
    plt.show()
    
    plt.plot(m_Xs, m_Ys)
    plt.plot(x, y, 'o-')
    plt.show()
    
    t = np.arange(-0.2, 1.1, 0.01)
    m_Xs = bezier_curve(m_dim, t, x)
    m_Ys = bezier_curve(m_dim, t, y)
    plt.plot(m_Xs, m_Ys)
    plt.plot(x, y, 'o-')
    plt.show() 
    
#==============================================================================
#     import matplotlib as mpl
#     from mpl_toolkits.mplot3d import Axes3D
#     import numpy as np
#     import matplotlib.pyplot as plt
#     
#     mpl.rcParams['legend.fontsize'] = 10
#     
#     fig = plt.figure()
#     ax = fig.gca(projection='3d')
#     theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
#     z = np.linspace(-2, 2, 100)
#     r = z**2 + 1
#     x = r * np.sin(theta)
#     y = r * np.cos(theta)
#     ax.plot(x, y, z, label='parametric curve')
#     ax.legend()
#     
#     plt.show() 
#==============================================================================
    
    