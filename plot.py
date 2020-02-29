import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random
import statistics
from collections import Counter

plt.style.use('fivethirtyeight')

x = []
y = []
sec_std_upper = []
sec_std_lower = []
third_std_upper = []
third_std_lower = []
avg = []
diff = []

index = 0

#create a figure with two subplots
fig = plt.figure()
gs = fig.add_gridspec(2, 2)
ax1 = fig.add_subplot(gs[0,:])
ax2 = fig.add_subplot(gs[1,0])
ax3 = fig.add_subplot(gs[1,1])


def animate(i):
    global index
    size_y = len(y)
    num = random.randrange(25,51)

    if size_y < 2 :
        x.append(index)
        y.append(num)
        avg.append(num)
        sec_std_lower.append(num)
        sec_std_upper.append(num)
        third_std_lower.append(num)
        third_std_upper.append(num)

    elif size_y >= 2 and size_y < 4:
        if num < statistics.mean(y) + 2*statistics.stdev(y) and num > statistics.mean(y) - 2*statistics.stdev(y):
            y.append(num)
            x.append(index)
            avg.append(statistics.mean(y))
            sec_std_lower.append(statistics.mean(y)-2*statistics.stdev(y))
            sec_std_upper.append(statistics.mean(y)+2*statistics.stdev(y))
            third_std_lower.append(statistics.mean(y)-3*statistics.stdev(y))
            third_std_upper.append(statistics.mean(y)+3*statistics.stdev(y))

    else:
        if num < statistics.mean(y) + 2*statistics.stdev(y) and num > statistics.mean(y) - 2*statistics.stdev(y):
            y.append(num)
            x.append(index)
            avg.append(sum(y[-5:])/5)
            sec_std_lower.append(statistics.mean(y)-2*statistics.stdev(y))
            sec_std_upper.append(statistics.mean(y)+2*statistics.stdev(y))
            third_std_lower.append(statistics.mean(y)-3*statistics.stdev(y))
            third_std_upper.append(statistics.mean(y)+3*statistics.stdev(y))

    index = index + 1

    if(len(y) == 1):
        diff.append(0)
    else:
        diff.append(y[-1]-y[-2])

    diff_dict = Counter(diff)

    ax1.cla()
    ax1.plot(x, y, label='random number')
    ax1.plot(x, avg, label='moving avg')
    ax1.plot(x, sec_std_lower, label='2nd sd')
    ax1.plot(x, sec_std_upper, label='2nd sd')
    ax1.plot(x, third_std_lower, label='3rd sd')
    ax1.plot(x, third_std_upper, label='3rd sd')
    ax1.legend()
    ax1.set_title('Random Number Plot')

    ax2.cla()
    ax2.plot(x, avg, label='moving avg', color='red')
    ax2.legend()
    ax2.set_title('Moving Avg')

    ax3.cla()
    ax3.bar(diff_dict.keys(), diff_dict.values())
    ax3.set_title('Rate of Change')

ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()
