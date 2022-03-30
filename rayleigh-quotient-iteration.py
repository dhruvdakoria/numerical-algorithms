import numpy as np

# Implementing Rayleigh Quotient Iteration
def main():

    # Input Array A and initial guess x0
    x0 = np.array([1,1,1])
    A = np.array([[1,-1,0],[0,-4,2],[0,0,-2]])
    
    tolerance = 0.01
    change = 1
    shiftold = 100
    print("------------ Given Matrix A --------------")
    np.set_printoptions(precision=4, suppress=True)
    print(A)
    print("\n\n------------ Initial Guess x --------------")
    print(x0,"\n\n\n------------ Rayleigh Quotient Iteration --------------")
    print('k ,\t\t xk\t\t\t,  Rayleigh Quotient')
    print('0 , ',x0,' ,  ')
    count = 1
    
    # Iterate until the change in shift is less than tolerance 
    while change>tolerance:
        xold = x0
        numerator = np.dot(np.matrix.transpose(x0),np.dot(A,x0)) # Numerator for Rayleigh Quotient
        denominator = np.dot(np.matrix.transpose(x0),x0) # Denominator for Rayleigh Quotient
        shift = numerator/denominator # Calculating Rayleigh Quotient
        x0 = gaussEliminationWithBackSubs(np.subtract(A,shift*np.identity(len(A))),x0) #LU Solver
        norm = max(abs(x0)) # Taking infinity norm
        x0 = x0/norm  # Normalizing x0
        print(count,', ', x0 ,', ', format(shift,".4f")) # Printing Rayleigh Quotient values on screen at each iteration
        count+=1  # Incrementing count
        change = abs(shift-shiftold)/shiftold*100 # change in shift calculation
        shiftold = shift  # Updating shiftold

# Applying Gauss Elimination with Back Substitution
def gaussEliminationWithBackSubs(arr,x0):
    arr=np.append(arr,np.array([x0]).transpose(),axis=1) # Augmented Matrix

    n=len(arr)
    x = np.zeros(n)
    for i in range(n):
      if arr[i][i] == 0.0:
        print('Pivot zero detected - interchanging rows!')
        for j in range(i+1, n):
          if arr[j][i] > arr[i][i]:
            arr[[i, j]] = arr[[j, i]]
            break
      for j in range(i+1, n):
        factor = arr[j][i]/arr[i][i]
        for k in range(n+1):
          arr[j][k] = arr[j][k] - factor * arr[i][k]
    
    # Backwards Substitution
    x[n-1] = arr[n-1][n]/arr[n-1][n-1]
    
    for i in range(n-2,-1,-1):
        x[i] = arr[i][n]
        
        for j in range(i+1,n):
            x[i] = x[i] - arr[i][j]*x[j]
        
        x[i] = x[i]/arr[i][i]
    return x
    
main()
