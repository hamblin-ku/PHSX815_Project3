# File:     Neyman_Construction.py
# Author:   Kurt Hamblin
# Description:  Neyman Constructionof '3' rolls

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from Random import Random
import matplotlib

# Import my custom matplotlib config and activate it
import my_params
custom_params = my_params.params()
matplotlib.rcParams.update(custom_params)

# sample data with rayleigh dist
def sample_data(Nexp, Nroll):
    rand = Random()
    
    
    mu_true_arr = np.array([])
    mu_meas_arr = np.array([])
    
    for i in range(0, 101, 1):
        mu_true = i/100.
        
        for j in range(Nexp):
            mu_meas = 0
            prob_rest = (1-mu_true)/5
            weights = np.array([prob_rest, prob_rest, mu_true, prob_rest, prob_rest, prob_rest])
            
            for k in range(Nroll):
                val = rand.roll_die( weights = weights )
                if val == 3:
                    mu_meas += 1 / Nroll
            mu_true_arr = np.append(mu_true_arr, mu_true)
            mu_meas_arr = np.append(mu_meas_arr, mu_meas)
    
    return mu_meas_arr, mu_true_arr




# main function for this Python code
if __name__ == "__main__":

    Nexp = 100
    
    rolls = np.array([10,100, 1000])

    rolls10_meas, rolls10_true = sample_data(Nexp, rolls[0])
    print('1 loaded')
    rolls100_meas, rolls100_true = sample_data(Nexp, rolls[1])
    print('2 loaded')
    rolls1000_meas, rolls1000_true = sample_data(Nexp, rolls[2])

    fig, ax = plt.subplots(nrows= 1, ncols = 3, figsize = (12,5))
    ax[0].set_ylabel(r'$P_{3,meas}$',fontsize = 18)
    ax[0].set_xlabel(r'$P_{3,true}$',fontsize = 18)
    ax[1].set_xlabel(r'$P_{3,true}$',fontsize = 18)
    ax[2].set_xlabel(r'$P_{3,true}$',fontsize = 18)
    
    hist1 = ax[0].hist2d(x = rolls10_true, y = rolls10_meas, bins = [10,10] , density = True, alpha = 1.0, cmap='Blues')
    hist2 = ax[1].hist2d(x = rolls100_true, y = rolls100_meas, bins = [10,10] , density = True, alpha = 1.0, cmap='Blues')
    hist3 = ax[2].hist2d(x = rolls1000_true, y = rolls1000_meas, bins = [10,10] , density = True, alpha = 1.0, cmap='Blues')
    
    cbar1 = plt.colorbar(hist1[3], orientation="horizontal", fraction=0.06, pad=0.18, ax = ax[0])
    cbar2 = plt.colorbar(hist2[3], orientation="horizontal", fraction=0.06, pad=0.18, ax = ax[1])
    cbar3 = plt.colorbar(hist3[3], orientation="horizontal", fraction=0.06, pad=0.18, ax = ax[2])

    cbar1.set_label('Probability Density', fontsize = 18)
    cbar2.set_label('Probability Density', fontsize = 18)
    cbar3.set_label('Probability Density', fontsize = 18)

    ax[0].text(0.6,0.2, r'$N_{rolls} = 10$', fontsize = 18)
    ax[1].text(0.57,0.2, r'$N_{rolls} = 10^2$', fontsize = 18)
    ax[2].text(0.57,0.2, r'$N_{rolls} = 10^3$', fontsize = 18)
    
    ax[0].set_xlim([0,1])
    ax[0].set_ylim([0, 1])
    
    ax[1].set_xlim([0,1])
    ax[1].set_ylim([0, 1])
    
    ax[2].set_xlim([0,1])
    ax[2].set_ylim([0, 1])
    
    plt.show()
