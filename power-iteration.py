import numpy as np

x0 = np.array([0,1])
A = np.array([[3,1],[1,3]])

tol = 0.1
change = 1
Ratio = 100
print('k ,  xk  ,  Ratio/Lambda')
print('0 , ',x0[0],x0[1],' ')
count = 1
while change>tol:
    xold = x0
    x0 = np.dot(A,x0)
    print(count,', ', x0[0],x0[1],', ', x0[1]/xold[1])
    count+=1
    change = abs(Ratio-x0[1]/xold[1])/Ratio*100 #change in lambda ((3.3333-3/3)*100)
    Ratio=x0[1]/xold[1]
    print(change)
