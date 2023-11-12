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


# Linear - O(N), where "N" is the number of digits in the number
def sum_digits(n):
  if n < 0:
    ValueError("Inputs 0 or greater only!")
  result = 0
  while n is not 0:
    result += n % 10
    n = n // 10
  return result + n

# sum_digits recursively
def sum_digits2(n):
  if n < 0:
    ValueError("Inputs 0 or greater only!")
  if n <= 9:
    return n
  last_digit = n % 10
  return sum_digits(n // 10) + last_digit


# O(N)
def find_min(my_list):
  min = None
  for element in my_list:
    if not min or (element < min):
      min = element
  return min

# find_min recursively
def find_min2(my_list, min = None):
  # if input is an empty list, return min
  if not my_list:
    return min
  # if min is None OR first element of list is < min
  if not min or my_list[0] < min:
    min = my_list[0]
  return find_min(my_list[1:], min)

# Palindromes are words which read the same forward and backward.
# In each iteration of the loop that doesn’t return False, we make a copy of the string with two fewer characters.
# Copying a list of N elements requires N amount of work in big O >> O(N^2)
def is_palindrome(str):
  while len(str) > 1:
    if str[0] != str[-1]:
      return False
    str = str[1:-1]
  return True 

# A more efficient version: Linear - O(N)
def is_palindrome1(str):
  str_length = len(str)
  middle_index = str_length // 2
  for index in range(0, middle_index):
    opposite_character_index = str_length - index - 1
    if str[index] != str[opposite_character_index]:
      return False  
  return True

# using recursive calls
def is_palindrome3(str):
  if len(str) < 2:
    return True
  if str[0] != str[-1]:
    return False
  return is_palindrome(str[1:-1])


# O(N)
def factorial(n):
  if n < 0:
    ValueError('Inputs 0 or greater only.')
  if n <= 1:
    return 1
  return n*factorial(n-1)


# lets rewrite factorial iteratively
def factorial_iter(n):
  if n < 0:
    ValueError('Inputs 0 or greater only.')
  if n <= 1:
    return 1
  
  result = 1
  while n != 1:
     result *= n
     n -= 1
  return result



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
# runtime: Exponential - O(2^N)
def fibonacci(n):
  # base cases
  if n < 0:
    ValueError('Inputs 0 or greater only.')
  if n < 2:
    return n
  
  # recursive step
  # note there are quite a bit of repeated function calls with the same input. This contributes to the expensive runtime
  print("Recursive call with {0} as input".format(n))
  return fibonacci(n - 1) + fibonacci(n - 2)

# fibonacci the iterative way
def fibonacci1(n):
  if n < 0:
    ValueError("Input 0 or greater only!")

  fibs = [0, 1]
  
  if n <= len(fibs) - 1:
    return fibs[n]
  
  while n > len(fibs) - 1:
    fibs.append(fibs[-1] + fibs[-2])
    
  return fibs[-1]





# Since the problem is that we re-compute values we have already computed, 
# we can instead choose to save the values we have already computed in a dict, 
# This is called memoization.
# Python 3 includes a decorator to do this - automatic memoization!
import functools
@functools.lru_cache(None)
def fibonacci2(n):
  if n < 0:
    ValueError('Inputs 0 or greater only.')
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