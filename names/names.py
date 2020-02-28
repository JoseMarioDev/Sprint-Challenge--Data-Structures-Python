from binary_search_tree import BinarySearchTree
import time


start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# using BST to improve speed
# I think the runtime complexity is O(n^2) because each for loop is O(n), multiplying each other since we are comparing

duplicates = []
bst = BinarySearchTree("names")

for names in names_1:
    bst.insert(names)
for names in names_2:
    if bst.contains(names):
        duplicates.append(names)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?
