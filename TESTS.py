#3.labaratorijas darbs
#Ielādējam savu repozitāriju terminālā un islēdzam  idle & vidi kur sākam veidot funkciju 
#Aptuveni novērtējot funkcijas saknes vertību lietojo "peli" iegūstam x =

from math import sinh,fabs

from time import sleep
#sys importē iebūvēto moduli (bibliotēku), kas nosaukts sys.


def f(x):
    return sin(x*x)

k = 0
a = 1
b = 5

#Ierakstām dotos un to vērtības

from numpy import *
from matplotlib import pyplot as plt
x = linspace(0 , 4 , 70)
y = sin(x*x)

#Ierādām kādās robežas ir noteiktais grafiks ka arī pierakstām grafiku kurš tiks attēlots

plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Funkcija $sin(x*x)$')
plt.plot(x, y, color = '#FF0000',linewidth = 1.0)
plt.show()

#ar plt. ieviešam funkcijas attelošanos ar plt.plot ierakstām pieškirto grafika krāsu un pieprasām visu attēlot
funa = f(a)
fnub = f(b)


if (funa*fnub >0.0):
    print('Dotajā intervālā [%s,%s] sakņu nav'%(a,b))
    sleep(1);exit()
else:
    print('Dotajā intervālā sakne(s) ir!')
deltax = 0.0001

#Pieškiram salidzinājumu a un b ka ja sareizinot a un b tiem ir jābut lielākiem par 0 vertību un tad norādām kurā intervalā skanes ir bet kura nav 
while(fabs(b-a) > deltax):
    k = k+1
    x=(a+b)/2.;funx=f(x)
    print(a,b,x)
    if(funa*fnub < 0.):
        b = x
    else:
        a = x

print('Sakne ir: ',x)
print('Sakne ir: ',f(x))
print('Interāciju skaits k = ',k)

#Pieprasām izvadīt skaitļus kuri norāda saknes un interāciju skaitu
