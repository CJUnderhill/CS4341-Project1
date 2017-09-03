# Daniel Kim, Spyridon Antonatos 8/31/2017

# Import functions from parser.py file for parsing the graph text files
# into networkx graph data structures
import graphParser
import sys
import operator




# networkx graph, search function -> queue
# Takes in a networkx graph and a search function and
# returns an error message if 'G' was not found, and
# returns the solution if 'G' was found
#
# A general search method to be called by all specific search methods
def General_Search(graph_data, search_method, limit = 1,ids = False):
    print("\n\n Starting " + search_method + " search method")
    # Initialize the queue with 'S' (Assume 'S' is always in the queue)
    queue = [['S']]
    # Loop
    running = True
    while (running):
        #print("\n new iteration")
        #print("general,queue: ",queue)
        print(queue)
        # If the queue is empty, 'G' was not found, so return failure message
        if (len(queue) == 0 and (not ids)):
            print("Error: Empty queue!")
            print("Goal not reached")
            sys.exit(1)
        elif (len(queue) == 0 and ids):
            print("\n going to next iterative deepening search")
            return False
            #break
        # If the queue is not empty, set the node variable to the first node
        # in the first path of the queue
        node = queue[0][0]
        # Check if a solution was found
        if node == 'G' and (not ids):
            print(queue)
            print("goal reached!")
            return queue[0]
        elif node == 'G' and ids:
            break
        # Expand the current node to it's neighboring nodes
        opened_nodes = graph_data[0].neighbors(node)
        #print("general, opened nodes: ",opened_nodes)

        heuristics = graph[1]
        #print("general, heuristics: ",heuristics)


        # Reset the queue based on the search method input
        #queue = search_method(opened_nodes, queue, heuristics)
        queue = call_search_method(search_method,opened_nodes,queue,heuristics,limit)
    return queue


#determine which search method to call
def call_search_method(search_method,neighbors,queue,heuristics,limit):
    if search_method == "depthFirst":
        return search_methods[1](neighbors,queue)
    
    elif search_method == "breadthFirst":
        return search_methods[2](neighbors,queue)
    
    elif search_method == "depthLimited":
        return search_methods[3](neighbors,queue,limit)
    
    elif search_method == "iterativeDeepening":
        return search_methods[4](neighbors,queue)
    
    elif search_method == "uniformCost":
        return search_methods[5](neighbors,queue)
    
    elif search_method == "greedySearch":
        return search_methods[6](neighbors,queue,heuristics)
    
    elif search_method == "aStar":
        return search_methods[7](neighbors,queue)
    
    elif search_method == "hillClimbing":
        return search_methods[8](neighbors,queue,heuristics)
    
    elif search_method == "beamSearch":
        return search_methods[9](neighbors,queue)
    
    else:
        print("unknown search method")
        return []
    

# Depth 1st search method
def depthFirst(neighbors, queue):
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
def breadthFirst(neighbors, queue):
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

#similar to depthFirst
def depthLimited(neighbors, queue,limit):
    #print("QUEUE: ",queue)
    print("limit: ",limit)
    # enqueue to front
    newQueue = []
    neighbors.sort()
    for n in neighbors:
        if n in queue[0]:
            continue
        tempQueue = []
        tempQueue.append(n)
        tempQueue.extend(queue[0])
        if(len(tempQueue) <= limit):
            newQueue.append(tempQueue)
    newQueue.extend(queue[1:])
    return newQueue

#similar to depthLimited
def iterativeDeepening(neighbors,queue):
    #return search_methods[3](neighbors,queue,limit)
    running = True
    new_limit2 = 1
    while(running):
        val = General_Search(graph, "depthLimited",limit = new_limit2,ids = True)
        if not val:
            new_limit2+=1
        else:
            running = False
            return val
        
def uniformCost(neighbors,queue):
    print(1)
def aStar(neighbors,queue):
    print(1)

#implemented the version with no backtracking as requested by the instructions
def hillClimbing(neighbors,queue,heuristics):
    # enqueue to front
    newQueue = []
    neighbors.sort()
    neighborsVal = {}
    for n in neighbors:
        if n == 'G':
            neighborsVal[n] = 0
        else:
            neighborsVal[n] = float(heuristics[n])
        if n in queue[0]:
            continue
    sorted_neighbors = sorted(neighborsVal.items(), key=operator.itemgetter(1))
    #print("so nei : ",sorted_neighbors)
    tempQueue = []
    tempQueue.append(sorted_neighbors[0][0])
    tempQueue.extend(queue[0])
    newQueue.append(tempQueue)
    return newQueue

def beamSearch(neighbors,queue):
    print(1)

    

#method dictionary?

search_methods = {0:General_Search,
                  1:depthFirst,
                  2:breadthFirst,
                  3:depthLimited,
                  4:iterativeDeepening,
                  5:uniformCost,
                  6:greedySearch,
                  7:aStar,
                  8:hillClimbing,
                  9:beamSearch
                  }

# Testing general search method
graph = graphParser.build_graph('graph.txt')
#General_Search(graph, "depthFirst")
#General_Search(graph, "breadthFirst")
#General_Search(graph, "greedySearch")
#General_Search(graph, "depthLimited",limit = 3)
#General_Search(graph, "iterativeDeepening")
General_Search(graph, "hillClimbing")


