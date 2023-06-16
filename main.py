import numpy as np
import matplotlib.pyplot as plt
from matpar import parent as par

def NewtonRaphson(f, x0, decPlace):
    xm = x0
    for i in range(10):
        print(f"{xm}, {f.computeAt(xm)}, {f.derivative().computeAt(xm)}, {f.computeAt(xm) / f.derivative().computeAt(xm)}")
        
        xn = xm - (f.computeAt(xm) / f.derivative().computeAt(xm))
        xm = xn
    return (np.round(xn, decPlace))

f0 = par.polynomial(2, (1, 2, -50))
print(NewtonRaphson(f0, -20, 4))

#(int(np.floor(xn*(10**decPlace))) != int(np.floor(xm*(10**decPlace))))