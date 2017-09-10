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
