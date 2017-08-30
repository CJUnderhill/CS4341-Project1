# Main controller for CS 4341 Project 1
# Developed by Chad Underhill on 8/30/2017

import sys
import argparse

# Build graph from graph file
# Params:
#		graph_file:	PATH	Path to text file containing graph information
# Returns:
#		Tuple containing ___ and hash map structure with heuristic information
def build_graph(graph_file):


# Main function
def main():
	# Parse input arguments
	parser = argparse.ArgumentParser(description='Process textual graphs using various search algorithms.')
	parser.add_argument('graph_file', help='Graph file to read in from.', default=(sys.path[0]+'/graph.txt'))

	args = parser.parse_args(sys.argv[1:2])
	#TODO: Error handling on arg parse?

	# Build graph from file
	build_graph(args.graph_file)


if __name__ == "__main__":
	# Run main function, with exception handling
	try:
		main()
	except Exception as err:
		print "Unhandled Exception: " + err