# Project 1 | CS4341 | A-Term (Fall 2017) | Prof. Carolina Ruiz | Worcester Polytechnic Institute
#
# This program uses a number of search algorithms to process an input graph data structure.
#
# @author Chad Underhill, Daniel Kim, Spiros Antonatos
# @since 9/5/2017


import graphParser


# This function provides a general search structure for both informed and
#   uninformed search algorithms, using a "queue" as specified in the 
#   project instructions.
# @param graph_data     Pre-parsed graph following the NetworkX structure
# @param search_method  The search algorithm to follow
# @param params         Additional parameters
# @return queue         The queue of explored paths processed by the search algorithm
#
def General_Search(graph_data, search_method, params = {}):
    # Make queue and initialize to start node
    queue = [{'path':['S'], 'h':11}]

    while(True):
        if len(queue) == 0:
            return []

        # Set current node to front of queue
        node = queue[0]['path'][0]

        # Return queue if goal reached
        if node == 'G':
            return queue

        # Determine nodes to expand from current node
        opened_nodes = graph_data[0].neighbors(node).sort()

        # Execute search algorithm and update the queue
        queue = search_method(opened_nodes, queue, graph_data, params)


# Helper for uniform-cost search; sorts by least cost so far
# @param e  Graph node
# @returns  Heuristic value of given node
#
def leastCost(e):
    return float(e['h'])


# This function models the sorting functionality outlined in the project document
# @param newQueue       The queue being updated
# @param tempDict       The current path being updated
# @return newQueue      The updated queue of explored paths, properly sorted
#
def sortFunction(newQueue, tempDict):
    # For each remaining item in our newQueue
    for m in newQueue:

        # Skip if we reach the goal node
        if "G" in tempDict['path']:
            continue

        # If two paths have different values, then one with lowest value comes first
        if float(tempDict['h']) not float(m['h']):
            
            if float(tempDict['h']) < float(m['h']):
                break
            else:
                break

        else: # Two paths have same value

            # If two paths end at different nodes, put in alphabetical order
            if n not m['path'][0]:

                if n < m['path'][0]:
                    break
                else:
                    break

            else: # The two paths end at the same node

                # If two paths are of different length, put shortest first
                if len(tempDict['path']) not len(m['path']):

                    if len(tempDict['path']) < len(m['path']):
                        break
                    else:
                        break

                else: # Two paths end at the same node and are of same length

                    # Sort lexicographically
                    break

    # Insert queue entry into queue
    newQueue.insert(index, tempDict)
    return newQueue


# This function executes the Depth-First Search algorithm on a provided graph
# @param neighbors      A list of the expanded node's immediate neighbors
# @param queue          The current queue of explored paths
# @param graph_data     Pre-parsed graph following the NetworkX structure
# @param params         Additional parameters
# @return newQueue      The updated queue of explored paths processed by the search algorithm
#
def depthFirst(neighbors, queue, graph_data, params):
    newQueue = []

    for n in neighbors:
        # Check if neighbor has already been visited
        if n in queue[0]['path']:
            continue

        # Add node to path list
        tempQueue = []
        tempQueue.append(n)
        tempQueue.extend(queue[0]['path'])

        # Add path to front of queue of explored paths
        newQueue.append({'path':tempQueue, 'h':0})

    # Add remaining paths to end of queue
    newQueue.extend(queue[1:])

    return newQueue


# This function executes the Breadth-First Search algorithm on a provided graph
# @param neighbors      A list of the expanded node's immediate neighbors
# @param queue          The current queue of explored paths
# @param graph_data     Pre-parsed graph following the NetworkX structure
# @param params         Additional parameters
# @return newQueue      The updated queue of explored paths processed by the search algorithm
#
def breadthFirst(neighbors, queue, graph_data, params):
    # Add remaining paths to front of queue
    newQueue = queue[1:]

    for n in neighbors:
        # Check if neighbor has already been visited
        if n in queue[0]['path']:
            continue

        # Add node to path list
        tempQueue = []
        tempQueue.append(n)
        tempQueue.extend(queue[0]['path'])

        # Add path to front of queue of explored paths
        newQueue.append({'path':tempQueue, 'h':0})

    return newQueue


# This function executes the Depth-Limited Search algorithm on a provided graph
# @param neighbors      A list of the expanded node's immediate neighbors
# @param queue          The current queue of explored paths
# @param graph_data     Pre-parsed graph following the NetworkX structure
# @param params         Additional parameters
# @return newQueue      The updated queue of explored paths processed by the search algorithm
#
def depthLimited(neighbors, queue, graph_data, params):
    newQueue = []

    for n in neighbors:
        # Check if neighbor has already been visited
        if n in queue[0]['path']:
            continue

        # Add node to path list
        tempQueue = []
        tempQueue.append(n)
        tempQueue.extend(queue[0]['path'])

        # Only append to queue of explored paths if list length is under the depth limit
        if len(tempQueue)-1 <= params['limit']:
            newQueue.append({'path':tempQueue, 'h':0})

    # Add remaining paths to end of queue
    newQueue.extend(queue[1:])

    print(newQueue)
    return newQueue


# This function executes the Iterative Deepening Search algorithm on a provided graph
# @param neighbors      A list of the expanded node's immediate neighbors
# @param queue          The current queue of explored paths
# @param graph_data     Pre-parsed graph following the NetworkX structure
# @param params         Additional parameters
# @return tempQueue      The updated queue of explored paths processed by the search algorithm
#
def iterativeDeepening(neighbors, queue, graph_data, params):
    newQueue = []
    limit = 1       # Default limit

    while(True):
        # Iteratively call Depth-Limited Search on queue
        tempQueue = General_Search(graph_data, depthLimited, {'limit': limit})

        # Increase limit if goal not found
        if not tempQueue:
            limit += 1
            newQueue.append(tempQueue)
            print(newQueue)
        else:
            return tempQueue


# This function executes the Uniform Cost Search algorithm on a provided graph
# @param neighbors      A list of the expanded node's immediate neighbors
# @param queue          The current queue of explored paths
# @param graph_data     Pre-parsed graph following the NetworkX structure
# @return newQueue      The updated queue of explored paths processed by the search algorithm
#
def uniformCost(neighbors, queue, graph_data):
    # Add remaining paths to front of queue
    newQueue = queue[1:]

    # Note: neighbors.sort() was called in general function, so this may not work properly???
    for n in neighbors:
        # Check if neighbor has already been visited
        if n in queue[0]['path']:
            continue

        # Add node to path list
        tempPath = []
        tempPath.append(n)
        tempPath.extend(queue[0]['path'])

        # Add path list to queue dictionary structure
        tempDict = {}
        tempDict['path'] = tempPath

        # Determine path cost between current node and neighbor node
        currentNode = queue[0]['path'][0]
        cost = float(graph_data[0][currentNode][n]['weight'])

        # Set cost of explored paths in queue dictionary structure
        if len(queue[0]) == 1:
            tempDict['h'] = cost
        else:
            tempDict['h'] = queue[0]['h'] + cost

        # Add path dictionary entry to queue
        newQueue.append(tempDict)
        newQueue.sort(key=leastCost)

    return newQueue


# This function executes the Greedy Search algorithm on a provided graph
# @param neighbors      A list of the expanded node's immediate neighbors
# @param queue          The current queue of explored paths
# @param graph_data     Pre-parsed graph following the NetworkX structure
# @param params         Additional parameters
# @return newQueue      The updated queue of explored paths processed by the search algorithm
#
def greedySearch(neighbors, queue, graph_data, params):
    # Add remaining paths to front of queue
    newQueue = queue[1:]

    # For each neighboring node
    for n in neighbors:
        # Check if neighbor has already been visited
        if n in queue[0]['path']:
            continue

        # Add node to path list
        tempQueue = []
        tempQueue.insert(0, n)
        tempQueue.extend(queue[0]['path'])

        # Add path list to queue dictionary structure
        tempDict = {}
        tempDict['path'] = tempQueue
        if n == 'G':    # Set heuristic when we reach the goal node
            tempDict['h'] =  0.0
        else:
            tempDict['h'] = float(graph_data[1][n])

        # If newQueue is empty, simply add to front
        if not newQueue:
            newQueue.append(tempDict)
        else:
            index = 0
            # For each remaining item in our newQueue
            for m in newQueue:
                # Skip if we reach the goal node
                if "G" in tempDict['path']:
                    continue

                # Exit loop and add to queue in current position if heuristic value less than current value in queue
                if float(graph_data[1][n]) < float(m['h']):
                    break
                else: # Increase index of location in queue if heuristic value greater than checked value
                    index += 1
                    continue

            # Insert queue entry into queue
            newQueue.insert(index, tempDict)

    print(newQueue)
    return newQueue


# This function executes the A* Search algorithm on a provided graph
# @param neighbors      A list of the expanded node's immediate neighbors
# @param queue          The current queue of explored paths
# @param graph_data     Pre-parsed graph following the NetworkX structure
# @param params         Additional parameters
# @return newQueue      The updated queue of explored paths processed by the search algorithm
#
def aStarSearch(neighbors, queue, graph_data, params):
    # Add remaining paths to front of queue
    newQueue = queue[1:]

    # For each neighboring node
    for n in neighbors:
        # Check if neighbor has already been visited
        if n in queue[0]['path']:
            continue

        # Add node to path list
        tempQueue = []
        tempQueue.insert(0, n)
        tempQueue.extend(queue[0]['path'])

        # Determine the current cost (and current f-value) of neighboring node
        prevF = float(graph_data[1][queue[0]['path'][0]])
        prevVal = float(queue[0]['h'])
        prevCost = prevVal - prevF
        currentCost = float(graph_data[0][n][queue[0]['path'][0]]['weight'])
        if n == 'G':    # Set F-val when we reach goal node
            currentF = 0
        else:
            currentF = float(graph_data[1][n])

        # Add path list to queue dictionary structure
        tempDict = {}
        tempDict['path'] = tempQueue
        tempDict['h'] = prevCost + currentF + currentCost
        
        # If newQueue is empty
        if not newQueue:
            newQueue.append(tempDict)
        else:
            skip = False
            for m in newQueue:

                # Skip if we reach the goal node
                if "G" in tempDict['path']:
                    continue

                # Check for common path
                if n == m['path'][0]:

                    # Take path with the least cost so far
                    if m['h'] < tempDict['h']:
                        skip = True

            # Insert queue entry into queue
            if not skip:
                newQueue.append(tempDict)
                newQueue.sort(key=leastCost)

    print(newQueue)
    return newQueue


# This function executes the Hill-Climbing Search algorithm on a provided graph
# @param neighbors      A list of the expanded node's immediate neighbors
# @param queue          The current queue of explored paths
# @param graph_data     Pre-parsed graph following the NetworkX structure
# @param params         Additional parameters
# @return newQueue      The updated queue of explored paths processed by the search algorithm
#
def hillClimbing(neighbors, queue, graph_data, params):
    newQueue = []
    neighborsVal = {}

    for n in neighbors:
        # Set F-value when we reach goal node
        if n == 'G':
            neighborsVal[n] = 0
        else:   # Set F-value to the heuristic
            neighborsVal[n] = float(graph_data[1][n])

        # Check if neighbor has already been visited
        if n in queue[0]['path']:
            continue

    # Sort neighbors by value
    sorted_neighbors = sorted(neighborsVal.items(), key=operator.itemgetter(1))

    # Add node to path list
    tempQueue = []
    tempQueue.append(sorted_neighbors[0][0])
    tempQueue.extend(queue[0]['path'])

    # Insert queue entry into queue
    newQueue.append({'path':tempQueue, 'h':0})
    
    print(newQueue)
    return newQueue


# This function executes the Beam Search algorithm on a provided graph
# @param neighbors      A list of the expanded node's immediate neighbors
# @param queue          The current queue of explored paths
# @param graph_data     Pre-parsed graph following the NetworkX structure
# @return newQueue      The updated queue of explored paths processed by the search algorithm
#
def beam(neighbors, queue, graph_data):
    #
    uniqueChild = len(neighbors)

    # Set initial queue heuristic to that of the starting node
    # TODO: Do we even need this anymore?
    if len(queue) == 1:
        queue[0]['h'] = 11

    # Add remaining paths to front of queue
    newQueue = queue[1:]
    for n in neighbors:
        #
        if n in queue[0]['path']:
            uniqueChild -= 1
            continue
        
        # Add node to path list
        tempPath = []
        tempPath.append(n)
        tempPath.extend(queue[0]['path'])

        # Set heuristic when we reach the goal node
        if n == 'G':
            heuristic = 0
        else:   # Pull heuristic from graph data
            heuristic = graph_data[1][n]

        # Add path list to queue dictionary structure
        tempDict = {}
        tempDict['path'] = tempPath
        tempDict['h'] = heuristic
        newQueue.append(tempDict)

    # sort lexographically
    cutoff = len(newQueue) - uniqueChild

    #
    beforeCutList = []
    if cutoff > 0:
        beforeCutList = newQueue[:cutoff]

    #
    newQueue = beforeCutList + sorted(newQueue[cutoff:], key=lex)
    
    #
    pastlen = 0
    if len(queue) > 2:
        for i in newQueue:
            ilen = len(i['path'])

            #
            if ilen == pastlen:
                newQueue.sort(key=leastCost)
                newQueue = newQueue[:2]
                return newQueue
            pastlen = ilen

    return newQueue


# Main function stuff
General_Search(graphParser.build_graph('graph.txt'), aStarSearch)
