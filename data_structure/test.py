from linkedlist import *
from queues_stacks_hashmaps import Queue, Stack, HashMap, HashMap_LL

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

## Test DoublyLinkedList class
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

## Test Queue class
print("Creating a deli line with up to 10 orders...\n------------")
deli_line = Queue(10)
print("Adding orders to our deli line...\n------------")
deli_line.enqueue("egg and cheese on a roll")
deli_line.enqueue("bacon, egg, and cheese on a roll")
deli_line.enqueue("toasted sesame bagel with butter and jelly")
deli_line.enqueue("toasted roll with butter")
deli_line.enqueue("bacon, egg, and cheese on a plain bagel")
deli_line.enqueue("two fried eggs with home fries and ketchup")
deli_line.enqueue("egg and cheese on a roll with jalapeos")
deli_line.enqueue("plain bagel with plain cream cheese")
deli_line.enqueue("blueberry muffin toasted with butter")
deli_line.enqueue("bacon, egg, and cheese on a roll")
deli_line.enqueue("western omelet with home fries")
# ------------------------ #
print("------------\nOur first order will be " + deli_line.peek())
print("------------\nNow serving...\n------------")
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
# ------------------------ #
# Uncomment the line below:
deli_line.dequeue()
# ------------------------ #

## Test Stack class
pizza_stack = Stack(6)
# Adding pizzas as they are ready until we have 
pizza_stack.push("pizza #1")
pizza_stack.push("pizza #2")
pizza_stack.push("pizza #3")
pizza_stack.push("pizza #4")
pizza_stack.push("pizza #5")
pizza_stack.push("pizza #6")
pizza_stack.push("pizza #7")
# Delivering pizzas from the top of the stack down
print("The first pizza to deliver is " + pizza_stack.peek())
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()

## Test HashMap class
hash_map = HashMap(20)
hash_map.assign('gneiss', 'metamorphic')
print(hash_map.retrieve('gneiss'))  

hash_map = HashMap(15)

hash_map.assign('gabbro', 'igneous')
hash_map.assign('sandstone', 'sedimentary')
hash_map.assign('gneiss', 'metamorphic')

print(hash_map.retrieve('gabbro'))
print(hash_map.retrieve('sandstone'))
print(hash_map.retrieve('gneiss'))


flower_definitions = [['begonia', 'cautiousness'], ['chrysanthemum', 'cheerfulness'], ['carnation', 'memories'], 
                      ['daisy', 'innocence'], ['hyacinth', 'playfulness'], ['lavender', 'devotion'], ['magnolia', 'dignity'], 
                      ['morning glory', 'unrequited love'], ['periwinkle', 'new friendship'], ['poppy', 'rest'], ['rose', 'love'], 
                      ['snapdragon', 'grace'], ['sunflower', 'longevity'], ['wisteria', 'good luck']]

blossom = HashMap_LL(len(flower_definitions))
for flower in flower_definitions:
  blossom.assign(flower[0], flower[1])
print(blossom.retrieve('daisy'))
