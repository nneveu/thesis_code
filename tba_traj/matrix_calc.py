from sympy import *

# Beam line = d1 - q1 - d2 - q2 - d3 - q3 - d4 - q4 - d5

f1 = Symbol('f1')
f2 = Symbol('f2')
f3 = Symbol('f3')
f4 = Symbol('f4')
l1  = Symbol('L1')

#beam = Matrix([[1,l1], [0,1]])
#Distance from end of linac to Q1 = 2.83 meters
d1 = Matrix([[1,2.83], [0,1]])
#Distance between Q1/Q2/Q3/Q4 = 0.25 meters
d2 = Matrix([[1,0.25], [0,1]])
d3 = Matrix([[1,0.25], [0,1]])
d4 = Matrix([[1,0.25], [0,1]])
#Distance from Q4 to entrance of kicker = 2.0 meters
d5 = Matrix([[1,2.0], [0,1]]) #Dist in opt is 1.8515 meters

quad1 = Matrix([[1,0], [-1/f1,1]])
quad2 = Matrix([[1,0], [-1/f2,1]])
quad3 = Matrix([[1,0], [-1/f3,1]])
quad4 = Matrix([[1,0], [-1/f4,1]])

test = simplify(d5*quad4*d4*quad3*d3*quad2*d2*quad1*d1)

#Karl Brown telescope
dk3 = Matrix([[1,f2], [0,1]])
dk2 = Matrix([[1,f1+f2], [0,1]])
dk1 = Matrix([[1,f1], [0,1]])
karlbrown1 = simplify(dk3*quad2*dk2*quad1*dk1) 

dk6 = Matrix([[1,f4], [0,1]])
dk5 = Matrix([[1,f3+f4], [0,1]])
dk4 = Matrix([[1,f3], [0,1]])
karlbrown2 = simplify(dk6*quad4*dk5*quad3*dk4) 

karlbrown3 = simplify(karlbrown2*karlbrown1)

print('karl brown - four focal lengths')
print(karlbrown1, '\n')
print(karlbrown2,'\n')
print(karlbrown3,'\n')
#print(karlbrown[1,1],'\n')

print('karl brown - two focal lengths')
telescope2 = dk1*quad1*dk2*quad2*dk3
telescope = simplify(telescope2*karlbrown1)
#simplify(dk1*quad1*(dk1+dk2)*quad2*(2*dk2)*quad2*(dk1+dk2)*quad1*dk1)

print(telescope, '\n')

print(Transpose(telescope))

#sig = Matrix([[1,f4], [0,1]]) 

#newsig = telescope*sig*Transpose(telescope)



#print('element 0,0')
#print(test[0,0], '\n')
#
#print('element 0,1')
#print(test[0,1], '\n')
#
#print('element 1,0')
#print(test[1,0], '\n')
#
#print('element 1,1')
#print(test[1,1], '\n')

#print(d1*d1)
