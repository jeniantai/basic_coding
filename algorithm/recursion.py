# To depict the steps of a recursive function, we’ll use a call stack and execution contexts for each function call.
# The call stack stores each function (with its internal variables) until those functions resolve in a last in, first out order.

def sum_to_one_iter(n):
  result = 1
  call_stack = []
  # loop of recursive calls which lead to a base case.
  while n != 1:
    execution_context = {'n_value': n}
    # push the recusive function calls onto the system's call stack
    call_stack.append(execution_context)
    n -= 1
    print(call_stack)
  print('BASE CASE REACHED')

  while len(call_stack) != 0:
    return_value = call_stack.pop()
    # see how execution contexts are removed from call stack
    print(call_stack)
    print("Return value of {0} adding to result {1}".format(return_value['n_value'], result))
    result += return_value['n_value']

  return result, call_stack




# Now lets create a truly recusive function
def sum_to_one_recur(n):
  if n == 1:
    return n
  # help visualize
  print("Recursing with input: {0}".format(n))
  # return argument + recursive_call(argument - 1)
  return n + sum_to_one_recur(n - 1)



def factorial(n):
  if n <= 1:
    return 1
  return n*factorial(n-1)




def power_set(my_list):
    # base case: an empty list
    if len(my_list) == 0:
        return [[]]
    # recursive step: subsets without first element
    power_set_without_first = power_set(my_list[1:])
    # subsets with first element
    with_first = [[my_list[0]] + rest for rest in power_set_without_first]
    # return combination of the two
    return with_first + power_set_without_first
  


def flatten(my_list):
  result = []
  for i in my_list:
    if isinstance(i, list):
      print('List found!')
      flat_list = flatten(i)
      result += flat_list
    else:
      result.append(i)
  return result




# Multiple recursive calls
def fibonacci(n):
  # base cases
  if n < 2:
    return n
  
  # recursive step
  # note there are quite a bit of repeated function calls with the same input. This contributes to the expensive runtime
  print("Recursive call with {0} as input".format(n))
  return fibonacci(n - 1) + fibonacci(n - 2)



# Since the problem is that we re-compute values we have already computed, 
# we can instead choose to save the values we have already computed in a dict, 
# This is called memoization.
# Python 3 includes a decorator to do this - automatic memoization!
import functools
@functools.lru_cache(None)
def fibonacci2(n):
    if n < 2:
        return n
    print("Recursive call with {0} as input".format(n))
    return fibonacci2(n-1) + fibonacci2(n-2)



# construct a binary search tree
def build_bst(my_list):
  # base case
  if len(my_list) == 0:
    return 'No Child'
  # recursive step
  middle_idx = len(my_list)//2
  middle_value = my_list[middle_idx]
  # my_list.pop()
  print('Middle index: {}'.format(middle_idx))
  print('Middle value: {}'.format(middle_value))
  # this tree should sprawl across all elements of the list
  tree_node = {'data': middle_value}
  # since data key will store the middle value, we shall exclude it in the branches
  tree_node['right_child'] = build_bst(my_list[middle_idx+1:])
  tree_node['left_child'] = build_bst(my_list[:middle_idx])
  # As the recursive calls resolve and pop off the call stack, the final return value 
  # will be the root or “top” tree_node which contains a reference to every other tree_node
  return tree_node