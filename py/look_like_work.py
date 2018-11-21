""".  """

import os

from settings.files import *

###################################################################################################
###################################################################################################

def main():

    print('\nFILLING DESKTOP WITH WORK\n')

    # Change directory
    os.chdir(PATH)

    for file in FILES:
        os.system('touch ' + file)

    os.system('mkdir ' + DAT_FOLDER)
    os.chdir(os.path.join(PATH, DAT_FOLDER))
    for dat_file in DAT_FILES:
        os.system('touch ' + dat_file)

if __name__ == "__main__":
    main()
