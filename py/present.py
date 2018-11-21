"""Demos: psychopy presentation."""

import time

from psychopy import visual, sound

###################################################################################################
###################################################################################################

WAIT_TIME = 4

###################################################################################################
###################################################################################################

def main():

    import os
    os.system('pwd')

    # Set window size & color
    win_size = [800, 600]
    win_color = [-1, -1, -1]

    mywin = visual.Window(win_size, color=win_color, colorSpace='rgb', fullscr=False,
                          monitor="MON_NAME", units="norm")

    # Beginning of block message
    message = visual.TextStim(mywin, height=0.5, text='HELLO')
    message.draw()
    mywin.flip()

    time.sleep(WAIT_TIME)

    # Load sound
    mywin.flip()

    music = sound.Sound("snd/gtr-jaz-2.wav")
    music.play()
    time.sleep(1)

    # Image 1
    img = visual.ImageStim(win=mywin, image="img/curly_branch.png", units="pix")
    img.draw()
    mywin.flip()

    time.sleep(WAIT_TIME)

    # Image 2
    img = visual.ImageStim(win=mywin, image="img/random_branch.png", units="pix")
    img.draw()
    mywin.flip()

    time.sleep(WAIT_TIME)

    mywin.close()


if __name__ == "__main__":
    main()