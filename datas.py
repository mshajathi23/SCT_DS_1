
import matplotlib.pyplot as plt
import numpy as np

# Generate a sample dataset of ages (continuous variable)
np.random.seed(42)
ages = np.random.randint(18, 80, size=200)

# Create a histogram to visualize the distribution of ages
plt.figure(figsize=(8, 6))
plt.hist(ages, bins=15, color='skyblue', edgecolor='black')
plt.title('Age Distribution', fontsize=16)
plt.xlabel('Age', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.grid(True)


plt.show()

input("Press Enter to close the plot and exit...")  
