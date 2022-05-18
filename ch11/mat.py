from matplotlib import pyplot as p
y=[1,2,3,4,5]
x=range(len(y))
p.plot(x,y,color='red')
p.scatter(x,y,linewidths=3,color='yellowgreen')
p.bar(x,y,width=0.3,color='black')
p.show()