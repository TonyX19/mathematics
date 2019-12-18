import math
from sympy import *

######################
#basic calculation
math.sqrt(2) ** 2
sympy.sqrt(2) ** 2

x = sympy.Symbol('x')
sympy.sqrt(x) ** 2
sympy.sqrt(8)

#为什么用sympy的计算结果貌似要比math单纯浮点计算后误差小很多，或者说基本没有？
#因为sympy的计算本质是符号计算，也就是它先计算 [公式] ，sympy先将其化简为 [公式] ，在代入求值。

x = Symbol('x')
y = Symbol('y')
z = Symbol('z')
a = Symbol('a')
b = Symbol('b')
c = Symbol('c')
# 等同于 x, y, z, a, b, c = symbols('x, y, z, a, b, c')
# 建议用下面这种表达，因为一个一个导入符号实在是太麻烦了。
f = (2/3)*x**2 + (1/3)*x**2 + x + x + 1

#simplify the expression f
f.simplify()

#expand the expression
f = (x+1)**2
expand(f)
#x**2 + 2*x + 1


#solve方程自动求解
f1 = 2*x - y + z - 10
f2 = 3*x + 2*y - z - 16
f3 = x + 6*y - z - 28
solve([f1, f2, f3])
#{x: 46/11, z: 74/11, y: 56/11}
##############################


###########################
#diff求导 differentiate /ˌdɪfəˈrenʃieɪt/
#diff(你的函数，自变量，求导的次数）
diff(sin(2*x), x)
#2*cos(2*x)
sin(2*x).diff(x) 
#2*cos(2*x)
diff(sin(2*x), x, 2) 
#-4*sin(2*x)
diff(sin(x*y), x,2,y,3) 
#x*(x**2*y**2*cos(x*y) + 6*x*y*sin(x*y) - 6*cos(x*y))

#偏微分 Partial differential equation
x=sympy.symbols('x')#约定变量x
y=x**3+10+sympy.sin(x)#这个sin是sy的sin
dy_dx=sympy.diff(y,x)#常微分，写成dy_dx=sy.diff(y)也可以

t=sympy.symbols('t')
z=x*sympy.ln(t)+t**4
dz_dt=sympy.diff(z,t)#偏微分

print(dy_dx.subs({x:5}))#把x=5代入
print(dy_dx.subs({x:5}).n(10))#转浮点，总位数为10

#Second order differential

x=sy.symbols('x')
print(sympy.diff(sympy.sin(x),x,2))#二阶微分

################

#######################
#Riemann integral /ˈɪntɪɡrəl/ ~ Integral
x = Symbol('x')
f = 1 / (1 + E ** x) ** 2
f, integrate(f, (x, 0, +oo))

#Multiple integral

f = (4/3)*x + 2*y
integrate(f, (x, 0, 1), (y, -3, 4))
#21/2

#######################

######################
#Improper Integral
f = 3*x**2 + 1
integrate(f, x)
#x**3 + x

#Multiple Improper integral
f = (4/3)*x + 2*y
integrate(f, (x, 0, 1), (y, -x, x))
#x

###############

