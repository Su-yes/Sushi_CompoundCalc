# -*- coding: utf-8 -*-
"""
Compounding Interest calculator
author: Suyash Bhattarai
"""
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from colors import get_color

matplotlib.rcParams.update(matplotlib.rcParamsDefault)

# for latex rendering
plt.rcParams['text.usetex'] = True
plt.rcParams['font.size'] = 12
plt.rcParams['font.family'] = "serif"

# Initialize parameters
# 385*2 + 500 + 300
deposit = 100
m_contribution = 888 + 500

retire_age = 65
current_age = 24
time = retire_age - current_age

return_rate = 6
n = 1

# calculations
ror = return_rate/100
t = np.arange(1,time+1)
A = np.zeros((time,1))
interest = np.zeros((time,1))
contribution = np.zeros((time,1))

y_contribution = m_contribution*12


for i in range(0,time):
    if i == 0:
        # year 1 
        yr = 1
        temp_A = deposit + y_contribution
        A[i] = temp_A*(1 + ror/n)**(n*yr)
        interest[i] = A[i] - temp_A
        contribution[i] = deposit + y_contribution
        
    else:
        # year 2 onwards. Make addition at the beginning of compounding period
        
        yr = 1 # locally year = 1 because calculating for each year
        contribution[i] = contribution[i-1] + y_contribution
        temp_A = A[i-1] + y_contribution
        A[i] = temp_A*(1 + ror/n)**(n*yr)   
        interest[i] = A[i] - contribution[i]
          
# fig = plt.figure()  # an empty figure with no Axes
# fig, ax = plt.subplots()  # a figure with a single Axes
# ax.plot(t,principal,'-r', t, interest,'k')

# =============================================================================
# Calculate pension 

avg_sal = 170000

if retire_age >= 62:
    factor = 0.011
    pension = factor*avg_sal*time
    
else:
    factor = 0.01
    pension = factor*avg_sal*time

print("\nYour pension after {} years at the age of {} is: ${:,.0f} per year.".format(time, retire_age, pension))

# =============================================================================
# Start Plots

fig = plt.figure()
fig, ax = plt.subplots()

years = t.flatten()
money = contribution.flatten()
intrst = interest.flatten()
total = money + intrst

col = "blue orange feelings"
ax.bar(years, money, width = 0.5, color = get_color(col)[2])
ax.bar(years, intrst, width = 0.5, bottom = money, color = get_color(col)[0])
ax.set_xlim(0.5, time + 0.5)
ax.set_xticks([1, int(time/2)+1, time])
ax.set_xlabel('Years')
ax.set_ylabel('Balance')
ax.legend(["Principal", "Interest"], loc = 2, frameon = False)

# Display final values
ax.text(1, 0.8*int(total[-1]), "Final Amount: \${:,.0f}".format(total[-1]), fontsize = 11)
ax.text(1, 0.74*int(total[-1]), "Pension: \${:,.0f}".format(pension, fontsize = 11))
ax.text(1, 0.68*int(total[-1]), "4\% Withdraw: \${:,.0f}".format(0.04*total[-1], fontsize = 11))

# Changes the y axis to currency. 
fmt = '\${x:,.0f}'
tick = mtick.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick)
plt.tight_layout()
plt.savefig('Result.png', dpi = 1200)

# =============================================================================

