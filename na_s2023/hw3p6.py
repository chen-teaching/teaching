# -*- coding: utf-8 -*-

import numpy as np

def solve_lower_triangular(L,b):
    
    # get shape of A
    n,_=np.shape(L)
    
    # intialize solution vector
    x = np.full(n,np.nan)
    
    for i in range(n):
        # solve for i-th equation 
        x[i] = (b[i] - x[:i]@L[i,:i])/L[i,i]
    
    return x

def solve_upper_triangular(U,b):
    
    # get shape of A
    n,_=np.shape(U)
    
    # intialize solution vector
    x = np.full(n,np.nan)
    
    for i in range(n-1,-1,-1):
        # solve for i-th equation 
        x[i] = (b[i] - x[i+1:]@U[i,i+1:])/U[i,i]
    
    return x

def solve_LU(L,U,b):
    """
    Solve LUx = b, where L is lower triangular and U is upper triangular
    """

    # TODO

    return x

L = np.tril(np.linspace(-1,1,100).reshape(10,10),0)
U = np.triu(np.ones(100).reshape(10,10),0)
b = np.ones(10)

x = solve_LU(L,U,b)
print(np.linalg.norm(b-L@U@x))

def solve_QR(Q,R,b):
    """
    Solve QRx = b, where Q is orthogonal and R is upper triangular
    """

    # TODO

    return x

Q = .5*np.array([[1,1,1,1],[-1,-1,1,1],[-1,1,1,-1],[-1,1,-1,1]])
R = np.array([[1,2,3,4],[0,5,6,7],[0,0,8,9],[0,0,0,10]])
b = np.array([1,1,1,1])

x = solve_QR(Q,R,b)
print(np.linalg.norm(b-Q@R@x))
