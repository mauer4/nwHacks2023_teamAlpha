from src.NLP.SomeText import SomeText

class Node:
    def __init__(self, text, weight, leaves=[]):
        self.text = text
        self.weight = weight
        self.leaves = leaves

# Create the root node
root = Node(SomeText("Root Category", 1), 0.5)

# Create the first leaf node
first_leaf = Node(SomeText("First Leaf Category", 0.7), 0.3)
# Create the second leaf node
second_leaf = Node(SomeText("Second Leaf Category", 0.3), 0.7)
# Create the third leaf node
third_leaf = Node(SomeText("Third Leaf Category", 0.5), 0.5)

# Add the leaf nodes to the root node
root.leaves.append(first_leaf)
root.leaves.append(second_leaf)
root.leaves.append(third_leaf)