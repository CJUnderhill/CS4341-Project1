# Project 1 | CS4341 | A-Term (Fall 2017) | Prof. Carolina Ruiz | Worcester Polytechnic Institute
#
# This file contains a sorting function and its helpers to sort the queue at each part of the trace.
#
# @author Chad Underhill, Daniel Kim, Spiros Antonatos
# @since 9/11/2017

def cmp_to_key(mycmp):
    'Convert a cmp= function into a key= function'
    class K(object):
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0  
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K


def compare(a,b):
    vala = a['h']
    valb = b['h']
    lista = a['path']
    listb = b['path']

    if(vala != valb):
        if(vala < valb):
            return -1
        else:
            return 1
    else:
        if lista[0] != listb[0]:
            if lista[0] > listb[0]:
                return 1
            else:
                return -1
        else:
            if len(lista) != len(listb):
                if len(lista) < len(listb):
                    return -1
                else:
                    return 1
            else:
                for i in range(len(lista)):
                    if lista[i] < listb[i]:
                        return -1
                    elif lista[i] > listb[i]:
                        return 1
                    else:
                        continue
                               
            
# This function models the sorting functionality outlined in the project document
# @param newQueue       The queue being updated
# @param tempDict       The current path being updated
# @return newQueue      The updated queue of explored paths, properly sorted
#
def sortFunction(queue):
    newQueue = queue[:] #copy the list 
    newQueue.sort(key = cmp_to_key(compare))
    return newQueue

# Helpers for search; sorts by least cost so far and alphabetical order
# @param e  Graph node
# @returns  Value to sort by
#
def leastCost(e):
    return float(e['h'])

def lex(e):
    return e['path'][0]
