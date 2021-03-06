# Project 1 | CS4341 | A-Term (Fall 2017) | Prof. Carolina Ruiz | Worcester Polytechnic Institute
#
# This program uses a number of search algorithms to process an input graph data structure and print its trace.
#
# @author Chad Underhill, Daniel Kim, Spiros Antonatos
# @since 9/11/2017

from Algorithms import *
import graphParser
from PrintTrace import *

# Individual functions
def DepthFirstSearch(graph_data):
    Q, out = General_Search(graph_data, depthFirst, {'h':0})
    return Q, out

def BreadthFirstSearch(graph_data):
    Q, out = General_Search(graph_data, breadthFirst, {'h':0})
    return Q, out

def DepthLimitedSearch(graph_data):
    Q, out = General_Search(graph_data, depthLimited, {'h':0, "limit":2})
    return Q, out

def IterativeDeepeningSearch(graph_data):
    Q, out = General_Search(graph_data, iterativeDeepening, {'h':0})
    return Q, out

def UniformSearch(graph_data):
    Q, out = General_Search(graph_data, uniformCost, {'h':0})
    return Q, out

def GreedySearch(graph_data):
    Q, out = General_Search(graph_data, greedySearch, {'h':11})
    return Q, out

def AStarSearch(graph_data):
    Q, out = General_Search(graph_data, aStarSearch, {'h':11})
    return Q, out

def HillClimbingSearch(graph_data):
    Q, out = General_Search(graph_data, hillClimbing, {'h':11})
    return Q, out

def BeamSearch(graph_data):
    Q, out = General_Search(graph_data, beam, {'h':11})
    return Q, out


# Main
def main(file):
    print("Running search on " + file)
    graph_data = graphParser.build_graph(file)

    print("Depth 1st search")
    Q, out = DepthFirstSearch(graph_data)
    printTrace(out, False)

    print("Breadth 1st search")
    Q, out = BreadthFirstSearch(graph_data)
    printTrace(out, False)

    print("Depth-limited search (limit = 2)")
    Q, out = DepthLimitedSearch(graph_data)
    printTrace(out, False)

    print("Iterative deepening search")
    IterativeDeepeningSearch(graph_data)

    print("Uniform Search (Branch-and-bound)")
    Q, out = UniformSearch(graph_data)
    printTrace(out, True)

    print("Greedy search")
    Q, out = GreedySearch(graph_data)
    printTrace(out, True)

    print("A*")
    Q, out = AStarSearch(graph_data)
    printTrace(out, True)

    print("Hill climbing search (No backtracking)")
    Q, out = HillClimbingSearch(graph_data)
    printTrace(out, True)

    print("Beam search (w = 2)")
    Q, out = BeamSearch(graph_data)
    printTrace(out, True)


if __name__ == "__main__":
    print("Welcome the graph search program.\n" +
          "Input the path of your txt file that has your graph\n" +
          "and the graph will be searched using 9 different search methods\n")
    path = input("What is the path of your txt file?: ")
    main(path)
