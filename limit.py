import math
from sympy import *

##########################
#limit
f = (x+1)**2 + 1
# x = a - 1 
limit(f, x, a-1) 
#a**2 + 1

#lim(x->0) sinx/x
f = sin(x)/x
limit(f, x, 0)
#1

#limit(f, x, 0)
print(limit(f, x, 0, dir='-'))
#1

#ƒ(x) = cos(x);limit(Δx->0) [ƒ(x) - ƒ(a-Δx)]/Δx
f = cos(x)
dx = Symbol('dx') #dx ~ Δx
print(limit(f, x, a)) # 这个的意思是函数f，自变量x用a代入
print(limit(f, x, a-dx))# f的自变量x用a-dx代入
print(limit((limit(f,x,a)-limit(f,x,a-dx))/dx, dx, 0))
#-sin(a) #这就是答案

n = Symbol('n')
print(limit(((n+3)/(n+2))**n, n, oo))
#E
#无穷用oo表示，负无穷用-oo
############################