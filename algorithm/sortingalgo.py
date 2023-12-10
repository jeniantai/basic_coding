
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


def quicksort(list, start, end):
  if start >= end:
    return list
	# Define your pivot variables below
  pivot_idx = randrange(start, end)
  pivot_element = list[pivot_idx]
  # Swap the elements in list below
  list[pivot_idx], list[end] = list[end], list[pivot_idx]
  # Leave these lines for testing
  print(list[start])
  start += 1
  return quicksort(list, start, end)