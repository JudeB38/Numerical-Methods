import numpy as np
import matplotlib.pyplot as plt

class parent:
    class polynomial:
        def __init__(self, order, coeff):
            self.order = order
            if len(coeff) == (order+1):
                self.coeff = np.array([coeff[i] for i in range(order+1)])
            else:
                raise Exception("Coefficients does not match order")
            
        def computeAt(self, x):
            output = 0
            for i in self.coeff:
                output = output*x
                output += i
                
            return output
        
        def computeRange(self, a, b, dx=0.01):
            ran = np.arange(a, b+dx, dx)
            yList = []
            yList.append(self.computeAt(ran))
            return np.array(yList)
        
        def iofuncLists(self, a, b, dx=0.01):
            xL = []
            i = a
            while i <= b:
                xL.append(i)
                i += dx
            xA = np.array(xL)
            yA = self.computeRange(a, b, dx)
            return (xA, yA[0])
        
        def derivative(self):
            dcoeff = []
            for i in range(self.order, 0, -1):
                dcoeff.append(self.coeff[self.order - i] * i)
            return parent.polynomial(self.order-1, dcoeff)
        
        def nDerivative(self, n):
            i = n
            outPol = self
            while i > 0:
                outPol = outPol.derivative()
                i -= 1
            return outPol
