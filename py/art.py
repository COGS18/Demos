"""Demo: Examples from contextfree

Source: https://github.com/undertherain/pycontextfree
"""

import sys
import math
import time

from PIL import Image

from contextfree import *

###################################################################################################
###################################################################################################

def main():

    print("\nCREATING RANDOM BRANCH EXAMPLE\n")

    # Create random branch example
    init(canvas_size=(400, 400), face_color="#44cc00", background_color="#082019", max_depth=600)
    for ind in range(10):
            random_branch()
    write_to_png('img/random_branch.png')

    # Display image
    random_branch_image = Image.open('img/random_branch.png')
    random_branch_image.show()

    time.sleep(5)

    print("\nCREATING CURLY BRANCH EXAMPLE\n")

    # Create curly branch example
    init(canvas_size=(400, 400), max_depth=400, background_color="#ffffff")
    curly_branch()
    write_to_png('img/curly_branch.png')

    # Display image
    curly_branch_image = Image.open('img/curly_branch.png')
    curly_branch_image.show()

# Note: the following functions copied from the demo in pycontextfree

@check_limits
def random_branch():

    circle(1)
    with transform(y=0.6, alpha=-0.003, angle=0.3, scale=0.998):
        if coinflip(50):
            with flip_y():
                random_branch()
        else:
            random_branch()

        if coinflip(120):
            with flip_y():
                with transform(scale=0.9):
                    random_branch()


@check_limits
def curly_branch():

    circle()
    with transform(y=0.5, angle=2, scale=0.99):
        curly_branch()
        if coinflip(80):
            with flip_y():
                with transform(scale=0.9):
                    curly_branch()


if __name__ == "__main__":
    main()
