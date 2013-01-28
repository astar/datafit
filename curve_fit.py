import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import scipy as sy
import pylab as plb  

data = plb.loadtxt('data.dat')  
x = data[:,0]
y= data[:,1]

def func(x, a, b, c, d):
  return a*x**3 +b*x**2 + c*x +d

p0 = sy.array([1,1,1,1])
coeffs, matcov = curve_fit(func, x, y, p0)

yaj = func(x, coeffs[0], coeffs[1], coeffs[2], coeffs[3])
print(coeffs)
print(matcov)

plt.plot(x,y,'x',x,yaj,'r-')
plt.show()