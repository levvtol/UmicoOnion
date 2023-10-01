import matplotlib.pyplot as plt
import numpy as np

arr = np.arange(40,1000)
# n = int(input('enter number n:'))

equa_list = []
cost = []
for i in arr:
    n = i
    equation = (n//500-1)*40 + (n//50-1)*7+(n//5-1)*8 + 10 + n%5
    equa_list.append(equation)
    cost.append(equation*200)


fig, (ax0,ax1) = plt.subplots(2,1,constrained_layout = True)
p = ax0.plot(arr,cost,'.')
# add title and x/y names
m = ax1.plot(arr,equa_list,'.',color='red')
ax0.grid(True)
ax1.grid(True)
ax0.set_title('Cost')
ax1.set_title('Customer')

# ax[1].title('Costumers')
plt.show()