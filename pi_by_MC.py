import numpy as np
import matplotlib.pyplot as plt
import time
#Function to estimate the value of pi using Monte Carlo method and Uniform distribution
def est_pi(nn):
	circle = 0
	start_time = time.time()
	for i in range(nn):
		x = np.random.uniform(-1, 1)
		x_val[i] = x
		y = np.random.uniform(-1, 1)
		y_val[i] = y
		if x**2 + y**2 <= 1:
			circle += 1
			pi_estimate = (circle / nn) * 4
			end_time = time.time()
	time_total = end_time - start_time
return pi_estimate, time_total
error = np.zeros(7)
time_all = np.zeros(7)
pi_value = np.zeros(7)
N = np.zeros(7)
for i in range(7):
nn = 10**(i+2)
N[i] = nn
x_val = np.zeros(nn)
y_val = np.zeros(nn)
pi_value[i], time_all[i] = est_pi(nn)
error[i] = (abs(np.pi - pi_value[i])/np.pi)*100
print(f"Estimated value of pi with {nn} samples:
{pi_value[i]}")
print(f"Error: {error[i]}%")
print(f"Time taken: {time_all[i]} seconds")
print("-------------------------------")



# Plotting the points
plt.figure(figsize=(6,6))
plt.title(f'Monte Carlo Pi Estimation with N={nn}\n')
plt.scatter(x_val, y_val, s=5)
circle = plt.Circle((0, 0), 1, color='r', fill=False,
linewidth=2)
plt.gca().add_artist(circle)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.savefig(f'monte_carlo_pi_python_{N[i]}.png')
plt.xlim(-1, 1)
plt.ylim(-1, 1)
# Plotting the points
plt.figure(figsize=(6,6))
plt.plot(np.log(N),error, marker="o")
plt.title('Error vs Sample size\n')
plt.xlabel('Sample size (N)')
plt.ylabel('Error (%)')
plt.grid(True)
plt.savefig(f'Error_vs_sample_size.png')
