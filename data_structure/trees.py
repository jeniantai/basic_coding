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
      
print('Once upon a time...')
######
# TREENODE CLASS
######
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



story_root = TreeNode_game("""
You are in a forest clearing. There is a path to the left.
A bear emerges from the trees and roars!
Do you: 
1 ) Roar back!
2 ) Run to the left...
""")

user_choice = input('What is your name?')
print(user_choice)
######
# VARIABLES FOR TREE
######
# each node is a piece of story
choice_a = TreeNode_game("""
The bear is startled and runs away.
Do you:
1 ) Shout 'Sorry bear!'
2 ) Yell 'Hooray!'
""")

choice_b = TreeNode_game("""
You come across a clearing full of flowers. 
The bear follows you and asks 'what gives?'
Do you:
1 ) Gasp 'A talking bear!'
2 ) Explain that the bear scared you.
""")
# add two choices for a middle section of story line stored inside of story_root.choices
story_root.add_child(choice_a)
story_root.add_child(choice_b)

choice_a_1 = TreeNode_game("""
The bear returns and tells you it's been a rough week. After making peace with
a talking bear, he shows you the way out of the forest.

YOU HAVE ESCAPED THE WILDERNESS.
""")
choice_a_2 = TreeNode_game("""
The bear returns and tells you that bullying is not okay before leaving you alone
in the wilderness.

YOU REMAIN LOST.
""")

choice_b_1 = TreeNode_game("""
The bear is unamused. After smelling the flowers, it turns around and leaves you alone.

YOU REMAIN LOST.
"""
)
choice_b_2 = TreeNode_game("""
The bear understands and apologizes for startling you. Your new friend shows you a 
path leading out of the forest.

YOU HAVE ESCAPED THE WILDERNESS.
""")

choice_a.add_child(choice_a_1)
choice_a.add_child(choice_a_2)
choice_b.add_child(choice_b_1)
choice_b.add_child(choice_b_2)

######
# TESTING AREA
######
story_root.traverse()


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


class MaxHeap:
  def __init__(self):
    self.heap_list = [None]
    self.count = 0

  # HEAP HELPER METHODS
  # DO NOT CHANGE!
  def parent_idx(self, idx):
    return idx // 2

  def left_child_idx(self, idx):
    return idx * 2

  def right_child_idx(self, idx):
    return idx * 2 + 1

  # END OF HEAP HELPER METHODS
  def add(self, element):
    self.count += 1
    print("Adding: {0} to {1}".format(element, self.heap_list))
    self.heap_list.append(element)
    self.heapify_up()
    
  def heapify_up(self):
    print("Heapifying up")
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
