import matplotlib.pyplot as pt
x = [1,2,3,4,5,6,7]
y = [5,3,7,10,5,11,13]
z = [1,2,3,4,5,6,7]
a = [6,5,9,14,14,12,9]
pt.plot(x,y,z,a)
pt.title("Revenue")
pt.xlim(-10,20)
pt.ylim(0,20)
pt.show()
