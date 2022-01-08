from time import sleep

def f():
    for _ in range(10):
        sleep(.5)
        print('A')




if __name__ == '__main__':

    from psychopy import visual
    from psychopy import monitors, parallel
    from multiprocessing import Process
    from stimuli.shapesStimuli import Trial_flickeringShapes


    stimWin = visual.Window(
        size = (1920,1080),
        screen = 0,
        fullscr = True,
        units = 'deg',
        monitor = 'TestMonitor',
        allowStencil = True
    )

    mask = visual.Aperture(stimWin)

    cross = Trial_flickeringShapes(
        stimWin,
        mask,
        )
    p = Process(target=f)

    p.start()
    for _ in range(2):
        cross.doTrial()







