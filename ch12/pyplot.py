# from matplotlib.pyplot import *
import matplotlib.pyplot as plt

y=[5,3,7,10,9,5,3.5,8]
x=range(len(y))
#bar(x,y,width=0.7,color="blue")
plt.bar(x,y,color='red')
# scatter(x,y,linewidths=5,color='gray')
# grid(True)
plt.show()