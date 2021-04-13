# File:     dice_analysis.py
# Author:   Kurt Hamblin
# Description:  Analyze outputs from the dice roll simulation 

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import argparse
from Random import Random
import matplotlib
from scipy.stats import norm

# Import my custom matplotlib config and activate it
import my_params
custom_params = my_params.params()
matplotlib.rcParams.update(custom_params)



# main function for this Python code
if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    
    data = np.loadtxt('data/dice_rolls.txt', delimiter = ',')
    weights = np.loadtxt('data/dice_weights.txt', delimiter = ',')


    Nexp = np.shape(data)[0]
    Nrolls = np.shape(data)[1]


    exp_threes = np.array([])
    for i in range(Nexp):
        threes = 0
        for j in range(Nrolls):
            if data[i][j] == 3:
                threes += 1/Nrolls
        exp_threes = np.append(exp_threes, threes)
    
    mu, sigma = norm.fit(exp_threes)

    #fig, ax = make_plot(exp_threes, r'$P_3$')
    
    fig, ax = plt.subplots(figsize = (6,6))
    
    ax.hist(exp_threes, bins = 15, color = 'g', density = True, histtype = 'step', zorder = 1, linewidth = 1.5)#, hatch = '\\\ ' , linewidth = 2, alpha = 0.7)
    ax.hist(exp_threes, bins = 15, color = 'g', density = True, histtype = 'step', hatch = '\\\\ ' , linewidth = 0.5, alpha = 0.7, zorder = 0)
    
    x = np.linspace(0,1, 1000)
    ax.plot(x, norm.pdf(x, mu, sigma), linewidth = 2, c = 'r')
    
    ax.text(0.295, 19, r'$P_3 =$' +  f'{mu:.2f}' + r'$ \pm$' + f'{sigma:.2f}')
    
    ax.vlines(x = mu, ymin = 0, ymax = 25, color = 'k', ls = '--')
    
    ax.set_xlim([0.15, .43])
    ax.set_ylim([0, 21])
    ax.set_xlabel(r'$P_3$', fontsize = 16)
    ax.set_ylabel(r'Probability', fontsize = 16)
    plt.show()

