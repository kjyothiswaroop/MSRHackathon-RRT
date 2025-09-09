import random
import math
import node
import matplotlib.pyplot as plt
class RRT:
    '''Class of the RRT Tree'''
    def __init__(self,domain,q_int,delta,vertices):
        self.d_x,self.d_y = domain
        self.q_int = q_int
        self.delta = delta
        self.vertices = vertices
        self.rrt = []
        self.dist = 0

        # Matplotlib setup
        self.fig, self.ax = plt.subplots()
        self.ax.set_xlim(0, self.d_x)
        self.ax.set_ylim(0, self.d_y)
        self.ax.set_aspect('equal')
        self.ax.set_title("RRT Growth")
        self.ax.plot(self.q_int.x, self.q_int.y, 'go', markersize=6)  # root node

    def constructRRT(self):
        '''Function to construct RRT Tree'''
        self.rrt.append(self.q_int)
        i = 1
        while i <= self.vertices:
        
            q_rand = self.randomConfiguration()
            
            q_near = self.nearestVertex(q_rand)
            q_new = self.newConfiguration(q_near,q_rand)
            if q_new :
                self.rrt.append(q_new)

                # Plot the new line from parent to q_new
                # self.ax.plot([q_near.x, q_new.x], [q_near.y, q_new.y], 'b-', alpha=0.7)
                # Plot the random sample point briefly
                rand_plot, = self.ax.plot(q_rand[0], q_rand[1], 'ro', markersize=4)
                new_plot, = self.ax.plot(q_new.x,q_new.y,'bo',markersize=5)
                self.ax.plot([q_near.x, q_new.x], [q_near.y, q_new.y], 'b-', alpha=0.7)
                plt.pause(0.1)  # small delay to animate
                rand_plot.remove()  # remove red point after plotting
                new_plot.remove()
                i = i+1

        plt.show()

            
    def randomConfiguration(self):
        '''Random point generation'''
        while True:
            q_rand = (random.randint(0,self.d_x),random.randint(0,self.d_y))
            for node in self.rrt:
                if(q_rand != (node.x,node.y)):
                    return q_rand


    def nearestVertex(self,q_rand):
        '''Nearest vertex finder'''
        min_dist = float('inf')
        q_near = None
        for entry in self.rrt :
            dist = math.dist((entry.x,entry.y),q_rand)
            if(dist < min_dist):
                min_dist = dist
                q_near = entry
        self.dist = min_dist
        return q_near

    def newConfiguration(self,q_near,q_rand):
        '''New point generator'''
        q_new = node.Node()
        if self.dist == 0:
            return 
        q_new.x  = max(0,q_near.x + (self.delta * (q_rand[0] - q_near.x))/self.dist)
        q_new.y  = max(0,q_near.y + (self.delta * (q_rand[1] - q_near.y))/self.dist)

        q_new.parent = q_near
        return q_new
