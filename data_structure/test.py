from linkedlists import *

# TEST THE CODES

## Relationship between data is built.
yacko = Node("likes to yak")
wacko = Node("has a penchant for hoarding snacks")
dot = Node("enjoys spending time in movie lots")

## Give these nodes some responsibilities!
yacko.set_next_node(dot)
dot.set_next_node(wacko)

dots_data = yacko.get_next_node().get_value()
wackos_data = dot.get_next_node().get_value()
print(dots_data)
print(wackos_data)

## Since the nodes use links to denote the next node in the sequence, 
## the nodes are not required to be sequentially located in memory! 


## Test LinkedList class
ll = LinkedList(5)
ll.insert_beginning(70)
ll.insert_beginning(5675)
ll.insert_beginning(90)
print(ll.stringify_list())


ll_swap = LinkedList()
for i in range(10):
  ll_swap.insert_beginning(i)


print(ll_swap.stringify_list())
swap_nodes(ll_swap, 9, 5)
print(ll_swap.stringify_list())

def generate_test_linked_list():
  linked_list = LinkedList()
  for i in range(50, 0, -1):
    linked_list.insert_beginning(i)
  return linked_list

test_list = generate_test_linked_list()
print(test_list.stringify_list())
nth_last = nth_last_node(test_list, 4)
print(nth_last.value)

def generate_test_linked_list(length):
  linked_list = LinkedList()
  for i in range(length, 0, -1):
    linked_list.insert_beginning(i)
  return linked_list

test_list = generate_test_linked_list(7)
print(test_list.stringify_list())
middle_node = find_middle(test_list)
print(middle_node.value)

subway = DoublyLinkedList()
subway.add_to_head('Times Square')
subway.add_to_head('Grand Central')
subway.add_to_head('Central Park')
print(subway.stringify_list())

subway.add_to_tail('Penn Station')
subway.add_to_tail('Wall Street')
subway.add_to_tail('Brooklyn Bridge')
print(subway.stringify_list())

subway.remove_head()
subway.remove_tail()
print(subway.stringify_list())

subway.remove_by_value('Times Square')
print(subway.stringify_list())