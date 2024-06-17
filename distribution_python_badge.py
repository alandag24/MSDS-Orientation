
#creating probability distributions for python badge

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# normal_dist_data = np.random.normal(size=1000)
# hist, bins = np.histogram(normal_dist_data, bins=50)


# plt.hist(normal_dist_data, bins=50, edgecolor='black')
# plt.ylabel('RV Values Generated 1-1000')
# plt.title('Histogram of Normal Distribution')
# plt.grid(True)
# plt.show()

#binomial distribution

# binom_dist_data = np.random.binomial(n=100, p = 0.5, size=1000)
# hist, bins = np.histogram(binom_dist_data, bins = 50)

# plt.hist(binom_dist_data, bins=50, edgecolor='black')
# plt.ylabel('RV Values Generated 1-1000')
# plt.title('Histogram of Binomial Distribution')
# plt.grid(False)
# plt.show()

#making chisquared distribution

chi_dist_data = np.random.chisquare(2,100)
hist, bins = np.histogram(chi_dist_data, bins = 50)

plt.hist(chi_dist_data, bins=50, edgecolor='black')
plt.ylabel('RV Values Generated 1-1000')
plt.title('Histogram of Chi-Square Distribution')
plt.grid(False)
plt.show()
