# Import libraries 
import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation

# Display single 3D data graph
# Take an array of point [[x,y,z]]
class SingleFrame:
    
    def  __init__(self, pointData, figsize = (10, 7), title="Title", color="red"):
        x = []
        y = []
        z = []
        for point in pointData:
            x.append(point[0])
            y.append(point[1])
            z.append(point[2])

        fig = plt.figure(figsize=figsize) 
        ax = plt.axes(projection ="3d") 
        # Creating plot 
        ax.scatter3D(x, y, z, color=color); 
        plt.title(title) 
        plt.show()

# Display a list of 3D data graph
# Take an array of point [[[x,y,z]]]
# List of frames, in which is a list of points made of [x,y,z]
# In manual mode press q to close, w (or any unbound key) to next image
class AnimatedFrames:
    
    def __init__(self, pointData, figsize = (10, 7), title="Title", automatic=False, color="red"):
        self.frames = pointData
        self.fig = plt.figure(figsize=figsize) 
        self.ax = plt.axes(projection ="3d") 
        self.color=color
        # Creating plot 
        plt.title(title) 
        if (automatic):
            anim = animation.FuncAnimation(self.fig, self.animate,frames=len(pointData), interval=350)
        else:
            self.index = 0
            self.fig.canvas.mpl_connect('key_press_event', self.update)
        plt.show()

    def draw(self, frame):
        x = []
        y = []
        z = []
        for point in frame:
            x.append(point[0])
            y.append(point[1])
            z.append(point[2])
        self.ax.scatter3D(x, y, z, color=self.color); 

    def update(self, e):
        self.ax.cla()
        self.index += 1
        if (self.index >= len(self.frames)):
            plt.close()
            return
        frame = self.frames[self.index]
        self.draw(frame)
        plt.show()
        return

    def animate(self, i):
        self.ax.cla()
        frame = self.frames[i]
        self.draw(frame)

def testSingleFrame():
    # Array of up to 15 random points
    test = np.random.randn(random.randint(1, 15), 3)
    SingleFrame(test)

def testManualFraming():
    # Up to 100 random frames
    # Array of up to 15 random points for each frame
    test = np.random.randn(random.randint(0, 100), random.randint(1, 15), 3)
    AnimatedFrames(test, automatic=False)

def testAutoFraming():
    # Up to 100 random frames
    # Array of up to 15 random points for each frame
    test = np.random.randn(random.randint(0, 100), random.randint(1, 15), 3)
    AnimatedFrames(test, automatic=True)

if __name__ == "__main__":
    testAutoFraming()
