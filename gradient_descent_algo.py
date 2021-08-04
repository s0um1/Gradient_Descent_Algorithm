from sympy import *

#cal_der calculates the derivative
def cal_der(d,p):
    d_val = lambdify(x, d)
    r = d_val(p)

    return r

#new_pos calculates the new position
def new_pos(p,s,r):
    return p - (s*r)

#x stores variable
x = Symbol('x')
#f stores the function
#f = x**2 - 2*x + 2
f = input("Enter function as A * x**2 + B * x + C : ")
print("Function : ", f)
#d stores derivative of the function
d = Derivative(f, x).doit()
print("Derivative : ",d)

coeff = int(input("Enter the coefficient of x from obtained derivative with proper sign: "))
cons = int(input("Enter the constant from obtained derivative with proper sign: "))

eq = Eq((coeff*x),-cons)
#sol stores the solution of the equation
sol = solve((eq),(x))
print("On equating derivative to 0, local mimimum =",sol[0])

p = int(input("Enter initial position: "))
s = float(input("Enter step size: "))

#pl stores the list of positions
pl =[p]
#dl stores the values of derivative at all positions
dl =[]
i =0

print("Position \t Derivative")
while (i>=0):
    #r stores value of derivative upto four decimal places
    r = float("%0.4f" %(cal_der(d,p)))
    if i > 0:
        if r >= dl[len(dl)-1]or r<0:
            break
    dl.append(r)
    #np stores the next position upto foue decimal places
    np = float("%0.4f" %(new_pos(p,s,r)))
    print(p,"\t\t",r)
    pl.append(np)
    p = np
    i = i+1
    
if(r<0):
    print("No solution")
else:
    print("Calculated local minimum =",pl[len(pl)-1])    

