import numpy as np
import matplotlib.pyplot as plt

num_simulations = 10000

totals = np.zeros(num_simulations)

for i in range(num_simulations):
    totals[i] = np.random.randint(1, 7, 3).sum()

hist_data = plt.hist(totals, bins=range(3, 20), edgecolor='black', linewidth=1)
plt.xlabel('Total')
plt.ylabel('Frequency')
plt.title('Distribution of Dice Totals')
plt.show()

print(hist_data)