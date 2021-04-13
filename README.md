# PHSX815 Project 3
## Estimating Dice Roll Probability
### Description:
For this project, I simulate rolls of a dice with weights drawn from a normal distribution, and I attempt to reconstruct the true probability of side 3 being rolled. 

### Usage
All python scripts can be ran from the command line with the `-h` or `--help` flags to display all the options. 

#### dice_exerpiement.py
This file simulates dice rolls for Nexp experiments with Nrolls number of rolls. It saves the output to 'datadice_rolls.txt'

python dice_experiment.py --seed --Nrolls --Nexp

#### anaylsis.py
This file constructs the side '3' histogram, and fits a normal dsitrbution to estimate the true value of a 3 being rolled. 
It loads the data from 'datadice_rolls.txt'

python analysis

#### Neyman_Construction.py
This file creates the Neyman Construction plot for simulations of 100 experiments with 10, 100, and 1000 rolls each. 

python Neyman_Construction.py
