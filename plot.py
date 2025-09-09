import matplotlib.pyplot as plt
import matplotlib.animation as anim

class Plotter:

    def __init__(self,rrt,domain):
        self.rrt = rrt.rrt
        self.vertices = rrt.vertices
        self.d_x,self.d_y = domain
        self.fig , self.ax = plt.subplots()
        self.lines = []
        self.frames = []


    def plotRRT(self,interval=200):

        self.ax.set_xlim(0,self.d_x)
        self.ax.set_ylim(0,self.d_y)
        self.ax.set_aspect('equal')
        self.ax.set_title("RRT Representation") 

        self.ax.plot(self.rrt[0].x,self.rrt[0].y,'ro',markersize=5)
        self.makeFrames()

        ani = anim.FuncAnimation(self.fig,self.drawLine,frames=len(self.frames),interval=interval)
        plt.show()
       
        

    def makeFrames(self):
        self.frames = []
        '''Generate each frame to be plotted'''
        for node in self.rrt:
            if node.parent is not None:
                self.frames.append(((node.parent.x,node.x),(node.parent.y,node.y)))
        return self.frames
    
    def drawLine(self,frame):
        x_vals , y_vals = self.frames[frame]
        line, = self.ax.plot(x_vals,y_vals,'b-',alpha=0.6)
        self.lines.append(line)
        return line,

