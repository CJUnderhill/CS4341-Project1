# Daniel Kim, Spyridon Antonatos 8/31/2017

# Import functions from parser.py file for parsing the graph text files
# into networkx graph data structures
import graphParser
import sys

# networkx graph, search function -> queue
# Takes in a networkx graph and a search function and
# returns an error message if 'G' was not found, and
# returns the solution if 'G' was found
#
# A general search method to be called by all specific search methods
def General_Search(graph, heuristics, search_method):
    # Initialize the queue with 'S' (Assume 'S' is always in the queue)
    queue = [['S']]
    # Loop
    while (True):
        # If the queue is empty, 'G' was not found, so return failure message
        if (len(queue) == 0):
            print("Error: Empty queue!")
            sys.exit(1)
        # If the queue is not empty, set the node variable to the first node
        # in the first path of the queue
        node = queue[0][0]
        # Check if a solution was found
        if node == 'G':
            print(queue)
            print("goal reached!")
            return queue[0]
        # Expand the current node to it's neighboring nodes
        opened_nodes = graph.neighbors(node)
        # Reset the queue based on the search method input
        queue = search_method(opened_nodes, queue, heuristics)

# Depth 1st search method
def depthFirst(neighbors, queue, heuristics):
    print(queue)
    # enqueue to front
    newQueue = []
    neighbors.sort()
    for n in neighbors:
        if n in queue[0]:
            continue
        tempQueue = []
        tempQueue.append(n)
        tempQueue.extend(queue[0])
        newQueue.append(tempQueue)
    newQueue.extend(queue[1:])
    return newQueue

# Breadth 1st search method
def breadthFirst(neighbors, queue, heuristics):
    # enqueue to end
    print(queue)
    newQueue = []
    neighbors.sort()
    newQueue.extend(queue[1:])
    for n in neighbors:
        if n in queue[0]:
            continue
        tempQueue = []
        tempQueue.append(n)
        tempQueue.extend(queue[0])
        newQueue.append(tempQueue)
    return newQueue

def greedySearch(neighbors, queue, heuristics):
    #
    print(queue)
    newQueue = []
    neighbors.sort()
    print(neighbors)

    lowest = ("", -1)

    for n in neighbors:
        if n in queue[0]:
            continue
        print(lowest[1])
        if float(heuristics[n]) < lowest[1] or lowest[1] < 0:
            lowest = (n, float(heuristics[n]))

    print (lowest)
    return newQueue

# Testing general search method
graph = graphParser.build_graph('graph.txt')
General_Search(graph[0], graph[1], depthFirst)
General_Search(graph[0], graph[1], breadthFirst)
#General_Search(graph[0], graph[1], greedySearch)
