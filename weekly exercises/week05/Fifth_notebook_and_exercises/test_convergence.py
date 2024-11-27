#Import the SimpsonIntegration class from the SimpsonIntegration file
from SimpsonIntegration import SimpsonIntegration

#Import other modules/functions required
import numpy as np
from scipy.integrate import simps

#Define the function that we want to integrate
# This should take exactly one argument, since we call the function
# in the simpson() static method
def myfunc(x):
    return np.exp(-x) * x**5
#Define the integration limits
xmin = 0
xmax = 1

#Create an instance of the SimpsonIntegration class
my_integral = SimpsonIntegration(myfunc, 1E-4)
#Actually perform the integration
result = my_integral.evaluate(xmin, xmax)
print("The result of your integral with an EPS of {0:e} is {1:.5f}".format(my_integral.eps, result))

#Now compare with scipy's simps() method
#For this, you can setup the x values you want to use to evaluate the function over
Nc = 10
x = np.linspace(xmin,xmax,Nc+1)
y = myfunc(x)
scipy_res = simps(y,x)
print("The result of your integral carried out with scipy simps() is {0:.5f}".format(scipy_res))

#Check the difference between our SimpsonIntegration result & the scipy result
print("The difference between our result & scipy is {0:.8f}".format(result - scipy_res))


#Exercise 1
# Now write a code to integrate sin(exp(x)) between -pi and pi using SimpsonIntegration
# The code should provide the result with a precision of 1e-3.
# Compare your result with the result provided by scipy.integrate.quad

#Exercise 2
# Now write a code to integrate np.exp(-x) * x**5 between 0 and 1E5 using SimpsonIntegration.simpson()
#  for a number of intervals between 2 and (around) 1E5. A step size of ~1000 is sufficient.
# You should store the result of each integration, and plot (using matplotlib) how the result converges.

#Exercise 3
# Following on from Exercise 2, evaluate the integratal with SimpsonIntegration.evaluate()
# Compare the answer with the result from your last evaluation in Exercise 2.
# How might you modify the SimpsonIntegration evaluate() method to allow convergence to the correct answer in this case?