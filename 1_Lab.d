# -*- coding: utf-8 -*-
from math import sin

def mans_sinuss(x):
    k = 1
    a = (-1)**0*x**2/(1)
    S = a
    print('a0 = %6.2f S0 = %6.2f'%(a,S))

    while k <= 500:
        k = k + 1
        R = (-1)*x**2/((2*k)*(2*k+1))
        a = a * R
        S = S + a
        if k == 499:
            print("a%d = %6.2f S%d = %6.2f"%(k,a,k,S))
        if k == 500:
            print('a%d = %6.2f S%d = %6.2f'%(k,a,k,S))

    return S


print("Sin aprekinasana:")
print("")

x= float(input("Ievadi argumentu (x): "))
y = sin(x * x)
print("PC sin:", y)
print("")

yy = mans_sinuss(x)
print("My  sin:", yy)

print('Formula: y = sin(x*x)')
print('             500')
print('            ______')
print('            \\          k     4*k+2')
print('     2       \\     (-1)  *  x ')
print('sin(x)   =    |     ----------------- = 1')    
print('             /        (2 * k +1)!')
print('            /_____')
print('             k=0')

print('                                   4 ')
print('                           (-1) * x  ')
print('rekurences reizinatajs: ________________  ')
print('                         k * 2 * (2*k+1)')

