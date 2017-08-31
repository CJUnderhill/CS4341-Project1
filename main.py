# Main controller for CS 4341 Project 1
# Developed by Chad Underhill on 8/30/2017
#
# Usage:
# From command-line, call "python main.py" to run using the default "graph.txt" file
# Alternatively, you can specify the path to another graph file by calling "python main.py <path_to_graph_file>"

import sys
import argparse
import networkx as nx

# Use argparse to handle CLI input
# Params:
#		None
# Returns:
#		Namespace containing parsed arguments
#TODO: Error handling on arg parse?
def handle_input():
	# Parse input arguments
	parser = argparse.ArgumentParser(description='Process textual graphs using various search algorithms.')
	parser.add_argument('--graph_file_path', help='Path to input graph file.', default=(sys.path[0]+'/graph.txt'))

	return parser.parse_args(sys.argv[1:2])


# Build graph from graph file
# Params:
#		graph_file:	PATH	Path to text file containing graph information
# Returns:
#		Tuple containing NetworkX graph and hash map structure with heuristic information
def build_graph(graph_file):
	G = nx.Graph()		# Initialize NetworkX graph structure

	heuristic = False	# Track whether filereader has started reading heuristic info
	h = {}				# Heuristic info dictionary

	# Open graph file
	with open(graph_file) as f:
		for line in f:

			# If we're reading graph info
			if heuristic == False:
				if line.strip() == "#####":
					heuristic = True
				else:
					# Split node information
					node_info = line.split()
					G.add_edge(node_info[0], node_info[1], weight=node_info[2])
			else:
				# Split and add heurisic info
				heuristic_info = line.split()
				h[heuristic_info[0]] = heuristic_info[1]

	return (G, h)

# Main function
def main():
	args = handle_input()

	# Build graph from file
	graph_data = build_graph(args.graph_file_path)
	
	print("\n")
	print(graph_data[0].adj)
	print("\n")
	print(graph_data[1])
	print("\n")

# Main function template
if __name__ == "__main__":
	# Run main function with exception handling
	try:
		main()
	except Exception as err:
		print("Unhandled Exception: " + str(err))
