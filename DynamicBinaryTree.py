# This program will find the minimum cost of a binary tree

NodeMax = [0]*100
 
#Function for DepthFirstSearch traversal which stores the maximum value
#for every node until it reaches every leave node
def DepthFirstSearch(values, vertex, unit, parent):
     
    #Initially NodeMax[unit] is always values[unit]
    NodeMax[unit] = values[unit - 1]
     
    #Minimum value from nodes set to infinity at first
    minimum = float('inf')
     
    # Traverse the tree
    for child in vertex[unit]:
         
        # continue if child is a parent 
        if child == parent:
            continue
         
        # DepthFirstSearch for further traversal
        DepthFirstSearch(values, vertex, child, unit)
         
        # keep the maximum of previous node and current node 
        minimum = min(minimum, NodeMax[child])
         
    # Add to the minimum value sent to the parent node
    if len(vertex[unit]) !=1:
        NodeMax[unit] += minimum

# Function that returns the minimum value
def minimumValue(values, vertex):
    DepthFirstSearch(values, vertex, 1, 0)
    return NodeMax[1]
 
# Driver Code 
def main():     
    #amount of nodes 
    noNodes = 15
     
    # place all vertex in a list
    vertex = {}
    for i in range(noNodes + 1):
        vertex[i] = []

#         8
#      /     \
#     4        12
#    / \      /   \
#   2    6   10    14 
#  / \  / \  / \   / \
# 1  3  5 7 9  11 13 15

    values = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]

    # build the tree from the diagram with undirected edges
    vertex[1].append(2), vertex[2].append(1)
    vertex[1].append(3), vertex[3].append(1)
    vertex[2].append(4), vertex[4].append(2) 
    vertex[2].append(5), vertex[5].append(2) 
    vertex[3].append(6), vertex[6].append(3)
    vertex[3].append(7), vertex[7].append(3) 
    vertex[4].append(8), vertex[8].append(4) 
    vertex[4].append(9), vertex[9].append(4) 
    vertex[5].append(10), vertex[10].append(5) 
    vertex[5].append(11), vertex[11].append(5) 
    vertex[6].append(12), vertex[12].append(6) 
    vertex[6].append(13), vertex[13].append(6)
    vertex[7].append(14), vertex[14].append(7)
    vertex[7].append(15), vertex[15].append(7)

    print("the minimum cost of this binary tree is: " + str(minimumValue(values, vertex)))

main() 
