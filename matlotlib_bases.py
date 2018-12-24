%matplotlib inline
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')

fig = plt.figure()
plt.plot(x, y, linestyle='-', color='chartreuse', label = 'nom_courbe')
# plt.legend()

# create the first of two panels and set current axis
plt.subplot(2, 1, 1) # (rows, columns, panel number)
plt.plot(x, np.sin(x))
# create the second panel and set current axis
plt.subplot(2, 1, 2)
plt.plot(x, np.cos(x))

# adjusting the plot : axes limits
plt.xlim(-1, 11)
plt.ylim(-1.5, 1.5)
plt.axis([-1, 11, -1.5, 1.5])
# labeling plots
plt.title("A Sine Curve")
plt.xlabel("x")
plt.ylabel("sin(x)");

plt.scatter(x, y, marker='o') # scatter plot
plt.scatter(x, y, c=rng.rand(100), s=1000 * rng.rand(100), alpha=0.3,
            cmap='viridis')
# plot is more efficient on large dataset vs scatter, because scatter has the capacity to render a different size/color for each point

######### object oriented method 

# First create a grid of plots
# ax will be an array of two Axes objects
fig, ax = plt.subplots(2)
# Call plot() method on the appropriate object
ax[0].plot(x, np.sin(x))
ax[1].plot(x, np.cos(x))

ax = plt.axes()
ax.plot(x, np.sin(x))
# insted of calling format functions individually
ax.set(xlim=(0, 10), ylim=(-2, 2),
       xlabel='x', ylabel='sin(x)',
       title='A Simple Plot')



## visualizing errors
plt.errorbar(x, y, yerr=dy, fmt='.k');

