import numpy as np
from numpy import linalg as LA # import linear algebra 
from numpy.linalg import inv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

Iteration=None
Z=None
X=None
CB=None
CN=None
RC=None
Basis=None
B=None
NB=None
Index_Enter=None
Index_Leave=None
eps = 1e-12 # value used to determine whether reduced costs is justifiable enough to keep looking for a solution. See definition of MaxRC to know that reduced costs calculation means.

def simplex_iteration(A, b, C, m: int, n: int):
    """Computes the optimal solution to the linear Program:
      Max C^tX
      Subject to: AX=b
      X >=0

    Arguments
      A: m × (n+m) array
      b: initial vector (length m)
      C: Objective coefficients (length n+m)
      n+m: dimension of X, must be >= 1
    
    Returns
      X: (n+m) x 1 vetor, solution to AX=b
      RC: 1x(n + m) vector, reduced costs of X and slack variables.  
      Z: Objective value

    Intermediary
    B: m x m, Basis matrix.
    NB: n x m, Non-basis matrix
    """
    #intialization
    global Iteration
    global Z
    global X
    global CB
    global CN
    global RC
    global Basis
    global B
    global NB
    global Index_Enter
    global Index_Leave
    global eps

    Iteration=0
    Z=0
    X=np.zeros((n+m))
    CB=np.zeros((m))
    CN=np.zeros((n))
    RC = np.zeros((n+m))
    Basis=np.zeros((m))
    B = np.zeros((m,m))
    NB = np.zeros((m,n))
    Index_Enter=-1
    Index_Leave=-1
    started = False
    MaxRC = 0
    
    # Generates matrices that represent indices and coefficients of current basic & non-basic variables during iterations (Basis, B, NB) 
    # and indices of the non-basic variables in initial objective function (CN).
    for i in range(0,m):
        Basis[i]=n+i
        for j in range(0,m):
         B[i, j]=A[i,n+j]
        for j in range(0,n):
         NB[i, j]=A[i,j]

    for i in range(0,n):
        CN[i]=C[i]
  
    print(f'A is: {A}')
    print(f'C is: {C}')
    print(f'Start Basis Indices is: {Basis}')
    print(f'Basis variables are: {B}')
    print(f'Non-Basic Variables in Constraint Equations are: {NB}')
    print(f'Non-Basic Variables in objective function are: {CN}')
    print(f'Basic Variables in objective function are: {CB}')
    # print(f'CB transposed is: {CB.transpose()}')
    # print(f'CB shape is: {CB.shape}')

    # print("Basis", Basis)
    while(not started or MaxRC > eps):
      if not started:
        started = True

      Iteration=Iteration+1
      print(f'Iteration Num: {Iteration}')

      # Calculates the reduced costs for each non-basic variable. Reduced Cost refers to a calculation that determines how much the objective function
      # would increase given that the value of each non-basic variable is increased while other variables are kept constant. The non-basic variable with
      # the highest value is the one that is chosen to enter the basis.
      RC=C-np.dot(CB.transpose(),np.dot(inv(B),A))

      MaxRC=0
      # Finds the index of the non-basic variable with the greatest coefficient that is to enter the basis. We choose the variable with the largest 
      # coefficient as a heuristic that contributes most effectively to the value of the objective function.
      for i in range(0,n+m):
        if(MaxRC<RC[i][i]):
            MaxRC=RC[i][i]
            Index_Enter=i
      # print(" Index_Enter: ",  Index_Enter)

      print("Previous Basis Variables: ",B)
      print("Old Basis Inidices", Basis)
      Index_Leave=-1
      MinVal=1000000
      for i in range(0,m):
       if(np.dot(inv(B),A)[i,  Index_Enter] > 0):
         # Divides the right-hand side of each constraint with the coefficient of the non-basic variable that is entering the basis to find out which basic
         # variable should be removed from the basis. This division basically ensures that when increasing/loosening the value of the non-basic variable
         # and tightening the value of the basic variable, we do not overshoot the boundary of the feasible solution. This is why we choose the 'minimum ratio'
         bratio=np.dot(inv(B),b)[i]/np.dot(inv(B),A)[i,  Index_Enter]
         if(MinVal > bratio ):
           Index_Leave=i
           MinVal=bratio
      # If there is no valid basic variable to leave the basis, the problem is unbounded, hence stop where we are.
      if (Index_Leave == -1):
         print("Problem Unbounded.")
         return Z,X,RC

      Basis[Index_Leave]=Index_Enter # Switches position of the variable leaving the basis with the variable entering the basis. 
     
      # Sorts the indices up to length m stored inside Basis. This is done simply for orderly purposes, to keep a coherent order.
      for i in range(m-1,0,-1):
        if(Basis[i] < Basis[i-1]):
            temp=Basis[i-1]
            Basis[i-1]=Basis[i]
            Basis[i]=temp
      print("Updated Basis Indices", Basis)

      # updates the values inside B and CB because a new variable is entering the basis. B represents the smaller matrix within A that consists of the coefficients of the current basic variables.
      # CB represents the vector within C that consists of the coefficients of the current basic varibles in the objective function.
      for i in range(0,m):
          for j in range(0,n+m):
              if(j==Basis[i]):
                B[:, i]=A[:,j]
                CB[i]=C[j]

      print("New Basis Variables in constraint equations are: ",B)

      # Print statements used for debugging and observing of solution
      # print(f'np.dot is: {np.dot(CB.transpose(),np.dot(inv(B),A))}')
      # print(f'C: {C} | CB: {CB} | CB transpose: {CB} | B: {B} | B inv: {inv(B)} | A: {A}')
      # print(f'RC is {RC}')
      # print(f'Index_Enter is : {Index_Enter}')
      # print("MaxRC",MaxRC)

      # calculates the values of the basic variables during iteration of the simplex method.
      X=np.dot(inv(B),b)
      print(f'X: {X}')
      print(f'Basis Indices are: {Basis}')
      print(f'Basis Coefficients in Objective Function are: {CB}')
      # print(f'X: {X} | B: {B} | B inv: {inv(B)} | b: {b}')
      # calculates value of the objective function given values of basic variables and their coefficients.
      Z=np.dot(CB,X)
      print(f'Z: {Z}')
    return Z, X, RC, Basis

# Example4:
# C=np.array([[2],[3],[2],[0],[0]])
# A=np.array([[1,3,2,1,0],[2,2,1,0,1]])
# b=np.array([[4],[2]])

C=np.array([[4], [6], [0], [0], [0]])
A=np.array([[-1, 1, 1, 0, 0],[1, 1, 0, 1, 0], [2, 5, 0, 0, 1]])
b=np.array([[11], [27], [90]])

Z,X,RC,B=simplex_iteration(A,b,C,3,2)
# simplex_iteration(A,b,C,2,3)

print("Z", Z)
print("X",X)
print("RC",RC)
print("B",B)


# Example1:
#A=np.array([[1,1,1,3,1,1,0,0],[1,4,1,3,1,0,1,0],[1,2,1,4,1,0,0,1]])
#b=np.array([[1],[2],[3]])
#C=np.array([5,3,4,2,3,0,0,0])


#Example2: 
#A=np.array([[1,3,2,1,0,0],[2,2,1,0,1,0],[1,1,2,0,0,1]])
#b=np.array([[4],[2],[3]])
#C=np.array([2,3,2,0,0,0])

# Example3:
#A=np.array([[1,2,1,2,1,3,1,1,0,0],[1,3,4,2,1,3,1,0,1,0],[3,2,2,1,5,4,1,0,0,1]])
#b=np.array([[4],[4],[4]])
#C=np.array([4,3,5,3,3,4,3,0,0,0])

# Example4:
#A=np.array([[1, 2, 2, 2, 5, 4, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#[3, 5, 1, 4, 2, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
#[4, 3, 2, 7, 1, 3, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
#[2, 1, 7, 2, 6, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
#[3, 2, 1, 4, 3, 7, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
#[1, 2, 5, 2, 5, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
#[3, 2, 1, 4, 2, 7, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
#[4, 3, 2, 8, 1, 6, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
#[2, 1, 4, 2, 6, 5, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
#[4, 2, 1, 4, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]])
#b=np.array([[9],[4],[5],[8],[7],[9],[6],[4],[3],[4]])
#C=np.array([5, 4, 3, 5, 8, 4,0,0,0,0,0,0,0,0,0,0])
