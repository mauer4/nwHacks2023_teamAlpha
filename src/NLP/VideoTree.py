# Create the root node
class Node:
    def __init__(self, category, weight, leaves=[]):
        self.category = category
        self.weight = weight
        self.leaves = leaves

    def get_nth_level_children(self, n):
        if n == 0:
            return [self]
        elif n == 1:
            return self.leaves
        else:
            for leaf in self.leaves:
                return leaf.get_nth_level_children(n-1)

root = Node("Root Category", 0.5)

root.leaves.append(Node("First Leaf Category", 0.3))
root.leaves.append(Node("Second Leaf Category", 0.3))
root.leaves.append(Node("Third Leaf Category", 0.3))

root.leaves[0].leaves.append(Node("Fourth Leaf Category", 0.8))

print(root.leaves[1].leaves[3].category)

# # Create the first level of leaves
# first_level_leaves = [
#     Node("First Leaf Category", 0.3),
#     Node("Second Leaf Category", 0.7),
#     Node("Third Leaf Category", 0.5)
# ]


# # Create the second level of leaves
# second_level_leaves = [
#     Node("Fourth Leaf Category", 0.4),
#     Node("Fifth Leaf Category", 0.8),
#     Node("Sixth Leaf Category", 0.1)
# ]

# # Add the second level of leaves to the first level leaves
# for leaf in first_level_leaves:
#     leaf.leaves += second_level_leaves

# # Add the first level of leaves to the root
# root.leaves += first_level_leaves

# # Print the second level leaves
# for leaf in root.leaves:
#     for second_level_leaf in leaf.leaves:
#         print("here")
#         print(second_level_leaf.category)
#     print("")