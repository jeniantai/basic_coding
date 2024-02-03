from random import randrange

def swap(arr, index_1, index_2):
  temp = arr[index_1]
  arr[index_1] = arr[index_2]
  arr[index_2] = temp


def bubble_sort_unoptimized(arr):
  iteration_count = 0
  for el in arr:
    for index in range(len(arr) - 1):
      iteration_count += 1
      if arr[index] > arr[index + 1]:
        swap(arr, index, index + 1)
  return print("PRE-OPTIMIZED ITERATION COUNT: {0}".format(iteration_count))
    
# the optimized sort reduces the number of iterations in the inner loop, altho it doesnt improve the overall runtime
def bubble_sort(arr):
  iteration_count = 0
  for i in range(len(arr)):
    # iterate through unplaced elements
    for idx in range(len(arr) - i - 1):
      iteration_count += 1
      if arr[idx] > arr[idx + 1]:
        # replacement for swap function
        arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
        
  return print("POST-OPTIMIZED ITERATION COUNT: {0}".format(iteration_count))


def bubble_sort_books(arr, comparison_function):
  swaps = 0
  sorted = False
  while not sorted:
    sorted = True
    for idx in range(len(arr) - 1):
      if comparison_function(arr[idx], arr[idx + 1]):
        sorted = False
        arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
        swaps += 1
  print("Bubble sort: There were {0} swaps".format(swaps))
  return arr

def merge_sort(items):
  if len(items) <= 1:
    return items

  middle_index = len(items) // 2
  left_split = items[:middle_index]
  right_split = items[middle_index:]

  left_sorted = merge_sort(left_split)
  right_sorted = merge_sort(right_split)

  return merge(left_sorted, right_sorted)

# left and right lists must be sorted
def merge(left, right):
  result = []
  # while both left and right have elements
  while (left and right):
    if left[0] < right[0]:
      result.append(left[0])
      left.pop(0)
    else:
      result.append(right[0])
      right.pop(0)

  if left:
    result += left
  if right:
    result += right

  return result

# in-place implementaion of the quicksort, no additional memory is used
def quicksort(list, start, end):
  if start >= end:
    return list
  print("Running quicksort on {0}".format(list[start: end + 1]))
	# Define your pivot variables within start and end
  pivot_idx = randrange(start, end)
  pivot_element = list[pivot_idx]
  print("Selected pivot {0}".format(pivot_element))
  # Swap the elements in list below
  list[pivot_idx], list[end] = list[end], list[pivot_idx]
  # Create the lesser_than_pointer
  lesser_than_pointer = start
  # Check if the value at idx is less than the pivot
    # If so: 
      # 1) swap lesser_than_pointer and idx values
      # 2) increment lesser_than_pointer
  for idx in range(start, end):
    if list[idx] < pivot_element:
      print("Swapping {0} with {1}".format(list[idx], list[lesser_than_pointer]))
      list[idx], list[lesser_than_pointer] =  list[lesser_than_pointer], list[idx]
      lesser_than_pointer += 1
  # After the loop is finished...
  # swap pivot with value at lesser_than_pointer
  list[end], list[lesser_than_pointer] = list[lesser_than_pointer], list[end]
  print("{0} successfully partitioned".format(list[start: end + 1]))
  # print(list[start])
  # start += 1
  # return quicksort(list, start, end)

  # Call quicksort on the "left" and "right" sub-lists
  quicksort(list, start, lesser_than_pointer - 1)
  quicksort(list, lesser_than_pointer + 1, end)

# This implementation creates two new lists for each recursive call. 
# The new lists are eventually combined into a new list with values in sorted order.
def qs(arr):
  if len(arr) <= 1:
    return arr

  smaller = []
  larger = []
  
  pivot = 0
  pivot_element = arr[pivot]
  
  for i in range(1, len(arr)):
    if arr[i] > pivot_element:
      larger.append(arr[i])
    else:
      smaller.append(arr[i])

  sorted_smaller = qs(smaller)
  sorted_larger = qs(larger)

  return sorted_smaller + [pivot_element] + sorted_larger

def quicksort_books(list, start, end, comparison_function):
  if start >= end:
    return
  pivot_idx = randrange(start, end + 1)
  pivot_element = list[pivot_idx]
  list[end], list[pivot_idx] = list[pivot_idx], list[end]
  less_than_pointer = start
  for i in range(start, end):
    if comparison_function(pivot_element, list[i]):
      list[i], list[less_than_pointer] = list[less_than_pointer], list[i]
      less_than_pointer += 1
  list[end], list[less_than_pointer] = list[less_than_pointer], list[end]
  quicksort_books(list, start, less_than_pointer - 1, comparison_function)
  quicksort_books(list, less_than_pointer + 1, end, comparison_function)

import sys, os
parent = os.path.dirname(os.getcwd())
sys.path.append(parent)
from data_structure.trees import MaxHeap

def heapsort(lst):
  # create an empty list to store the root nodes
  sort = []
  max_heap = MaxHeap()
  for idx in lst:
    max_heap.add(idx)
  while max_heap.count > 0:
    max_value = max_heap.retrieve_max()
    sort.insert(0, max_value)
  return sort
