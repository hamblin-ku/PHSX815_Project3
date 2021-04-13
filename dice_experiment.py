# File:     dice_experiment.py
# Author:   Kurt Hamblin
# Description:  Utitlize the Random Class to:
# Simulate dice rolls where the dice weights are sampled from a normal distribution

from Random import Random
import numpy as np
import argparse

# main function for this Python code
if __name__ == "__main__":
    
    # Set up parser to handle command line arguments
    # Run as 'python monopoly_experiment.py -h' to see all available commands
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", "-s", help="Seed number to use")
    parser.add_argument("--Nrolls",  help="Number of rolls")
    parser.add_argument("--Nexp",  help="Number of rolls")
    args = parser.parse_args()

    # default seed
    seed = 5555
    if args.seed:
        print("Set seed to %s" % args.seed)
        seed = args.seed
    random = Random(seed)

    Nrolls = 100
    if args.Nrolls:
        print("Number of rolls per experiment: %s" % args.Nrolls)
        Nrolls = np.uint64(args.Nrolls)
     
    Nexp = 1000
    if args.Nexp:
        print("Number of experiments: %s" % args.Nexp)
        Nexp = np.uint64(args.Nexp)
    
    # Create weights by pulling from normal distribution
    weights = abs(np.random.normal(size=Nsides))
    # The weigths need to sum to one, so normalize them
    weights /= weights.sum()

    # The weigths need to sum to one, so normalize them
    weights /= weights.sum()
    np.savetxt('data/dice_weights.txt', weights, delimiter = ',')
    
    print(f'True probability of rolling a 3: {weights[2]:.3f}')
    
    rolls = np.zeros((Nexp, Nrolls))
    for i in range(Nexp):
        for j in range(Nrolls):
            rolls[i,j] = random.roll_die(Nsides = Nsides, weights = weights)

    # Save the normalized results
    np.savetxt('data/dice_rolls.txt', rolls, delimiter = ',', fmt="%d")

    
