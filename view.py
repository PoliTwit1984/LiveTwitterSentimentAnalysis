import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time
style.use("ggplot")

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    pullData = open("bb2.txt","r").read()
    lines = pullData.split('\n')
    print (lines)
    xar = []
    yar = []

    x = 0
    y = 0

    for l in lines[-50:-1]:
        x=x+1
        if l!=' ':
            a=float(l)
            print(a)
            if a>0.0:
                y+=a
            elif a<0.0:
                y-=abs(a)

        xar.append(x)
        yar.append(y)
        
    ax1.clear()
    ax1.plot(xar,yar)
ani = animation.FuncAnimation(fig, animate, interval=200)
plt.show()
