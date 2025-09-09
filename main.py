#!/usr/bin/env python3
import rrt
import plot
import node

def main():
    #Take user input for number of vertices
    print("Input number of Vertices:")
    r = int(input())

    #Instaniate RRT Object and construct the tree
    init_node = node.Node(50,50)
    rrtObj = rrt.RRT((100,100),init_node,1,r)
    rrtTree = rrtObj.constructRRT()

    #Plot the Tree
    # pltObj = plot.Plotter(rrtObj,(100,100))
    # pltObj.plotRRT()

if __name__ == "__main__":
    main()
