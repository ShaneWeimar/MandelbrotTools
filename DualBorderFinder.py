# (1) Establish parameters (initial points on the real axis p1, p2)

p1 = [-1.5,1]
p2 = [-1.3,1]
n = 2000
k = 10000
reduction_size = 0.01
	
# (2) Define functions for the dual numbers

def midpoint(x,y):
    return [(x[0]+y[0])/2,1]
def dualSquare(z):
    return [z[0]**2, 2*z[0]*z[1]]
def dualAdd(z1,z2):
    return [z1[0]+z2[0],z1[1]+z2[1]]
def abs(z):
    return(z[0]**2+z[1]**2)
def f_c(z,c):
    return dualAdd(dualSquare(z),c)
z=midpoint(p1,p2)
	
# (3) Define a function to check a point’s divergence

def checkDivergence(c,k):
    divergence = 0
    i=0
    z=c
    while divergence == 0 and i < k:
        if abs(z)>10**10:
            divergence = 1
            z = f_c(z,c)
            i=i+1
        return divergence
			
# (4) Iterate through nested intervals and print the result

for i in range(0,n+1):
    c = midpoint(p1,p2)
    divergence = checkDivergence(c,k)
    if divergence == 0:
        p2 = [p2[0] - (p2[0]-p1[0])*reduction_size,1]
    if divergence == 1:
        p1 = [p1[0] + (p2[0]-p1[0])*reduction_size,1]
    if i<15 or (i%5 == 0 and i<50) or (i%100 == 0 and i<1000) or i%500 == 0:
        print(str(i) + ": " + str(midpoint(p1,p2)[0]))
