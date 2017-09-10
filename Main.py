from Algorithms2 import *
import graphParser

# Print
def printQueue(queue):
    print(queue)
    for p in queue:
        line = "["
        for i in p:
            line += str(i['h'])
            pathstr = str(i['path'])
            pathstr = pathstr[1:len(pathstr)-1]
            line += "<" + pathstr + ">"
            line += "]"
        print(line)
    print()

# Main
def main(file):
    print("Running search on " + file)
    graph_data = graphParser.build_graph(file)

    print("Depth 1st search")
    Q, out = General_Search(graph_data, depthFirst, {})
    #printQueue(out)
    print(out)

    print("Breadth 1st search")
    Q, out = General_Search(graph_data, breadthFirst, {})
    print(out)

    print("Depth-limited search (limit = 2)")
    Q, out = General_Search(graph_data, depthLimited, {"limit":2})

    print("Iterative deepening search")
    Q, out = General_Search(graph_data, iterativeDeepening, {})

    print("Uniform Search (Branch-and-bound)")
    Q, out = General_Search(graph_data, uniformCost)

    print("Greedy search")
    Q, out = General_Search(graph_data, greedySearch, {})

    print("A*")
    Q, out = General_Search(graph_data, aStarSearch, {})

    print("Hill climbing search (No backtracking)")
    Q, out = General_Search(graph_data, hillClimbing, {})

    print("Beam search (w = 2)")
    Q, out = General_Search(graph_data, beam, {})

main("second_graph.txt")
