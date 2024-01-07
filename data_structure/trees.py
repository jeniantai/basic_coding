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