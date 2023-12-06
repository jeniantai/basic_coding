# Naive Search
# The algorithm begins by iterating through the text and setting a variable match_count equal to 0.
# Then, for each index of the text, the algorithm iterates through the pattern to check for 
# matching characters, and if found, increments match_count. Otherwise, the search breaks the 
# pattern iteration and moves onto the next index in text.
# Each time the pattern iteration is completed, the match_count is compared to the length of 
# the pattern to determine if a match is found.
def pattern_search(text, pattern):
  print("Input Text:", text, "Input Pattern:", pattern)
  for index in range(len(text)):
    print("Text Index:", index)
    match_count = 0
    for char in range(len(pattern)):
      print("Pattern Index:", char)
      if pattern[char] == text[index + char]:
        print("Matching index found")
        print("Match Count:", match_count)
        match_count += 1
      # it doesn’t make sense to continue counting if a match doesn’t exist
      else:
        break
    if match_count == len(pattern):
      print(pattern, "found at index", index)


def pattern_search2(text, pattern, case_sensitive=True):
  for index in range(len(text)):
    match_count = 0
    for char in range(len(pattern)): 
      if case_sensitive and pattern[char] == text[index + char]:
        match_count += 1
      elif not case_sensitive and pattern[char].lower() == text[index + char].lower(): 
        match_count += 1
      else:
        break
    if match_count == len(pattern):
      print(pattern, "found at index", index)


def pattern_search3(text, pattern, replacement, case_sensitive=True):
  fixed_text = ""
  num_skips = 0

  for index in range(len(text)):

    if num_skips > 0:
      num_skips -= 1
      # skipping remaining code and jumps to next iteration ie index
      continue

    match_count = 0

    for char in range(len(pattern)): 
      if case_sensitive and pattern[char] == text[index + char]:
        match_count += 1
      elif not case_sensitive and pattern[char].lower() == text[index + char].lower(): 
        match_count += 1
      else:
        break

    if match_count == len(pattern):
      print(pattern, "found at index", index)
      fixed_text += replacement
      num_skips = len(pattern)-1
    else:
      fixed_text += text[index]

  return fixed_text

def linear_search(search_list, target_value):
  for idx in range(len(search_list)):
    # print(search_list[idx])
    if search_list[idx] == target_value:
      return idx
  raise ValueError("{0} not in list".format(target_value))

# search that handles duplicates
def linear_search_all(search_list, target_value):
  matches = []
  for idx in range(len(search_list)):
    if search_list[idx] == target_value:
      matches.append(idx)
  if matches:
    return matches
  else:
    raise ValueError("{0} not in list".format(target_value))
  
# search max value the linear way
def linear_search_max(search_list):
  maximum_score_index = None
  for idx in range(len(search_list)):
    # if maximum_score_index is not None or it's value is smaller than the current index value
    if not maximum_score_index or search_list[idx] > search_list[maximum_score_index]:
      maximum_score_index = idx
  return maximum_score_index
