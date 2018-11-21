"""Demonstration script: conversation."""

import os
import time

def main():

    os.system('say hello from your computer')

    time.sleep(2)

    os.system('say Python is great. -v Fred')

if __name__ == "__main__":
    main()