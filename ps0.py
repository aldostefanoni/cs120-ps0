#################
#               #
# Problem Set 0 #
#               #
#################


#
# Setup
#
class BinaryTree:
    def __init__(self, root):
        self.root: BTvertex = root
 
class BTvertex:
    def __init__(self, key):
        self.parent: BTvertex = None
        self.left: BTvertex = None
        self.right: BTvertex = None
        self.key: int = key
        self.size: int = None

#
# Problem 1a
#

# Input: BTvertex v, the root of a BinaryTree of size n
# Output: Up to you
# Side effect: sets the size of each vertex n in the
# ... tree rooted at vertex v to the size of that subtree
# Runtime: O(n)
def calculate_sizes(v):
    v.size = 1
    if v.left == v.right == None:
        return v.size
    if v.left != None:
      v.size += calculate_sizes(v.left)
    if v.right != None:
      v.size += calculate_sizes(v.right)
    return v.size
  # justification of runtime
  # as this algorithm recursively calculates the size of every single vertex
  # it works by operating on each vertex exactly once. Thus, as we know that
  # it must have a runtime of O(n) because it is only operating over all the 
  # vertices only once.
    
#
# Problem 1c
#

# Input: BTvertex r, the root of a size-augmented BinaryTree T
# ... of size n and height h
# Output: A BTvertex that, if removed from the tree, would result
# ... in disjoint trees that all have at most n/2 vertices
# Runtime: O(h)
def find_vertex(r): #11:30    
  if r.size % 2 == 1:             #odd    
    compare = (r.size - 1) / 2 
  else:                           #even
    compare = r.size / 2

  def helper(v):
    if v.left != None and v.right != None: #both children exist
      if v.left.size - 1 == compare:
        return v.left
      elif v.right.size - 1 == compare:
        v.right
      if v.left.size == compare or v.right.size == compare:
        return v
      elif v.left.size > v.right.size:
        return helper(v.left)
      if v.left.size == v.right.size:
        return v
      else:
        return helper(v.right) 
    if v.left == None and v.right != None: #only right child exits
      if v.right.size == compare:
        return v
      if v.right.size - 1 == compare:
        return v.right
      else:
        return helper(v.right)
    if v.left != None and v.right == None: #only left child exists
      if v.left.size == compare:
        return v
      elif v.left.size - 1 == compare:
        return v.left
      else:
        return helper(v.left) 
    if v.size == compare: #if self is compare node
      return v
    if v.left == None and v.right == None: #if neither children exist
      return v
    
  return helper(r)
  # justification of runtime 
  # As this funciton only works by checking the two children of the first
  # node, and then if the vertex to remove is not found in this step it only
  # moves down to the single child with a greater size, we know that for each
  # examination of a node, it will take a constant number of steps, and when
  # it does need to move further down the tree, it will only move down a single
  # path, meaning that the program will complete at the worst case just by
  # traversing down the height of the tree.
  
     
  