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
    newQueue = []

    # Add remaining paths to front of queue
    newQueue.extend(queue[1:])

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
# @return newQueue      The updated queue of explored paths processed by the search algorithm
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
    newQueue = []

    # Add remaining paths to front of queue
    newQueue.extend(queue[1:])

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
    # Take shortest straight-line route every time
    newQueue = queue[1:]

    # For each neighboring node
    for n in neighbors:
        tempQueue = []
        tempDict = {}
        if n in queue[0]['path']:   # Skip cycles
            continue

        print("Queue: " + str(newQueue))

        # Construct queue entry
        tempQueue.insert(0, n)
        tempQueue.extend(queue[0]['path'])
        print("Queue Entry: " + str(tempQueue))

        index = 0

        tempDict['path'] = tempQueue
        if n == 'G':
            tempDict['h'] =  0.0
        else:
            tempDict['h'] = float(graph_data[1][n])

        # If newQueue is empty, simply add to front
        if not newQueue:
            newQueue.append(tempDict)
            print("tempQueue: " + str(tempQueue))
            print("tempDict: " + str(tempDict))
        else:
            for m in newQueue:
                if "G" in tempDict['path']:
                    continue
                # Review heuristic value
                if float(graph_data[1][n]) < float(m['h']):
                    print(str(n) + " : " + str(graph_data[1][n]))
                    print(str(m['h']) + " : " + str(m['h']))
                    #print(m)
                    break
                else: # Increase index of location in queue if heuristic value greater than checked value
                    index += 1
                    continue

            # Insert queue entry into queue
            newQueue.insert(index, tempDict)
        print("New Queue: " + str(index) + " " + str(newQueue) + "\n")

    return newQueue

# Helper for uniform-cost search
# Sorts by least cost so far
def leastCost(e):
    return float(e['h'])


# This function executes the A* Search algorithm on a provided graph
# @param neighbors      A list of the expanded node's immediate neighbors
# @param queue          The current queue of explored paths
# @param graph_data     Pre-parsed graph following the NetworkX structure
# @param params         Additional parameters
# @return newQueue      The updated queue of explored paths processed by the search algorithm
#
def aStarSearch(neighbors, queue, graph_data, params):
    #print(queue)
    # Take shortest straight-line route every time
    newQueue = queue[1:]

    # For each neighboring node
    for n in neighbors:
        tempQueue = []
        tempDict = {}
        if n in queue[0]['path']:   # Skip cycles
            continue

        #print("Queue: " + str(newQueue))

        # Construct queue entry
        tempQueue.insert(0, n)
        tempQueue.extend(queue[0]['path'])
        #print("Queue Entry: " + str(tempQueue))

        index = 0

        tempDict['path'] = tempQueue
        prevH = float(graph_data[1][queue[0]['path'][0]])
        prevVal = float(queue[0]['h'])
        prevCost = prevVal - prevH
        currentWeight = float(graph_data[0][n][queue[0]['path'][0]]['weight'])
        if n == 'G':
            currentH = 0
        else:
            currentH = float(graph_data[1][n])
        print(prevVal)
        tempDict['h'] = prevCost + currentH + currentWeight
        skip = False
        
        # If newQueue is empty
        if not newQueue:
            newQueue.append(tempDict)
            #print("tempQueue: " + str(tempQueue))
            #print("tempDict: " + str(tempDict))
        else:
            for m in newQueue:
                if "G" in tempDict['path']:
                    continue
                # Check for common goal
                if n == m['path'][0]:
                    print(m['h'])
                    print(tempDict['h'])
                    # Take least cost so far
                    if m['h'] < tempDict['h']:
                        skip = True

            # Insert queue entry into queue
            if not skip:
                newQueue.append(tempDict)
                newQueue.sort(key=leastCost)
        #print("New Queue: " + str(index) + " " + str(newQueue) + "\n")
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
    neighbors.sort()
    neighborsVal = {}
    for n in neighbors:
        if n == 'G':
            neighborsVal[n] = 0
        else:
            neighborsVal[n] = float(graph_data[1][n])
        if n in queue[0]['path']:
            continue
    sorted_neighbors = sorted(neighborsVal.items(), key=operator.itemgetter(1))
    tempQueue = []
    tempQueue.append(sorted_neighbors[0][0])
    tempQueue.extend(queue[0]['path'])
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
    uniqueChild = len(neighbors)
    if len(queue) == 1:
        queue[0]['h'] = 11
    newQ = []
    newQ.extend(queue[1:])
    for n in neighbors:
        if n in queue[0]['path']:
            uniqueChild -= 1
            continue
        tempDict = {}
        tempPath = []
        tempPath.append(n)
        tempPath.extend(queue[0]['path'])
        tempDict['path'] = tempPath
        if n == 'G':
            heuristic = 0
        else:
            heuristic = graph_data[1][n]
        tempDict['h'] = heuristic
        newQ.append(tempDict)
    # sort lexographically
    cutoff = len(newQ) - uniqueChild
    #print(cutoff)
    #print('before: ',newQ)
    beforeCutList = []
    if cutoff > 0:
        #print('here')
        beforeCutList = newQ[:cutoff]
    #print('notsorted: ', beforeCutList)
    #print('sorted: ',sorted(newQ[cutoff:], key=lex))
    newQ = beforeCutList + sorted(newQ[cutoff:], key=lex)
    #print('after: ',newQ)
    pastlen = 0
    if len(queue) > 2:
        for i in newQ:
            ilen = len(i['path'])
            if ilen == pastlen:
                newQ.sort(key=leastCost)
                #print('LeastCost: ', newQ)
                newQ = newQ[:2]
                #print("Next level")
                #print('after next level: ', newQ)
                return newQ
            pastlen = ilen
    return newQ

General_Search(graphParser.build_graph('graph.txt'), aStarSearch)
