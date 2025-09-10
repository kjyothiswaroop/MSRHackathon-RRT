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
        self.randoms = []
        
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
                self.randoms.append(q_rand)
                i = i+1

            
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
