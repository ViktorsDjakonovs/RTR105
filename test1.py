# -*- coding: utf-8 -*-
from math import sin

#(1.) * (2)=(2.)-float * int = float
#(1.) * (2.)= (2.) - float * float = float
#float(input()) -> float
print('Sin aprekinasana:')
x=float(input("Ievadi argumentu (x):"))
#print type(x)

y = sin(x*x)
print("sin(%.2f) = %.2f"%(x,y))

a0 = (-1)**0*x**4*0+2/(1*1)
S0 = a0
print("a0 = %.2f S0 = %.2f"%(a0,S0))

a1 = (-1)**1*x**4*1+2/(1*2*3)
S1 = a0 +a1
print("a1 = %.2f S1 = %.2f"%(a1,S1))

a2 = (-1)**2*x**4*2+2/(1*2*3*4*5)
S2 = a0 + a1 +a2
print("a2 = %.2f S2 = %.2f"%(a2,S2))

a3 = (-1)**3*x**4*3+2/(1*2*3*4*5*6*7)
S3 = a0 + a1 + a2 + a3
print("a3 = %.2f S3 = %.2f"%(a3,S3))



print('Formula: y = sin(x*x)')
print('             500')
print('            ______')
print('            \\          k     4*k+2')
print('     2       \\     (-1)  *  x ')
print('sin(x)   =    |     ----------------- = 1')    
print('             /        (2 * k +1 )!')
print('            /_____')
print('             k=0')

print('                                   2 ')
print('                           (-1) * x  ')
print('rekurences reizinatajs: ________________  ')
print(' k * 2 * (2*k+1)')
