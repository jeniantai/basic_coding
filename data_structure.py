# NODES

## A Node class with an accessible but immutable value
class Node:
  def __init__(self, value, link_node=None):
    self.value = value
    self.link_node = link_node
    
  ## Define your getters - get_value and get_link_node methods below:
  def get_value(self):
    return self.value

  def get_link_node(self):
    return self.link_node
  
  ## Define your set_link_node method to allow updating the link of the node after creation of instance:
  def set_link_node(self, link_node):
    self.link_node = link_node


yacko = Node("likes to yak")
wacko = Node("has a penchant for hoarding snacks")
dot = Node("enjoys spending time in movie lots")

## Give these nodes some responsibilities!
yacko.set_link_node(dot)
dot.set_link_node(wacko)

dots_data = yacko.get_link_node().get_value()
wackos_data = dot.get_link_node().get_value()
print(dots_data)
print(wackos_data)

## Relationship between data is built.
## Since the nodes use links to denote the next node in the sequence, 
## the nodes are not required to be sequentially located in memory! 


# LINKED LIST ALGORITHM

# Create LinkedList class which can be instantiated with a head node:
class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)

  def get_head_node(self):
    return self.head_node
  
# Method to insert a new head node:
  def insert_beginning(self, new_value):
    new_node = Node(new_value)
    new_node.set_link_node(self.head_node)
    self.head_node = new_node

# Method to print of the value of the LinkedList
  def stringify_list(self):
    string_list = ""
    current_node = self.get_head_node()
    while current_node != None:
      string_list += str(current_node.get_value()) + "\n"
      current_node = current_node.get_link_node()
    return string_list
    
# Test the code
ll = LinkedList(5)
ll.insert_beginning(70)
ll.insert_beginning(5675)
ll.insert_beginning(90)
print(ll.stringify_list())