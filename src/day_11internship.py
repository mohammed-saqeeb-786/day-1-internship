import matplotlib.pyplot as plt

x =[1,2,3,4,5]
y =[5,4,3,2,1]

plt.scatter(x,y)
plt.show()


import matplotlib.pyplot as plt

categories =['A','B','C']
value =[11,20,50]
plt.bar(categories,value)
plt.show()

import matplotlib.pyplot as plt

plt.subplot(1,2,1)
plt.plot([1,2,3], [1,4,9])
plt.title("line bar")
plt.subplot(1,2,2)
plt.bar(['A','B','C'], [3,7,5])
plt.title(" bar chart")
plt.show()


#task1
import matplotlib.pyplot as plt

months=[1,2,3,4,5]
revenue=[2000,4500,4000,7500,9000]
plt.plot(months,revenue)
plt.tittle=("Months Revenue Growth")
plt.xlable("months")
plt.ylable("revenue in as dollar")
plt.show()