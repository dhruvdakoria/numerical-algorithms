import numpy as np

# Implementing Inverse Iteration
def main():
    x0 = np.array([1,1,1])
    A = np.array([[1,-1,0],[0,-4,2],[0,0,-2]])
    
    tol = 0.01
    change = 1
    normold = 100
    
    print("------------ Given Matrix A --------------")
    np.set_printoptions(precision=4, suppress=True)
    print(A)
    print("\n\n------------ Initial Guess x --------------")
    print(x0,"\n\n\n------------ Inverse Iteration --------------")
    print('k ,\t\t xk\t\t\t,   Norm yk')
    print('0 , ',x0,' ,  ')
    count = 1
    
    while change>tol:
        xold = x0
        x0 = gaussEliminationWithBackSubs(A,x0) # LU Solver
        norm = max(abs(x0)) # Taking infinity norm
        x0 = x0/norm  # Normalizing x0
        print(count,', ', x0,', ', "{:.3f}".format(norm)) # Printing values at each iteration
        count+=1
        change = abs(norm-normold)/normold*100 # change in lambda ((3.3333-3/3)*100)
        normold = norm

# Applying Gauss Elimination with Back Substitution
def gaussEliminationWithBackSubs(arr,x0):
    arr=np.append(arr,np.array([x0]).transpose(),axis=1) # Augmented Matrix
    # print(arr)
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
