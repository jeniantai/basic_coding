from data_structure.linkedlist import Node, LinkedList


class Queue:
  def __init__(self, max_size=None):
    self.head = None
    self.tail = None
    self.max_size = max_size
    self.size = 0
    
  def peek(self):
    if self.is_empty():
      print("Nothing to see here!")
    else:
      return self.head.get_value()
  
  def get_size(self):
    return self.size
  
  def has_space(self):
    if self.max_size == None:
      return True
    else:
      return self.max_size > self.get_size()
    
  def is_empty(self):
    return self.size == 0
  
  def enqueue(self, value):
    if self.has_space():
      item_to_add = Node(value)
      print("Adding " + str(item_to_add.get_value()) + " to the queue!")
      if self.is_empty():
        self.head = item_to_add
        self.tail = item_to_add
      else:
        self.tail.set_next_node(item_to_add)
        self.tail = item_to_add
      self.size += 1
    else:
      print("Sorry, no more room!")

  def dequeue(self):
    if self.get_size() > 0:
      item_to_remove = self.head
      print("Removing " + str(item_to_remove.get_value()) + " from the queue!")
      if self.get_size() == 1:
        self.head = None
        self.tail = None
      else:
        self.head = self.head.get_next_node()
      self.size -= 1
      return item_to_remove.get_value()
    else:
      print("This queue is totally empty!")


class Stack:
  def __init__(self, name):
    self.size = 0
    self.top_item = None
    self.limit = 1000
    self.name = name
  
  def push(self, value):
    if self.has_space():
      item = Node(value)
      item.set_next_node(self.top_item)
      self.top_item = item
      self.size += 1
    else:
      print("No more room!")

  def pop(self):
    if self.size > 0:
      item_to_remove = self.top_item
      self.top_item = item_to_remove.get_next_node()
      self.size -= 1
      return item_to_remove.get_value()
    print("This stack is totally empty.")

  def peek(self):
    if self.size > 0:
      return self.top_item.get_value()
    print("Nothing to see here!")

  def has_space(self):
    return self.limit > self.size

  def is_empty(self):
    return self.size == 0
  
  def get_size(self):
    return self.size
  
  def get_name(self):
    return self.name
  
  def print_items(self):
    pointer = self.top_item
    print_list = []
    while(pointer):
      print_list.append(pointer.get_value())
      pointer = pointer.get_next_node()
    print_list.reverse()
    print("{0} Stack: {1}".format(self.get_name(), print_list))


# print("\nLet's play Towers of Hanoi!!")
# # The game follows three rules:
# # Only one disk can be moved at a time.
# # Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or on an empty rod.
# # No disk may be placed on top of a smaller disk.

# #Create the Stacks
# left_stack = Stack('Left')
# middle_stack = Stack('Middle')
# right_stack = Stack('Right')

# stacks = [left_stack, middle_stack, right_stack]

# #Set up the Game
# num_disks = int(input("\nHow many disks do you want to play with?\n"))

# while num_disks<3:
#   num_disks = int(input('Enter a number greater than or equal to 3\n'))

# for disk in range(num_disks, 0, -1):
#   left_stack.push(disk)

# num_optimal_moves = 2**num_disks-1
# print("\nThe fastest you can solve this game is in {0} moves".format(num_optimal_moves))

# #Get User Input
# def get_input():
#   choices = [stack.get_name()[0] for stack in stacks]
#   while True:
#     for i in range(len(stacks)):
#       name = stacks[i].get_name()
#       letter = choices[i]
#       print("Enter {0} for {1}".format(letter, name))
#     user_input = input('')
#     if user_input in choices:
#       for i in range(len(stacks)):
#         return stacks[choices.index(user_input)]

# #Play the Game
# num_user_moves = 0
# while right_stack.get_size() != num_disks:
#   print("\n\n\n...Current Stacks...")
#   for stack in stacks:
#     stack.print_items()
#   while True:
#     print("\nWhich stack do you want to move from?\n")
#     from_stack = get_input()
#     print("\nWhich stack do you want to move to?\n")
#     to_stack = get_input()

#     if from_stack.is_empty():
#       print("\n\nInvalid Move from empty stack. Try Again")
#     elif to_stack.is_empty() or from_stack.peek() < to_stack.peek():
#       disk = from_stack.pop()
#       to_stack.push(disk)
#       num_user_moves += 1
#       break
#     else:
#       #if the user tries to move a larger disk onto a smaller disk.
#       print("\n\nInvalid Move of larger disk to smaller. Try Again")

#   print("\n\nYou completed the game in {0} moves, and the optimal number of moves is {1}".format(num_user_moves, num_optimal_moves))
    

# HASHMAP - PROBING
# simulate an array by creating a list and keeping track of the size of the list with an additional integer variable.
class HashMap:
  def __init__(self, array_size):
    self.array_size = array_size
    self.array = [None for i in range(self.array_size)]

  def hash(self, key, count_collisions=0):
    # turn key into a list of bytes
    key_bytes = key.encode()
    # turn the bytes object into a hash code
    hash_code = sum(key_bytes)
    # uses the number of collisions to determine the hash code
    return hash_code + count_collisions
  
  # a compressor ensures that the index is always within the bounds of the array
  def compressor(self, hash_code):
    return hash_code%self.array_size
  
  # define the setter
  def assign(self, key, value):
    array_index = self.compressor(self.hash(key))
    current_array_value = self.array[array_index]

    if current_array_value is None:
      self.array[array_index] = [key, value]
      return

    # overwrite if key match
    # current_array_value holds our key/value pairs in an array that looks like [key, value]. 
    # So to check if the keys are equal, you should compare key to current_array_value[0]
    if current_array_value[0] == key:
      self.array[array_index] = [key, value]
      return

    # Collision! 
    number_collisions = 1

    while(current_array_value[0] != key):
      new_hash_code = self.hash(key, number_collisions)
      new_array_index = self.compressor(new_hash_code)
      current_array_value = self.array[new_array_index]
      # check again after increment
      if current_array_value is None:
        self.array[new_array_index] = [key, value]
        return

      if current_array_value[0] == key:
        self.array[new_array_index] = [key, value]
        return

      number_collisions += 1
    return
  
  # define the getter
  def retrieve(self, key):
    array_index = self.compressor(self.hash(key))
    possible_return_value = self.array[array_index]

    if possible_return_value is None:
        return None

    if possible_return_value[0] == key:
        return possible_return_value[1]

    # possible_return_value holds different key
    retrieval_collisions = 1

    while (possible_return_value != key):
      new_hash_code = self.hash(key, retrieval_collisions)
      retrieving_array_index = self.compressor(new_hash_code)
      possible_return_value = self.array[retrieving_array_index]

      if possible_return_value is None:
        return None

      if possible_return_value[0] == key:
        return possible_return_value[1]

      retrieval_collisions += 1

    return
  

# HASHMAP - CHAIN

class HashMap_LL:
  def __init__(self, size):
    self.array_size = size
    self.array = [LinkedList() for i in range(size)]

  def hash(self, key):
    return sum(key.encode())

  def compress(self, hash_code):
    return hash_code%self.array_size

  def assign(self, key, value):
    array_index = self.compress(self.hash(key))
    payload = Node([key, value])
    list_at_array = self.array[array_index]
    for item in list_at_array:
      if item[0] == key:
        item[1] = value
        return
    # if return, the following line wont happen
    list_at_array.insert(payload)

  def retrieve(self, key):
    array_index = self.compress(self.hash(key))
    list_at_index = self.array[array_index]
    for item in list_at_index:
      if item[0] == key:
        return item[1]
    return None