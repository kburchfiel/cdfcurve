#Program for plotting both the normal distribution and its corresponding cumulative density function
#Helpful references included: 
#http://home.ustc.edu.cn/~lipai/auto_examples/plot_exp.html
#https://courses.csail.mit.edu/6.867/wiki/images/3/3f/Plot-python.pdf
#https://matplotlib.org/tutorials/introductory/pyplot.html
#https://stackoverflow.com/questions/28504737/how-can-i-plot-a-single-point-in-matplot-python/44420447
#https://stackoverflow.com/questions/20130227/matplotlib-connect-scatterplot-points-with-line-python
import matplotlib.pyplot as plt
import numpy as np
from statistics import NormalDist
xset = np.arange(-3.5,3.5,0.01)
b = 0 #b = mean
c = 1 #c = standard deviation
zscores = []
percentiles = []
#As a newcomer to Python, I am not aware of a way to plot the cumulative density function of the normal distribution as a continuous line. Instead, I will generate 751 points along this line (representing z scores of -3.5 to 3.5), add them to two lists, and then plot the lists as a line graph.
for i in range (-350,351,1): #We will divide i by 100 so that it can represent z scores in .01 increments from -3.5 to 3.5
    zscore = i/100
    percentile = NormalDist(mu=b, sigma=c).cdf(zscore)
    print(f"A z score of {zscore} corresponds to a percentile of {percentile}.") #This prints out each z score-percentile pair, but can be commented out if desired.
    zscores.append(zscore) #Building our list of zscores
    percentiles.append(percentile) #Building our corresponding list of percentiles
    plt.plot(zscores,percentiles)
yset2 = (1/(c*(2*np.pi)**(1/2)))*np.exp(-1/2*((xset-b)/c)**2) #Normal distribution function
plt.plot(xset,yset2)
plt.show()

