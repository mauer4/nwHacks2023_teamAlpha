class Node:
    def __init__(self, category, weight, leaves=[]):
        self.category = category
        self.weight = weight
        self.leaves = leaves
        self.height = 0

# Create the root node
root = Node("Root Category", 0.5)

# Create the first leaf node
first_leaf = Node("First Leaf Category", 0.3)
# Create the second leaf node
second_leaf = Node("Second Leaf Category", 0.7)
# Create the third leaf node
third_leaf = Node("Third Leaf Category", 0.5)
# Create the fourth leaf node
fourth_leaf = Node("Forth Leaf Category", 0.5)

# Add the leaf nodes to the root node
root.leaves.append(first_leaf)
root.leaves.append(second_leaf)
root.leaves.append(third_leaf)
root.leaves[0].leaves.append(fourth_leaf)

def addToTree(root, leaves):
    root.height += 1
    leaves = getLeaves(root, root.height)
    

def getLeaves(leaf, height):
    if height == 0:
            return [leaf]
    elif height == 1:
        return leaf.leaves
    else:
        for leaf in leaf.leaves:
            return getLeaves(leaf, height-1)

root.height += 2
leaves = getLeaves(root, root.height)
for leaf in leaves:
    print(leaf.category)

print(root.leaves[0].leaves)