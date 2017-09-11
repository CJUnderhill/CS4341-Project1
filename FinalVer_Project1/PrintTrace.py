# Project 1 | CS4341 | A-Term (Fall 2017) | Prof. Carolina Ruiz | Worcester Polytechnic Institute
#
# This file contains a method to print the trace of the queue as
#   a search method is being performed.
#
# @author Chad Underhill, Daniel Kim, Spiros Antonatos
# @since 9/11/2017

# This function prints the trace of a search algorithm on a graph,
#   including the expanded nodes and the state of the queue at each step.
# @param output     Array of the states of a queue from a search method
# @param informed   True if the search performed was informed, false otherwise
#
def printTrace(output, informed):
    print()
    print("     Expanded   Queue")
    for queue in output:
        # If solution was not found, print error
        if queue == []:
            print("\tfailure to find path between S and G")
            break
        # Print expanded
        expanded = queue[0]['path'][0]
        line = "\t" + expanded + "\t["
        # Print queue
        for path in queue:
            pathstr = ""
            if informed:
                pathstr += str(path['h'])
            pathstr += "<"
            for node in path['path']:
                pathstr += (node + ",")
            pathstr = pathstr[:len(pathstr)-1]
            pathstr += ">"
            line += (pathstr + " ")
        line = line[:len(line)-1]
        line += "]"
        print(line)
        # If solution was found, print success
        if expanded == 'G':
            print("\tgoal reached!")
            break
    print()
