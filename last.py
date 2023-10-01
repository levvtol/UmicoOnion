import numpy as np
import matplotlib.pyplot as plt
import math

arr= np.arange(100,1000)
cassback = []
for i in arr:
    cassback.append(i/100)
plt.grid(True)
plt.plot(arr,cassback)
plt.title('1/100 Cashback')

plt.show()

equa_list = []
one_person_earn = []
cost = []
for i in arr:
    n = i
    equation = (n//500-1)*40 + (n//50-1)*7+(n//5-1)*8 + 10 + n%5
    one_person_earn2 = (n//500-1)*50 + (n//50-1)*10 +(n//5-1)*3 + n%5
    equa_list.append(equation)
    cost.append(equation*200)
    one_person_earn.append(one_person_earn2)


plt.grid(True)
fig, (ax0,ax1) = plt.subplots(2,1,constrained_layout = True)
ax0.plot(arr,equa_list,arr,one_person_earn)
ax1.plot(arr,cost)

ax0.set_title('1/100 Cashback')
ax1.set_title('how much Umico cost')
ax0.legend(['all earn','one person earn'])
fig.suptitle('Promo codes and Costs')
# 0 -1000 is fee of device
plt.show()