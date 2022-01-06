from psychopy import visual, monitors

from stimuli.shapesStimuli import Trial_flickeringShapes

# ------------------------------------------------------------------------------
# -- PARAMETERS DEFINITIONS
# ------------------------------------------------------------------------------

# STIMULI
# ---------------
shapesWidth = 20
shapesStroke = 2
chkbrdTempFreq = 5
chkbrdSpFreq = 0.08
chkbrdContrast = 0.8
prestimFrames = 60
stimFrames = 60
postStimFrames = 180

# MONITOR
# ---------------
distanceCm = 50
monitorWidthCm = 56
monitorResolution = [1920, 1200]

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

mon = monitors.Monitor('TestMonitor')
mon.setDistance(distanceCm)
mon.setWidth(monitorWidthCm)

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