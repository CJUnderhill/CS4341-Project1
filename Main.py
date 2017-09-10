from Algorithms2 import *
import graphParser

def DepthFirstSearch(graph_data):
    Q, out = General_Search(graph_data, depthFirst, {'h':0})
    return Q, out

# Print
def printQueue(output, informed):
    print()
    print("     Expanded   Queue")
    for queue in output:
        if queue == []:
            print("\tfailure to find path between S and G")
            break
        if queue == 'goal reached!':
            print("\t" + queue)
            break
        # print expanded
        expanded = queue[0]['path'][0]
        # print rest of line
        line = "\t" + expanded + "\t["
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
    print()

# Main
def main(file):
    print("Running search on " + file)
    graph_data = graphParser.build_graph(file)

    print("Depth 1st search")
    Q, out = DepthFirstSearch(graph_data)
    printQueue(out, False)

    print("Breadth 1st search")
    Q, out = General_Search(graph_data, breadthFirst, {'h':0})
    printQueue(out, False)

    print("Depth-limited search (limit = 2)")
    Q, out = General_Search(graph_data, depthLimited, {'h':0, "limit":2})
    printQueue(out, False)

    print("Iterative deepening search")
    Q, out = General_Search(graph_data, iterativeDeepening, {'h':0})
    printQueue(out, False)
    # FIX THIS

    print("Uniform Search (Branch-and-bound)")
    Q, out = General_Search(graph_data, uniformCost, {'h':0})
    printQueue(out, True)
    # sort lexo

    print("Greedy search")
    Q, out = General_Search(graph_data, greedySearch, {'h':11})
    printQueue(out, True)

    print("A*")
    Q, out = General_Search(graph_data, aStarSearch, {'h':11})
    printQueue(out, True)

    print("Hill climbing search (No backtracking)")
    Q, out = General_Search(graph_data, hillClimbing, {'h':11})
    printQueue(out, True)

    print("Beam search (w = 2)")
    Q, out = General_Search(graph_data, beam, {'h':11})
    printQueue(out, True)

main("graph.txt")
#main("second_graph.txt")
