import math
from sympy import *


############################
#Ordinary Differential Equations
t = sympy.Symbol('t')
c = sympy.Symbol('c')
domain = np.linspace(-3,3,100)
v = t**3-3*t-6
a = v.diff()

for p in np.linspace(-2,2,20):
    slope = a.subs(t,p)
    intercept = sympy.solve(slope*p+c-v.subs(t,p),c)[0]
    lindomain = np.linspace(p-1,p+1,20)
    plt.plot(lindomain,slope*lindomain+intercept,'red',linewidth = 1)

plt.plot(domain,[v.subs(t,i) for i in domain],linewidth = 2)



#dsolve() 计算微分方程 Differential equation

x = symbols("x", real=True) # 定义符号x 为实数 
eq1 = dsolve(f(x).diff(x) + f(x)**2 + f(x), f(x)) 
eq1
#f(x) == -C1/(C1 - exp(x))
#如果设置hint参数为“best”,就能得到更简
#单的显函数表达式

eq2 = dsolve(f(x).diff(x) + f(x)**2 + f(x), f(x), hint="best")
eq2
#f(x) == -C1/(C1 - exp(x))

#Taylor Series
x = sympy.Symbol('x')
# exp为公式
exp = e**x
# 下面开始求和,就求前21项的和吧
sums = 0
for i in range(20):
    # 求i次导函数
    numerator = exp.diff(x,i)
    # 计算导函数在x=0处的值
    numerator = numerator.evalf(subs={x:0})
    denominator = np.math.factorial(i)
    sums += numerator/denominator*x**i

# 下面检验一下原始的exp函数和其在x=0处展开的泰勒级数前20项之和的差距
print(exp.evalf(subs={x:0})-sums.evalf(subs={x:0}))
# result is 0
xvals = np.linspace(0,20,100)

for xval in xvals:
    plt.plot(xval,exp.evalf(subs={x:xval}),'bo',\
             xval,sums.evalf(subs={x:xval}),'ro')
