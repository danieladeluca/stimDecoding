
def triggerControl(pPort):
    clk = core.Clock()
    clk.reset()
    framesAcquired = 0
    while framesAcquired < 60:
        if clk.getTime() >= .1:
            pPort.setData(int("00000001",2))
            sleep(.001)
            pPort.setData(int("00000000",2))
            framesAcquired += 1
            clk.reset()

if __name__ == '__main__':
    from psychopy import visual, monitors, parallel, core
    from stimuli.shapesStimuli import Trial_flickeringShapes
    import socket
    from threading import Thread
    from time import sleep

    # ------------------------------------------------------------------------------
    # -- PARAMETERS DEFINITIONS
    # ------------------------------------------------------------------------------

    # STIMULI
    # ---------------
    shapesWidth = 40
    shapesStroke = 4
    chkbrdTempFreq = 5
    chkbrdSpFreq = 0.08
    chkbrdContrast = 0.8
    prestimFrames = 60
    stimFrames = 60
    postStimFrames = 240

    # MONITOR
    # ---------------
    distanceCm = 20
    monitorWidthCm = 52
    monitorResolution = [1920, 1080]

    # TPC/IP Communication
    # ---------------
    TCP_ip = '192.168.1.2'      # IP address of the recording machine
    TCP_port = 40000            # 
    TCP_buffSize = 4096

    # ------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------

    mon = monitors.Monitor('TestMonitor')
    mon.setDistance(distanceCm)
    mon.setWidth(monitorWidthCm)

    pPort = parallel.ParallelPort(address = '0xD010')




    # Main stimulation window
    stimWin = visual.Window(
        size = monitorResolution,
        screen = 0,
        fullscr = True,
        units = 'deg',
        monitor = mon,
        allowStencil = True
    )

    # Aperture object
    mask = visual.Aperture(stimWin)

    # Cross stimulus object
    cross = Trial_flickeringShapes(
        stimWin,
        mask,
        pPort = pPort,
        shape='cross',
        width = shapesWidth,
        stroke = shapesStroke,
        chkbrdTempFreq = chkbrdTempFreq,
        chkbrdSpFreq = chkbrdSpFreq,
        chkbrdContrast = chkbrdContrast,
        prestimFrames = prestimFrames,
        stimFrames = stimFrames,
        postStimFrames = postStimFrames
        )
    # Circle stimulus object
    circle = Trial_flickeringShapes(
        stimWin,
        mask,
        pPort = pPort,
        shape='circle',
        width = shapesWidth,
        stroke = shapesStroke,
        chkbrdTempFreq = chkbrdTempFreq,
        chkbrdSpFreq = chkbrdSpFreq,
        chkbrdContrast = chkbrdContrast,
        prestimFrames = prestimFrames,
        stimFrames = stimFrames,
        postStimFrames = postStimFrames
        )
    # Triangle stimulus object
    triangle = Trial_flickeringShapes(
        stimWin,
        mask,
        pPort = pPort,
        shape='triangle',
        width = shapesWidth,
        stroke = shapesStroke,
        chkbrdTempFreq = chkbrdTempFreq,
        chkbrdSpFreq = chkbrdSpFreq,
        chkbrdContrast = chkbrdContrast,
        prestimFrames = prestimFrames,
        stimFrames = stimFrames,
        postStimFrames = postStimFrames
        )

    tcpObj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpObj.connect((TCP_ip, TCP_port))
    tcpObj.settimeout(600)

    p = Thread(target=triggerControl, args=(pPort,))


    while True:
        msg = tcpObj.recv(TCP_buffSize)
        msg = msg.decode('utf8')
        print(f'TRIAL: {msg}')

        if msg == 'cross':
            p.start()
            cross.doTrial()
        elif msg == 'circle':
            p.start()
            circle.doTrial()
        elif msg == 'triangle':
            p.start()
            triangle.doTrial()
        elif msg == 'stop':
            break