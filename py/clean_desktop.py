"""Demo: clear generated files from desktop."""

import os
import shutil

from settings.files import *

###################################################################################################
###################################################################################################

def main():

    print('\nCLEANING UP DESKTOP\n')

    # Move to path
    os.chdir(PATH)

    # Remove files
    for file in FILES:
        os.remove(file)

    shutil.rmtree(DAT_FOLDER)

if __name__ == "__main__":
    main()