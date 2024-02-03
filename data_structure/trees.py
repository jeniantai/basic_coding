class TreeNode:
  def __init__(self, value):
    self.value = value
    self.children = []

  def __repr__(self, level=0):
    # helper method to print tree
    ret = "--->" * level + repr(self.value) + "\n"
    for child in self.children:
      ret += child.__repr__(level+1)
    return ret

  def add_child(self, child_node):
    self.children.append(child_node) 


class TreeNodeFull:
  def __init__(self, value):
    self.value = value
    self.children = []

  def __repr__(self, level=0):
    # helper method to print tree
    ret = "--->" * level + repr(self.value) + "\n"
    for child in self.children:
      ret += child.__repr__(level+1)
    return ret

  def add_child(self, child_node):
    # prevent adding a child node which already exists in self.children
    if child_node in self.children:
      return
    print("Adding " + child_node.value)
    self.children.append(child_node) 

  def remove_child(self, child_node):
    print("Removing " + child_node.value + " from " + self.value)
    self.children = [child for child in self.children if child != child_node]

  def traverse(self):
    print("Traversing...")
    # moves through each node referenced from self downwards
    nodes_to_visit = [self]
    while len(nodes_to_visit)>0:
      current_node = nodes_to_visit.pop()
      print(current_node.value)
      nodes_to_visit += current_node.children


# Choose-Your-Own-Adventure Game
# the flow:
# print out the story_node.story_piece.
# while story_node.choices has nodes inside…
# prompt the user for a choice.
# set story_node to be the user’s story choice.
# repeat until the story is over!
      

######
# An interactive game class
class TreeNode_game:
  def __init__(self, story_piece):
    self.story_piece = story_piece
    self.choices = []

  def add_child(self, node):
    self.choices.append(node)

  def traverse(self):
    story_node = self
    print(story_node.story_piece)
    while len(story_node.choices) > 0:
      choice = input('Enter 1 or 2 to continue the story:')
      if choice not in ['1', '2']:
        print('Please input 1 or 2.')
      chosen_index = int(choice) - 1
      chosen_child = story_node.choices[chosen_index]
      print(chosen_child.story_piece)
      story_node = chosen_child



# Below is used for breadth-first search / depth-first search
from collections import deque

class TreeNode_bd:
  def __init__(self, value):
   self.value = value
   self.children = []

  def __repr__(self):
    return self.value

  def add_child(self, child_node):
    # creates parent-child relationship
    print("Adding " + child_node.value)
    self.children.append(child_node) 
    
  def remove_child(self, child_node):
    # removes parent-child relationship
    print("Removing " + child_node.value + " from " + self.value)
    self.children = [child for child in self.children 
                     if child is not child_node]

  def traverse(self):
    # moves through each node referenced from self downwards
    nodes_to_visit = [self]
    while len(nodes_to_visit) > 0:
      current_node = nodes_to_visit.pop()
      print(current_node.value)
      nodes_to_visit += current_node.children

  ## replaced by print_tree below
  # def __str__(self):
  #   stack = deque()
  #   stack.append([self, 0])
  #   level_str = "\n"
  #   while len(stack) > 0:
  #     node, level = stack.pop()
      
  #     if level > 0:
  #       level_str += "| "*(level-1)+ "|-"
  #     level_str += str(node.value)
  #     level_str += "\n"
  #     level+=1
  #     for child in reversed(node.children):
  #       stack.append([child, level])

  #   return level_str

# Breadth-first search function
def bfs(root_node, goal_value):

  # initialize frontier queue
  path_queue = deque()

  # With deque() class, we will add elements with the .appendleft() method
  # and remove elements with the .pop() method
  # add root path to the frontier
  initial_path = [root_node]
  path_queue.appendleft(initial_path)
  
  # search loop that continues as long as
  # there are paths in the frontier
  while path_queue:
    # get the next path and node 
    # then output node value
    current_path = path_queue.pop()
    current_node = current_path[-1]
    print(f"Searching node with value: {current_node.value}")

    # check if the goal node is found
    if current_node.value == goal_value:
      return current_path

    # add paths to children to the frontier
    for child in current_node.children:
      # alternative to current_path[:]
      # new_path = current_path.copy()
      new_path = current_path[:]
      new_path.append(child)
      path_queue.appendleft(new_path)

  # return an empty path if goal not found
  return None

# recursive version of depth-first search
def print_tree(root):
  stack = deque()
  stack.append([root, 0])
  level_str = "\n"
  prev_level = 0
  level = 0
  while len(stack) > 0:
    prev_level = level
    node, level = stack.pop()
    
    if level > 0 and len(stack) > 0 and level <= stack[-1][1]:
      level_str += "   "*(level-1)+ "├─"
    elif level > 0:
      level_str += "   "*(level-1)+ "└─"
    level_str += str(node.value)
    level_str += "\n"
    level+=1
    for child in node.children:
      stack.append([child, level])

  print(level_str)

  def print_path(path):
    # If path is None, no path was found
    if path == None:
      print("No paths found!")

    # If a path was found, print path
    else:  
      print("Path found:")
      for node in path:
        print(node.value)

# recursive dfs without tracking the paths
def dfs_wo_path(root, target):
  if root.value == target:
    return root
  
  for child in root.children:
    node_found = dfs_wo_path(child, target)
    if node_found != None:
      return node_found
  
  return None


# accepting path as a varialble so that we can maintain the path by passing
# the current search path to the recursive call, and adding the current node 
# to the end of the current path before checking for value equality.
def dfs_w_path(root, target, path=()):
  path = path + (root,)
  
  if root.value == target:
    return path

  for child in root.children:
    node_found = dfs_w_path(child, target, path)

    if node_found is not None:
      return node_found

  return None

# Our MaxHeap must abide by two principles:
# The element at index 1 is the maximum value in the entire list.
# Every “child” element in the list must be smaller than their “parent”
# The first element we add to the list will automatically be the maximum 
# value since there are no other elements in our heap. 
class MaxHeap:
  def __init__(self):
    self.heap_list = [None]
    self.count = 0

  # HEAP HELPER METHODS
  # to determine the relationship of elements with the internal list
  def parent_idx(self, idx):
    return idx // 2

  def left_child_idx(self, idx):
    return idx * 2

  def right_child_idx(self, idx):
    return idx * 2 + 1

  def child_present(self, idx):
    return self.left_child_idx(idx) <= self.count
  
  # handle adding an element to the heap via the .heap_list property.
  def add(self, element):
    self.count += 1
    print("Adding: {0} to {1}".format(element, self.heap_list))
    self.heap_list.append(element)
    self.heapify_up()
    
  # maintaining the heap properties as we add additional elements
  def heapify_up(self):
    print("Restoring the heap property…")
    # idx = last index of the list
    idx = self.count
    while self.parent_idx(idx) > 0:
      child = self.heap_list[idx]
      parent = self.heap_list[self.parent_idx(idx)]
      if parent < child:
        print("swapping {0} with {1}".format(parent, child))
        self.heap_list[idx] = parent
        self.heap_list[self.parent_idx(idx)] = child
      idx = self.parent_idx(idx)
    print("Heap Restored {0}".format(self.heap_list))

  def retrieve_max(self):
    if self.count == 0:
      print("No items in heap")
      return None
    max_value = self.heap_list[1]
    print("Removing: {0} from {1}".format(max_value, self.heap_list))
    self.heap_list[1] = self.heap_list[self.count]
    self.count -= 1
    self.heap_list.pop()
    print("Last element moved to first: {0}".format(self.heap_list))    
    self.heapify_down()
    return max_value

  def heapify_down(self):
    idx = 1
    while self.child_present(idx):
      print("Heapifying down!")
      larger_child_idx = self.get_larger_child_idx(idx)
      child = self.heap_list[larger_child_idx]
      parent = self.heap_list[idx]
      if parent < child:
        # parent swaps with the larger child
        self.heap_list[idx] = child
        self.heap_list[larger_child_idx] = parent
      idx = larger_child_idx
    print("HEAP RESTORED! {0}".format(self.heap_list))
    print("") 

  def get_larger_child_idx(self, idx):
    if self.right_child_idx(idx) > self.count:
      print("There is only a left child")
      return self.left_child_idx(idx)
    else:
      left_child = self.heap_list[self.left_child_idx(idx)]
      right_child = self.heap_list[self.right_child_idx(idx)]
      if left_child > right_child:
        print("Left child "+ str(left_child) + " is larger than right child " + str(right_child))
        return self.left_child_idx(idx)
      else:
        print("Right child " + str(right_child) + " is larger than left child " + str(left_child))
        return self.right_child_idx(idx)
