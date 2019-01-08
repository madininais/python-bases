%matplotlib inline #static plot embedded in the noetbook
%matplotlib notebook #interactve plot embedded in the noetbook

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

# hitograms
plt.hist(data, databins=30, normed=True, alpha=0.5,
                    histtype='stepfilled', color='steelblue',
                    edgecolor='none'))

# visualizing errors
plt.errorbar(x, y, yerr=dy, fmt='.k') # basic errobars

# 2D histgrams and binnings



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
ax[0].legend(['input'], loc=2)
ax[0].get_xticklabels()[4].set(weight='heavy', color='red') # get_xticklabels to access x labels
ax[0].axvline(local_max, alpha=0.3, color='red')

labels = ax.get_xticklabels()
plt.setp(labels, rotation=45, horizontalalignment='right')

ax.barh(x,y)
ax.axvline(x, ls='--', color='r')

## style / themes
print(plt.style.available)
plt.style.use('fivethirtyeight')




