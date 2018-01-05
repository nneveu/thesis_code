from sympy import *

# Beam line = d1 - q1 - d2 - q2 - d3 - q3 - d4 - q4 - d5

f1 = Symbol('f1')
f2 = Symbol('f2')
f3 = Symbol('f3')
f4 = Symbol('f4')
l1  = Symbol('L1')

#beam = Matrix([[1,l1], [0,1]])

d1 = Matrix([[1,l1], [0,1]])
d2 = Matrix([[1,l1], [0,1]])
d3 = Matrix([[1,l1], [0,1]])
d4 = Matrix([[1,l1], [0,1]])
d5 = Matrix([[1,l1], [0,1]])

quad1 = Matrix([[1,0], [f1,1]])
quad2 = Matrix([[1,0], [f2,1]])
quad3 = Matrix([[1,0], [f3,1]])
quad4 = Matrix([[1,0], [f4,1]])


test = quad4*quad3*quad2*d1

print(test)
print(d1*d1)
