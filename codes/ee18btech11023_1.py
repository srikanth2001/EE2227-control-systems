import numpy as np
import control
import matplotlib.pyplot as plt


num = 20
den = [1,1,0]

num1 = [1,3]
den1 = [1,4]
#Creating a transfer function G = num/den
G = control.tf(num,den) 
H = control.tf(num1,den1)

control.nyquist(G*H);
print("Roots of the the polynomial:")
print(np.roots([1,5,4,0]))
plt.grid(True)
plt.title('Nyquist Diagram of G(s)*h(s) = 20(s+3)/s(s+1)(s+4)')
plt.xlabel('Re(s)')
plt.ylabel('Im(s)')
plt.show()
