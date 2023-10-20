def count(N):
  count = 0
  while N > 1:
    N = N//2
    count += 1
  return count


num_iterations_1 = count(1)
print("The while loop performs {0} iterations when N is 1".format(num_iterations_1))

num_iterations_2 = count(2)
print("\nThe while loop performs {0} iterations when N is 2".format(num_iterations_2))

num_iterations_4 = count(4)
print("\nThe while loop performs {0} iterations when N is 4".format(num_iterations_4))

num_iterations_32 = count(32)
print("\nThe while loop performs {0} iterations when N is 32".format(num_iterations_32))

num_iterations_64 = count(64)
print("\nThe while loop performs {0} iterations when N is 64".format(num_iterations_64))

runtime = "log N"
print("\nThe runtime for this function is O({0})".format(runtime))



def find_max(linked_list):
  print("--------------------------")
  print("Finding the maximum value of:\n{0}".format(linked_list.stringify_list()))
  current_node = linked_list.get_head_node()
  maximum_val = current_node.get_value()

  while current_node.get_next_node():
    current_node = current_node.get_next_node()
    if current_node.get_value() > maximum_val:
      maximum_val = current_node.get_value()

  return maximum_val

import sys, os
sys.path.append('C:/Users/Jenian/Desktop/github/basic_coding')
from data_structure.linkedlist import LinkedList
def sort_linked_list(linked_list):
  print("\n---------------------------")
  print("The original linked list is:\n{0}".format(linked_list.stringify_list()))
  new_linked_list = LinkedList()
  
  while linked_list.get_head_node():
    current_max = find_max(linked_list)
    linked_list.remove_node(current_max)
    new_linked_list.insert_beginning(current_max)
  
  return new_linked_list

