import math
from sympy import *

#Riemann integral /ˈɪntɪɡrəl/ ~ Integral
x = Symbol('x')
f = 1 / (1 + E ** x) ** 2
f, integrate(f, (x, 0, +oo))





#Improper Integral
