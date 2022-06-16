from numpy import *
m1 = matrix('1 2 ; 3 4 ')
m2= matrix('4 3  ; 2 1 ')
m3 = matrix('0 0 ; 0 0 ')

for i in range(2):
    for j in range(2):
            m3[i,j] = 0
            for k in range(2):
                m3[i,j] = m3[i,j] + m1[i,k] * m2[k,j]
print(m3)

m4=m1*m2
print(m4)