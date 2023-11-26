# NODES

## A Node class with an accessible but immutable value
class Node:
  def __init__(self, value, prev_node=None, next_node=None):
    self.value = value
    self.next_node = next_node
    self.prev_node = prev_node
    
  ## Define your getters - get_value and get_next_node methods below:
  def get_value(self):
    return self.value

  def get_next_node(self):
    return self.next_node
  
  def get_prev_node(self):
    return self.prev_node
  
  ## Define your set_next_node method to allow updating the link of the node after creation of instance:
  def set_next_node(self, next_node):
    self.next_node = next_node

  def set_prev_node(self, prev_node):
    self.prev_node = prev_node
  
  def flatten(self):
    flat_lst = []
    temp = self
    while temp:
      flat_lst.append(temp.value)
      temp = temp.next_node
    return flat_lst


# LINKED LIST

## Create LinkedList class which can be instantiated with a head node:
class LinkedList:
  def __init__(self, value=None):
    # avoid creating None node
    if value is None:
      self.head_node = None
    else:
      self.head_node = Node(value)

  def get_head_node(self):
    return self.head_node
  
## Method to insert a new head node:
  def insert_beginning(self, new_value):
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node

## Method to print of the value of the LinkedList
  def stringify_list(self):
    string_list = '<head> \n'
    current_node = self.get_head_node()
    while current_node:
      if current_node.get_value() != None:
        string_list += str(current_node.get_value()) + "\n"
      current_node = current_node.get_next_node()
    string_list += '<tail>'
    return string_list

## Method to remove node:
  def remove_node(self, value_to_remove):
    current_node = self.get_head_node()
    if current_node.get_value() == value_to_remove:
      self.head_node = current_node.get_next_node()
    else:
      ## Check if current node exists
      while current_node:
        next_node = current_node.get_next_node()
        if next_node.get_value() == value_to_remove:
          current_node.set_next_node(next_node.get_next_node())
          ## exit the loop
          current_node = None
        else:
          current_node = next_node

  def find_node_iteratively(self, value):
      current_node = self.head_node
      
      while current_node:
        if current_node.value == value:
          return current_node
        current_node = current_node.get_next_node()
        
      return None
      
  def find_node_recursively(self, value, current_node):
    if current_node == None:
      return None
    elif current_node.value == value:
      return current_node
    else:
      return self.find_node_recursively(value, current_node.get_next_node())

  # insert Node itself not value, at the end
  def insert(self, new_node):
    current_node = self.head_node

    if not current_node:
      self.head_node = new_node

    while(current_node):
      next_node = current_node.get_next_node()
      if not next_node:
        current_node.set_next_node(new_node)
      current_node = next_node

# without this method, 'LinkedList' object is not iterable
  def __iter__(self):
    current_node = self.head_node
    while(current_node):
      yield current_node.get_value()
      current_node = current_node.get_next_node()



# Function to swap nodes of a list
def swap_nodes(input_list, val1, val2):
  print(f'Swapping {val1} with {val2}')
  node1 = input_list.head_node
  node2 = input_list.head_node
  node1_prev = None
  node2_prev = None

  ## Edge case 1
  if val1 == val2:
    print('Elements are the same - no swap needed')
    return

  while node1 is not None:
    if node1.get_value() == val1:
      break
    node1_prev = node1
    node1 = node1.get_next_node()

  while node2 is not None:
    if node2.get_value() == val2:
      break
    node2_prev = node2
    node2 = node2.get_next_node()

  ## Edge case 2
  if (node1 is None or node2 is None):
    print("Swap not possible - one or more element is not in the list")
    return

  if node1_prev is None:
    input_list.head_node = node2
  else:
    node1_prev.set_next_node(node2)

  if node2_prev is None:
    input_list.head_node = node1
  else:
    node2_prev.set_next_node(node1)

  temp = node1.get_next_node()
  node1.set_next_node(node2.get_next_node())
  node2.set_next_node(temp)



## pseudocode of swapping two specific value
## 1. Iterate through the list looking for the node that matches val1 to be swapped (node1), 
## keeping track of the node's previous node (node1_prev)
## 2. Repeat step 1 looking for the node that matches val2 (giving you node2 and node2_prev)
## 3. If node1_prev is None, node1 was the head of the list, so set the list's head to node2
## 4. Otherwise, set node1_prev's next node to node2
## 5. If node2_prev is None, set the list's head to node1
## 6. Otherwise, set node2_prev's next node to node1
## 7. Set node1's next node to node2's next node, node2's next node to node1's next node


# TWO-POINTER LINKED LIST
## In order to return e.g. the 3rd to last element in a singly linked list, one method 
## first come to mind is to use a list to store a representation of the linked list, 
## and then to obtain the nth to last element from this list. While this approach results in 
## an easy-to-read implementation, it could also use up lots of memory e.g. if the linked list 
## has one million nodes, we'll need one million pointers in a list to keep track of it.
## An approach like this results in an extra O(n) space being allocated.


## The following function complete this problem efficiently, in O(n) time (we must iterate through the entire list once), 
## and O(1) space complexity (we always use only three variables no matter what size the linked list is: two pointers and a counter).
def nth_last_node(linked_list, n):
  current_node = None
  tail_seeker = linked_list.head_node
  count = 1
  while tail_seeker:
    tail_seeker = tail_seeker.get_next_node()
    count += 1
    ## start pointing back to locate nth node when available
    if count >= n + 1:
      if current_node is None:
        current_node = linked_list.head_node
      else:
        current_node = current_node.get_next_node()
  return current_node


# POINTERS AT DIFFERENT SPEEDS
## The first pointer takes two steps through the linked list for every one step that the second takes, so it iterates twice as fast

def find_middle(linked_list):
  fast = linked_list.head_node
  slow = linked_list.head_node
  while fast:
    fast = fast.get_next_node()
    if fast:
      fast = fast.get_next_node()
      slow = slow.get_next_node()
  return slow

## Another equally valid solution is to move the fast pointer once with each loop iteration but 
## only move the slow pointer every-other iteration:
def find_middle_alt(linked_list):
  count = 0
  fast = linked_list.head_node
  slow = linked_list.head_node
  while fast:
    fast = fast.get_next_node()
    if count % 2 != 0:
      slow = slow.get_next_node()
    count += 1
  return slow


# DOUBLY LINKED LIST
## Doubly linked list added tail_node property on top of head_node for the list.
class DoublyLinkedList:
  def __init__(self):
    self.head_node = None
    self.tail_node = None

  def add_to_head(self, new_value):
    new_head = Node(new_value)
    current_head = self.head_node

    ## the list isnt empty
    if current_head != None:
      current_head.set_prev_node(new_head)
      new_head.set_next_node(current_head)

    ## set the list head node to new_head
    self.head_node = new_head

    if self.tail_node == None:
      self.tail_node = new_head

  def add_to_tail(self, new_value):
    new_tail = Node(new_value)
    current_tail = self.tail_node

    if current_tail != None:
      current_tail.set_next_node(new_tail)
      new_tail.set_prev_node(current_tail)

    self.tail_node = new_tail

    if self.head_node == None:
      self.head_node = new_tail

  def remove_head(self):
      removed_head = self.head_node

      if removed_head == None:
        return None

      self.head_node = removed_head.get_next_node()

      if self.head_node != None:
        self.head_node.set_prev_node(None)

      if removed_head == self.tail_node:
        self.remove_tail()

      return removed_head.get_value()
  
  def remove_tail(self):
    removed_tail = self.tail_node

    if removed_tail == None:
      return None

    self.tail_node = removed_tail.get_prev_node()

    if self.tail_node != None:
      self.tail_node.set_next_node(None)

    if removed_tail == self.head_node:
      self.remove_head()

    return removed_tail.get_value()

  def remove_by_value(self, value_to_remove):
    node_to_remove = None
    current_node = self.head_node

    while current_node != None:
      if current_node.get_value() == value_to_remove:
        node_to_remove = current_node
        break

      current_node = current_node.get_next_node()

    if node_to_remove == None:
      return None
      
    if node_to_remove == self.head_node:
      self.remove_head()
    elif node_to_remove == self.tail_node:
      self.remove_tail()
    else:
      next_node = node_to_remove.get_next_node()
      prev_node = node_to_remove.get_prev_node()
      next_node.set_prev_node(prev_node)
      prev_node.set_next_node(next_node)
    
    return node_to_remove

  def stringify_list(self):
    string_list = ""
    current_node = self.head_node
    while current_node:
      if current_node.get_value() != None:
        string_list += str(current_node.get_value()) + "\n"
      current_node = current_node.get_next_node()
    return string_list
  


