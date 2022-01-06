from psychopy import core, visual
import numpy as np
import math


class Trial_flickeringShapes:

    def __init__(self,
                stimWin,
                aperture,
                shape = 'cross',
                width = 20,
                stroke = 2,
                chkbrdTempFreq = 5,
                chkbrdSpFreq = 0.08,
                chkbrdContrast = 0.8,
                prestimFrames = 60,
                stimFrames = 60,
                postStimFrames = 180,
                ):

        self.stimWindow = stimWin
        self.aperture = aperture
        self.shape = shape
        self.width = width
        self.stroke = stroke
        self.chkbrdTempFreq = chkbrdTempFreq
        self.chkbrdSpFreq = chkbrdSpFreq
        self.chkbrdContrast = chkbrdContrast
        self.prestimFrames = prestimFrames
        self.stimFrames = stimFrames
        self.postStimFrames = postStimFrames

        # Check that a supported shape is requested
        msg = "Shape must be one of 'cross','triangle', or 'circle'"
        assert shape in ['cross','triangle','circle'], msg
        
        # Calculate the proper shape coordinates
        if shape == 'cross':
            coord = self._crossCoordinates(width=width, stroke=stroke)
        elif shape == 'triangle':
            coord = self._triangleCoordinates(width=width, stroke=stroke)
        elif shape == 'circle':
            coord = self._circleCoordinates(width=width, stroke=stroke)

        # Generate the Background Checkerboard
        chkb_texture = np.array([[-1,1],[1,-1]])
        self.checkerboard = visual.GratingStim(
            self.stimWindow,
            size = [180,180],
            sf = self.chkbrdSpFreq,
            contrast = self.chkbrdContrast,
            ori = 0,
            tex = chkb_texture,
            autoDraw = False
        )

        # Generate the coordinates for restricting the stimulus visibility by
        # using both aperture and an optional shapeStim for shapes with holes
        if coord.ndim > 2:
            self.outerEdges = coord[:,:,0]
            self.innerEdges = coord[:,:,1]
        else:
            self.outerEdges = coord
            self.innerEdges = [[0,0]]

        # Shape object for filling central holes in stimuli shapes like circle 
        # or triangle
        self.outBckg = visual.ShapeStim(
            self.stimWindow,
            vertices = self.innerEdges,
            fillColor = [0,0,0],
            lineWidth=0
            )

        # Generate a clock for flickering the background checkerboard
        self.revClock = core.Clock()
        self.revClock.reset()

    def doTrial(self, sendTrigger=False):
        # Change the aperture to only render the central part of the stimulus
        self.aperture._shape.vertices = self.outerEdges
        self.aperture._needVertexUpdate = True
        self.aperture._reset()

        # PRESTIM
        for _ in range(self.prestimFrames):
            self.stimWindow.flip()
        # STIM
        for _ in range(self.prestimFrames):
            if self.revClock.getTime() >= 1/self.chkbrdTempFreq:
                self.checkerboard.phase += (0.5, 0)
                self.revClock.reset()

            self.checkerboard.draw()
            self.outBckg.draw()
            self.stimWindow.flip()
        # POSTSTIM
        for _ in range(self.postStimFrames):
            self.stimWindow.flip()

    #---------------------------------------------------------------------------
    #--- INTERNAL FUNCTIONS
    #---------------------------------------------------------------------------

    def _crossCoordinates(self, width=10, stroke=2):
        # Calculates the coordinates of the 12 vertices of a cross (square form 
        # factor since witdh = height) given its width and the stroke
        height = width
        coord = np.zeros([12,2])
        coord[0,:] = np.array([-(width/2) - stroke, height/2])
        coord[1,:] = np.array([-(width/2) + stroke, height/2])
        coord[2,:] = np.array([0, (height/2)*stroke/(width/2)])
        coord[3,:] = np.array([-coord[1,0], height/2])
        coord[4,:] = np.array([-coord[0,0], height/2])
        coord[5,:] = np.array([stroke,0])
        coord[6,:] = np.array([coord[4,0], -height/2])
        coord[7,:] = np.array([coord[3,0], -height/2])
        coord[8,:] = np.array([0, -coord[2,1]])
        coord[9,:] = np.array([coord[1,0], -height/2])
        coord[10,:] = np.array([coord[0,0], -height/2])
        coord[11,:] = np.array([-stroke,0])

        coord[[0,1,3,4],1] += stroke
        coord[[6,7,9,10],1] -= stroke
        return coord

    def _triangleCoordinates(self, width=10, stroke=2):
        # Calulates the coordinates of the 6 vertices of an equilateral triangle. 
        # The output is given in a list of 2 sets of 3 vertices: the first 3 vertices 
        # are vertices of the external triangle, while the second 3 are the 
        # vertices of the internal triangle
        aboveZero = (width/2) / math.cos(math.radians(30))

        coordInt = np.zeros([3,2])
        coordExt = np.zeros([3,2])
        coordExt[0,:] = np.array([0, aboveZero+stroke])
        coordExt[1,:] = np.array([(aboveZero+stroke)* math.cos(math.radians(30)), 
            -(aboveZero+stroke)* math.sin(math.radians(30))])
        coordExt[2,:] = np.array([-coordExt[1,0], coordExt[1,1]])
        coordInt[0,:] = np.array([0, aboveZero-stroke])
        coordInt[1,:] = np.array([(aboveZero-stroke)* math.cos(math.radians(30)),
            -(aboveZero-stroke)* math.sin(math.radians(30))])
        coordInt[2,:] = np.array([-coordInt[1,0], coordInt[1,1]])

        offsetUp = aboveZero - (width/2)
        coordExt[:,1] = coordExt[:,1] - offsetUp
        coordInt[:,1] = coordInt[:,1] - offsetUp

        coord = np.dstack((coordExt, coordInt))
        return coord

    def _circleCoordinates(self, width=10, stroke=2):
        coordExt = self._calcEquilateralVertices(100, radius = width/2 + stroke)
        coordInt = self._calcEquilateralVertices(100, radius = width/2 - stroke)

        coord = np.dstack((coordExt, coordInt))
        return coord

    def _calcEquilateralVertices(self, edges, radius=5):
        """
        Get vertices for an equilateral shape with a given number of sides, will assume radius is 0.5 (relative) but
        can be manually specified
        """
        d = np.pi * 2 / edges
        vertices = np.asarray(
            [np.asarray((np.sin(e * d), np.cos(e * d))) * radius
             for e in range(int(round(edges)))])
        return vertices


if __name__ == '__main__':

    from psychopy import monitors

    mon = monitors.Monitor('TestMonitor')
    mon.setDistance(50)
    mon.setWidth(56)

    stimWin = visual.Window(
        size = (1200,800),
        screen = 0,
        fullscr = False,
        units = 'deg',
        monitor = mon,
        allowStencil = True
    )

    mask = visual.Aperture(stimWin)

    cross = Trial_flickeringShapes(
        stimWin,
        mask,
        shape='cross',
        chkbrdSpFreq=0.3)

    circle = Trial_flickeringShapes(
        stimWin,
        mask,
        shape='circle',
        chkbrdSpFreq=0.3)
    
    triangle = Trial_flickeringShapes(
        stimWin,
        mask,
        shape='triangle',
        chkbrdSpFreq=0.3)

    for _ in range(1):
        cross.doTrial()
        triangle.doTrial()
        circle.doTrial()

