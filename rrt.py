import random
import math
import node
import matplotlib.pyplot as plt
import numpy as np
class RRT:
    '''Class of the RRT Tree'''
    def __init__(self,domain,q_int,delta,vertices,circles=None,q_goal=None):
        self.d_x,self.d_y = domain
        self.q_int = q_int
        self.delta = delta
        self.vertices = vertices
        self.rrt = []
        self.dist = 0
        self.randoms = []
        self.circles = circles
        self.q_goal = q_goal
        
    def constructRRT(self):
        '''Function to construct RRT Tree'''
        self.rrt.append(self.q_int)
        i = 1
        while i <= self.vertices:
        
            q_rand = self.randomConfiguration()
            q_near = self.nearestVertex(q_rand)
            q_new = self.newConfiguration(q_near,q_rand)

            if q_new and self.collisionFree(q_near,q_new):
                self.rrt.append(q_new)
                self.randoms.append(q_rand)

                if self.q_goal and self.collisionFree(q_new,self.q_goal):
                    self.q_goal.parent = q_new
                    self.rrt.append(self.q_goal)
                    self.randoms.append((self.q_goal.x,self.q_goal.y))
                    break

                i = i+1

            
    def randomConfiguration(self):
        '''Random point generation'''
        while True:
            q_rand = (np.random.randint(0,self.d_x),np.random.randint(0,self.d_y))
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
    
    def collisionFree(self,q_near,q_new):

        if self.circles:

            a = np.array([q_near.x,q_near.y])
            b = np.array([q_new.x,q_new.y])

            a_b = b-a #considering line segment as a vector

            for circle in self.circles:
                c = np.array([circle.c_x,circle.c_y])
                a_c = c - a

                distAB = np.linalg.norm(a_b)
                t = np.dot(a_c,a_b) / (distAB**2) #finding the projection of the point on the line segment AB

                if t < 0:
                    d = a
                elif t > 1 :
                    d = b
                else:
                    d = a + t * a_b

                dist_lineSegment = np.linalg.norm(c - d) #Finding distance between the linesegment and circle center
                if (dist_lineSegment <= circle.radius + 0.5):
                    return False
            
        return True
