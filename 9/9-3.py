# ----------- Chain reaction process -----------
import numpy as np
import matplotlib.pyplot as plt

t_half_Bi213 = 45.6  # min
t_half_Tl209 = 2.2  # min
t_half_Pb209 = 3.3*60  # min (3.3 h)

lambda_Bi213 = np.log(2)/t_half_Bi213
lambda_Tl209 = np.log(2)/t_half_Tl209
lambda_Pb209 = np.log(2)/t_half_Pb209

p_alpha = 0.0209  # Bi213 -> Tl209 -> Pb209 -> Bi209 alpha decay
p_beta = 0.9791  # Bi213 -> Po213 -> Pb209 -> Bi209 beta decay

t = 0
dt = 0.01

N_Bi213 = 100000
N_Tl209 = 0
N_Pb209 = 0
N_Bi209 = 0
time, N1, N2, N3, N4 =[0], [100000], [0], [0], [0]  # list for plot

while N_Bi209 <= N_Bi213:

    # Bi213 decay, p = lambda* dt is the probability of decay in such a short time
    decay_Bi213 = np.random.rand(N_Bi213) < lambda_Bi213*dt
    N_decay_Bi213 = np.sum(decay_Bi213)  # np.sum(boolean) collects all the 'True's as '1's

    # roll the dice to decide how to decay
    beta_decay_Bi213 = np.random.rand(N_decay_Bi213) < p_beta
    N_beta_decay_Bi213 = np.sum(beta_decay_Bi213)
    N_alpha_decay_Bi213 = N_decay_Bi213 - N_beta_decay_Bi213

    # update the number of particles
    N_Bi213 -= N_decay_Bi213
    N_Pb209 += N_beta_decay_Bi213  # middle product Po213 decay instantly -> Pb209 
    N_Tl209 += N_alpha_decay_Bi213

    # Tl209 decay
    decay_Tl209 = np.random.rand(N_Tl209) < lambda_Tl209*dt
    N_decay_Tl209 = np.sum(decay_Tl209)
    N_Tl209 -= N_decay_Tl209
    N_Pb209 += N_decay_Tl209

    # Pb209 decay
    decay_Pb209 = np.random.rand(N_Pb209) < lambda_Pb209*dt
    N_decay_Pb209 = np.sum(decay_Pb209)
    N_Pb209 -= N_decay_Pb209
    N_Bi209 += N_decay_Pb209

    # update the time and list for plot
    t += dt
    time.append(t)
    N1.append(N_Bi213)
    N2.append(N_Tl209)
    N3.append(N_Pb209)
    N4.append(N_Bi209)

print(f"After {t} minutes, N_Bi209 > N_Bi213")

# plot the line chart
plt.plot(time, N1, 'r-', label='Bi213')
plt.plot(time, N2, 'b-', label='Tl213')
plt.plot(time, N3, 'g-', label='Pb209')
plt.plot(time, N4, 'y-', label='Bi209')
plt.legend()
plt.show()

# plot the bar chart
name = ['Bi213','Po213', 'Tl209', 'Pb209', 'Bi209']
counts = [N_Bi213,0, N_Tl209, N_Pb209, N_Bi209]
plt.bar(name, counts, color='skyblue', edgecolor='black')
plt.show()