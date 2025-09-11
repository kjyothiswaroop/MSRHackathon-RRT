import matplotlib.pyplot as plt
import matplotlib.animation as anim
import imageio
import numpy as np
import matplotlib.patches as patch

class Plotter:

    def __init__(self,rrt,domain,circles=None):
        self.rrt = rrt.rrt
        self.vertices = rrt.vertices
        self.d_x,self.d_y = domain
        self.fig , self.ax = plt.subplots()
        self.lines = []
        self.frames = []
        self.randoms = rrt.randoms
        self.circles = circles


    def plotRRT(self):
        '''Takes the full RRT and generates the plot, additionally a gif is also saved'''

        self.ax.set_xlim(0,self.d_x)
        self.ax.set_ylim(0,self.d_y)
        self.ax.set_aspect('equal') 
        self.ax.set_title(f"RRT Generation {self.vertices} step")

        self.ax.plot(self.rrt[0].x,self.rrt[0].y,'go',markersize=5)
        self.rrt.pop(0)
        frames = []

        if self.circles:
            for circle in self.circles:
                self.ax.add_patch(patch.Circle((circle.c_x,circle.c_y),circle.radius,color='blue',clip_on=False))

        for i,node in enumerate(self.rrt):
            self.ax.set_xlabel(f"Step : {i+1}")
            if node.parent is not None:
                if self.randoms:
                    rand_plot, = self.ax.plot(self.randoms[i][0],self.randoms[i][1],'ro', markersize=4)
                self.ax.plot(node.x,node.y,'bo',markersize=2)
                self.ax.plot([node.parent.x,node.x],[node.parent.y,node.y],'b-',alpha=0.7)

                plt.pause(0.1)

                self.fig.canvas.draw()
                frame = np.array(self.fig.canvas.renderer.buffer_rgba())
                frames.append(frame)

                rand_plot.remove()


        gif_name = f"images/RRT{self.vertices}.gif"
        imageio.mimsave(gif_name, frames, fps=5)
        print(f"Saved GIF as {gif_name}")
        plt.show()