class TreeNode:
  def __init__(self, value):
    self.value = value
    self.children = []

  def __repr__(self, level=0):
    # helper method to print tree
    ret = "--->" * level + repr(self.value) + "\n"
    for child in self.children:
      ret += child.__repr__(level+1)
    return ret

  def add_child(self, child_node):
    self.children.append(child_node) 


class TreeNodeFull:
  def __init__(self, value):
    self.value = value
    self.children = []

  def __repr__(self, level=0):
    # helper method to print tree
    ret = "--->" * level + repr(self.value) + "\n"
    for child in self.children:
      ret += child.__repr__(level+1)
    return ret

  def add_child(self, child_node):
    # prevent adding a child node which already exists in self.children
    if child_node in self.children:
      return
    print("Adding " + child_node.value)
    self.children.append(child_node) 

  def remove_child(self, child_node):
    print("Removing " + child_node.value + " from " + self.value)
    self.children = [child for child in self.children if child != child_node]

  def traverse(self):
    print("Traversing...")
    # moves through each node referenced from self downwards
    nodes_to_visit = [self]
    while len(nodes_to_visit)>0:
      current_node = nodes_to_visit.pop()
      print(current_node.value)
      nodes_to_visit += current_node.children


# Choose-Your-Own-Adventure Game
# the flow:
# print out the story_node.story_piece.
# while story_node.choices has nodes inside…
# prompt the user for a choice.
# set story_node to be the user’s story choice.
# repeat until the story is over!
      
print('Once upon a time...')
######
# TREENODE CLASS
######
class TreeNode_game:
  def __init__(self, story_piece):
    self.story_piece = story_piece
    self.choices = []

  def add_child(self, node):
    self.choices.append(node)

  def traverse(self):
    story_node = self
    print(story_node.story_piece)
    while len(story_node.choices) > 0:
      choice = input('Enter 1 or 2 to continue the story:')
      if choice not in ['1', '2']:
        print('Please input 1 or 2.')
      chosen_index = int(choice) - 1
      chosen_child = story_node.choices[chosen_index]
      print(chosen_child.story_piece)
      story_node = chosen_child



story_root = TreeNode_game("""
You are in a forest clearing. There is a path to the left.
A bear emerges from the trees and roars!
Do you: 
1 ) Roar back!
2 ) Run to the left...
""")

user_choice = input('What is your name?')
print(user_choice)
######
# VARIABLES FOR TREE
######
# each node is a piece of story
choice_a = TreeNode_game("""
The bear is startled and runs away.
Do you:
1 ) Shout 'Sorry bear!'
2 ) Yell 'Hooray!'
""")

choice_b = TreeNode_game("""
You come across a clearing full of flowers. 
The bear follows you and asks 'what gives?'
Do you:
1 ) Gasp 'A talking bear!'
2 ) Explain that the bear scared you.
""")
# add two choices for a middle section of story line stored inside of story_root.choices
story_root.add_child(choice_a)
story_root.add_child(choice_b)

choice_a_1 = TreeNode_game("""
The bear returns and tells you it's been a rough week. After making peace with
a talking bear, he shows you the way out of the forest.

YOU HAVE ESCAPED THE WILDERNESS.
""")
choice_a_2 = TreeNode_game("""
The bear returns and tells you that bullying is not okay before leaving you alone
in the wilderness.

YOU REMAIN LOST.
""")

choice_b_1 = TreeNode_game("""
The bear is unamused. After smelling the flowers, it turns around and leaves you alone.

YOU REMAIN LOST.
"""
)
choice_b_2 = TreeNode_game("""
The bear understands and apologizes for startling you. Your new friend shows you a 
path leading out of the forest.

YOU HAVE ESCAPED THE WILDERNESS.
""")

choice_a.add_child(choice_a_1)
choice_a.add_child(choice_a_2)
choice_b.add_child(choice_b_1)
choice_b.add_child(choice_b_2)

######
# TESTING AREA
######
story_root.traverse()