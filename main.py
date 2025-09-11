#!/usr/bin/env python3
import rrt
import plot
import node
import numpy as np
import circle

def main():
    np.random.seed(10)
    #Take user input for number of vertices
    print("Input number of Vertices:")
    r = int(input())

    circles = [circle.Circle((10,20),3),circle.Circle((40,60),15),circle.Circle((80,40),10)]

    #Instaniate RRT Object and construct the tree
    init_node = node.Node(10,90)
    goal_node = node.Node(99,10)
    rrtObj = rrt.RRT((100,100),init_node,1,r,circles,goal_node)
    rrtTree = rrtObj.constructRRT()

    #Plot the Tree and save a gif to images folder
    pltObj = plot.Plotter(rrtObj,(100,100),circles)
    pltObj.plotRRT()

if __name__ == "__main__":
    main()
