"""Demo: HyperPlots"""

import time

import numpy as np

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import hypertools as hyp

###################################################################################################
###################################################################################################

def main():

    # Display EEG picture
    plt.imshow(mpimg.imread('img/EEG.jpg'))
    plt.show()

    time.sleep(5)

    # Load data - aligned data
    avg_al_1 = np.load('dat/avg_al_1.npy')
    avg_al_2 = np.load('dat/avg_al_2.npy')

    # Load data - unaligned data
    avg_una_1 = np.load('dat/avg_una_1.npy')
    avg_una_2 = np.load('dat/avg_una_2.npy')

    # Trajectories - Unaligned
    hyp.plot([avg_una_1.T, avg_una_2.T], animate=True, rotations=1)

    time.sleep(2)

    # Trajectories - Aligned
    hyp.plot([avg_al_1.T, avg_al_2.T], animate=True, rotations=1)

    # Display MEG picture
    plt.imshow(mpimg.imread('img/MEG.jpg'))
    plt.grid(False)
    plt.show()

if __name__ == "__main__":
    main()