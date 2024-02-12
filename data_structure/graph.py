
from random import randrange
from math import inf, sqrt
from heapq import heappop, heappush
class Vertex:
  """
  Responsible for knowing which other vertices are connected.
  """
  def __init__(self, value):
    self.value = value
    self.edges = {}

  def add_edge(self, vertex, weight = 0):
    self.edges[vertex] = weight

  def get_edges(self):
    return list(self.edges.keys())

  def get_edge_weight(self, edge): 
    return self.edges[edge]
  
class Graph:
  """
  Track all the vertices and handle higher level concerns like whether 
  the graph is directed, requiring edges to have a set direction, 
  or undirected, allowing bi-directional movement across edges.
  """
  def __init__(self, directed = False):
    self.graph_dict = {}
    self.directed = directed

  def add_vertex(self, vertex):
    print(f'Adding {vertex.value}')
    self.graph_dict[vertex.value] = vertex

  def add_edge(self, from_vertex, to_vertex, weight = 0):
    print(f'Adding edge from {from_vertex.value} to {to_vertex.value}')
    # these are add_edge in Vertex as self.graph_dict[from_vertex.value] is a Vertex
    self.graph_dict[from_vertex.value].add_edge(to_vertex.value, weight)
    if not self.directed:
      self.graph_dict[to_vertex.value].add_edge(from_vertex.value, weight)

  def find_path(self, start_vertex, end_vertex):
    # use this list to keep track of the vertices as we search
    start = [start_vertex]
    # seen is a dict to track which vertices we;ve already visited
    seen = {}
    while len(start) > 0:
      current_vertex = start.pop(0)
      seen[current_vertex] = True
      print("Visiting " + current_vertex)
      if current_vertex == end_vertex:
        return True
      else:
        vertices_to_visit = set(self.graph_dict[current_vertex].edges.keys())
        start += [vertex for vertex in vertices_to_visit if vertex not in seen]
    return False
  
def print_graph(graph):
  for vertex in graph.graph_dict:
    print("")
    print(vertex + " connected to")
    vertex_neighbors = graph.graph_dict[vertex].edges
    if len(vertex_neighbors) == 0:
      print("No edges!")
    for adjacent_vertex in vertex_neighbors:
      print("=> " + adjacent_vertex)


def build_graph(directed):
  g = Graph(directed)
  vertices = []
  for val in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
    vertex = Vertex(val)
    vertices.append(vertex)
    g.add_vertex(vertex)

  for v in range(len(vertices)):
    v_idx = randrange(0, len(vertices) - 1)
    v1 = vertices[v_idx]
    v_idx = randrange(0, len(vertices) - 1)
    v2 = vertices[v_idx]
    g.add_edge(v1, v2, randrange(1, 10))

  print_graph(g)


def grph_bfs(graph, start_vertex, target_value):
  path = [start_vertex]
  vertex_and_path = [start_vertex, path]
  bfs_queue = [vertex_and_path]
  visited = set()
  while bfs_queue:
    current_vertex, path = bfs_queue.pop(0)
    visited.add(current_vertex)
    for neighbor in graph[current_vertex]:
      if neighbor not in visited:
        if neighbor is target_value:
          return path + [neighbor]
        else:
          bfs_queue.append([neighbor, path + [neighbor]])

def grph_dfs(graph, current_vertex, target_value, visited = None):
  if visited is None:
    visited = []
  visited.append(current_vertex)
  # base case
  if current_vertex is target_value:
    return visited
  
  for neighbor in graph[current_vertex]:
    if neighbor not in visited:
      path = grph_dfs(graph, neighbor, target_value, visited)
      if path:
        return path

# a graph of all stations in the Vancouver metro system
vc_metro = {
  'Richmond-Brighouse': set(['Lansdowne']),
  'Lansdowne': set(['Richmond-Brighouse', 'Aberdeen']),
  'Aberdeen': set(['Lansdowne', 'Bridgeport']),
  'Bridgeport': set(['Aberdeen', 'Templeton', 'Marine Drive']),
  'YVR-Airport': set(['Sea Island Centre']),
  'Sea Island Centre': set(['YVR-Airport', 'Templeton']),
  'Templeton': set(['Sea Island Centre', 'Bridgeport']),
  'Marine Drive': set(['Bridgeport', 'Langara-49th Avenue']),
  'Langara-49th Avenue': set(['Marine Drive', 'Oakbridge-41st Avenue']),
  'Oakbridge-41st Avenue': set(['Langara-49th Avenue', 'King Edward']),
  'King Edward': set(['Oakbridge-41st Avenue', 'Broadway-City Hall']),
  'Broadway-City Hall': set(['King Edward', 'Olympic Village']),
  'Olympic Village': set(['Broadway-City Hall', 'Yaletown-Roundhouse']),
  'Yaletown-Roundhouse': set(['Olympic Village', 'Vancouver City Centre']),
  'Vancouver City Centre': set(['Yaletown-Roundhouse', 'Waterfront']),
  'Waterfront': set(['Vancouver City Centre', 'Burrard']),
  'Burrard': set(['Waterfront', 'Granville']),
  'Granville': set(['Burrard', 'Stadium-Chinatown']),
  'Stadium-Chinatown': set(['Granville', 'Main Street-Science World']),
  'Main Street-Science World': set(['Stadium-Chinatown', 'Commercial-Broadway']),
  'Commercial-Broadway': set(['VCC-Clark', 'Main Street-Science World', 'Renfrew', 'Nanaimo']),
  'VCC-Clark': set(['Commercial-Broadway']),
  'Nanaimo': set(['Commercial-Broadway', '29th Avenue']),
  '29th Avenue': set(['Nanaimo', 'Joyce-Collingwood']),
  'Joyce-Collingwood': set(['29th Avenue', 'Patterson']),
  'Patterson': set(['Joyce-Collingwood', 'Metrotown']),
  'Metrotown': set(['Patterson', 'Royal Oak']),
  'Royal Oak': set(['Metrotown', 'Edmonds']),
  'Edmonds': set(['Royal Oak', '22nd Street']),
  '22nd Street': set(['Edmonds', 'New Westminster']),
  'New Westminster': set(['22nd Street', 'Columbia']),
  'Columbia': set(['New Westminster', 'Sapperton', 'Scott Road']),
  'Scott Road': set(['Columbia', 'Gateway']),
  'Gateway': set(['Scott Road', 'Surrey Central']),
  'Surrey Central': set(['Gateway', 'King George']),
  'King George': set(['Surrey Central']),
  'Sapperton': set(['Columbia', 'Braid']),
  'Braid': set(['Sapperton', 'Lougheed Town Centre']),
  'Lougheed Town Centre': set(['Braid', 'Production Way / University', 'Burquitlam']),
  'Burquitlam': set(['Lougheed Town Centre', 'Moody Centre']),
  'Moody Centre': set(['Burquitlam', 'Inlet Centre']),
  'Inlet Centre': set(['Moody Centre', 'Coquitlam Central']),
  'Coquitlam Central': set(['Inlet Centre', 'Lincoln']),
  'Lincoln': set(['Coquitlam Central', 'Lafarge Lake-Douglas']),
  'Lafarge Lake-Douglas': set(['Lincoln']),
  'Production Way / University': set(['Lougheed Town Centre', 'Lake City Way']),
  'Lake City Way': set(['Production Way / University', 'Sperling / Burnaby Lake']),
  'Sperling / Burnaby Lake': set(['Lake City Way', 'Holdom']),
  'Holdom': set(['Sperling / Burnaby Lake', 'Brentwood Town Centre']),
  'Brentwood Town Centre': set(['Holdom', 'Gilmore']),
  'Gilmore': set(['Brentwood Town Centre', 'Rupert']),
  'Rupert': set(['Gilmore', 'Renfrew']),
  'Renfrew': set(['Rupert', 'Commercial-Broadway'])
  }

# a dictionary of Vancouver landmarks mapped to their nearest metro station(s)
vc_landmarks = {
  'Marine Building': set(['Burrard', 'Waterfront']),
  'Scotiabank Field at Nat Bailey Stadium': set(['King Edward']),
  'Vancouver Aquarium': set(['Burrard']),
  'Vancouver Lookout': set(['Waterfront']),
  'Canada Place': set(['Burrard', 'Waterfront']),
  'Cathedral of Our Lady of the Holy Rosary': set(['Vancouver City Centre', 'Granville']),
  'Library Square': set(['Vancouver City Centre', 'Stadium-Chinatown']),
  'B.C. Place Stadium': set(['Stadium-Chinatown']),
  'Lions Gate Bridge': set(['Burrard']),
  'Gastown Steam Clock': set(['Waterfront']),
  'Waterfront Station': set(['Waterfront']),
  'Granville Street': set(['Granville', 'Vancouver City Centre']),
  'Pacific Central Station': set(['Main Street-Science World']),
  'Prospect Point Lighthouse': set(['Burrard']),
  'Queen Elizabeth Theatre': set(['Stadium-Chinatown']),
  'Stanley Park': set(['Burrard']),
  'Granville Island Public Market': set(['Yaletown-Roundhouse']),
  'Kitsilano Beach': set(['Olympic Village']),
  'Dr. Sun Yat-Sen Classical Chinese Garden': set(['Stadium-Chinatown']),
  'Museum of Vancouver': set(['Yaletown-Roundhouse']),
  'Science World': set(['Main Street-Science World']),
  'Robson Square': set(['Vancouver City Centre']),
  'Samson V Maritime Museum': set(['Columbia']),
  'Burnaby Lake': set(['Sperling / Burnaby Lake', 'Lake City Way', 'Production Way / University']),
  'Nikkei National Museum & Cultural Centre': set(['Edmonds']),
  'Central Park': set(['Patterson', 'Metrotown'])
}

# a dictionary of letters of the alphabet mapped to landmarks to make it easier for users to make a selection
landmark_choices = {
  'a': 'Marine Building',
  'b': 'Scotiabank Field at Nat Bailey Stadium',
  'c': 'Vancouver Aquarium',
  'd': 'Vancouver Lookout',
  'e': 'Canada Place',
  'f': 'Cathedral of Our Lady of the Holy Rosary',
  'g': 'Library Square',
  'h': 'B.C. Place Stadium',
  'i': 'Lions Gate Bridge',
  'j': 'Gastown Steam Clock',
  'k': 'Waterfront Station',
  'l': 'Granville Street',
  'm': 'Pacific Central Station',
  'n': 'Prospect Point Lighthouse',
  'o': 'Queen Elizabeth Theatre',
  'p': 'Stanley Park',
  'q': 'Granville Island Public Market',
  'r': 'Kitsilano Beach',
  's': 'Dr. Sun Yat-Sen Classical Chinese Garden',
  't': 'Museum of Vancouver',
  'u': 'Science World',
  'v': 'Robson Square',
  'w': 'Samson V Maritime Museum',
  'x': 'Burnaby Lake',
  'y': 'Nikkei National Museum & Cultural Centre',
  'z': 'Central Park'
}



def dijkstras(graph, start):
  distances = {}
  for vertex in graph:
    distances[vertex] = inf
    distances[start] = 0
  # the first tuple represents the start vertex within the min-heap list
  vertices_to_explore = [(0, start)]
  while vertices_to_explore:
    # this will always be the ertex with the min distance from start
    current_distance, current_vertex = heappop(vertices_to_explore)
    
    for neighbor, edge_weight in graph[current_vertex]:
      new_distance = current_distance + edge_weight
      if new_distance < distances[neighbor]:
        distances[neighbor] = new_distance
        heappush(vertices_to_explore, (new_distance, neighbor))

  return distances

def build_tsp_graph(directed):
  g = Graph(directed)
  vertices = []
  for val in ['a', 'b', 'c', 'd']:
    vertex = Vertex(val)
    vertices.append(vertex)
    g.add_vertex(vertex)

  g.add_edge(vertices[0], vertices[1], 3)
  g.add_edge(vertices[0], vertices[2], 4)
  g.add_edge(vertices[0], vertices[3], 5)
  g.add_edge(vertices[1], vertices[0], 3)
  g.add_edge(vertices[1], vertices[2], 2)
  g.add_edge(vertices[1], vertices[3], 6)
  g.add_edge(vertices[2], vertices[0], 4)
  g.add_edge(vertices[2], vertices[1], 2)
  g.add_edge(vertices[2], vertices[3], 1)
  g.add_edge(vertices[3], vertices[0], 5)
  g.add_edge(vertices[3], vertices[1], 6)
  g.add_edge(vertices[3], vertices[2], 1)
  return g

# helper function that checks whether all of the vertices in the graph have been visited or not
def visited_all_nodes(visited_vertices):
  for vertex in visited_vertices:
    if visited_vertices[vertex] == "unvisited":
      return False
  return True

import random

def traveling_salesperson(graph):
  ts_path = ""
  visited_vertices = {x: "unvisited" for x in graph.graph_dict}
  current_vertex = random.choice(list(graph.graph_dict))
  visited_vertices[current_vertex] = "visited"
  ts_path += current_vertex
  visited_all_vertices = visited_all_nodes(visited_vertices)
  while not visited_all_vertices:
    current_vertex_edges = graph.graph_dict[current_vertex].get_edges()
    current_vertex_edge_weights = {}
    for edge in current_vertex_edges:
      current_vertex_edge_weights[edge] = graph.graph_dict[current_vertex].get_edge_weight(edge)

    found_next_vertex = False
    next_vertex = ""
    while not found_next_vertex:
      if current_vertex_edge_weights is None:
        break
      next_vertex = min(current_vertex_edge_weights, key=current_vertex_edge_weights.get)
      if visited_vertices[next_vertex] == "visited":
        current_vertex_edge_weights.pop(next_vertex)
      else:
        found_next_vertex = True

    if current_vertex_edge_weights is None:
      visited_all_vertices = True
    else:
      current_vertex = next_vertex
      visited_vertices[current_vertex] = "visited"
      ts_path += current_vertex

    visited_all_vertices = visited_all_nodes(visited_vertices)

  print(ts_path)



def modified_dijkstras(graph, start, target):
  paths_and_distances = {}
  for vertex in graph:
    paths_and_distances[vertex] = [inf, [start.name]]
  
  paths_and_distances[start][0] = 0
  vertices_to_explore = [(0, start)]

  while vertices_to_explore:
    current_distance, current_vertex = heappop(vertices_to_explore)
    for neighbor, edge_weight in graph[current_vertex]:
      new_distance = current_distance + edge_weight
      new_path = paths_and_distances[current_vertex][1] + [neighbor.name]
      if new_distance < paths_and_distances[neighbor][0]:
        paths_and_distances[neighbor][0] = new_distance
        paths_and_distances[neighbor][1] = new_path
        heappush(vertices_to_explore, (new_distance, neighbor))
  
  return paths_and_distances[target][1]

# A graph and vertices for midufued_dijkstras:
class graph_vertex:
  def __init__(self, name, x, y):
    self.name = name
    self.position = (x, y)

# Manhattan heuristic is only considered admissible — 
# meaning that it never overestimates the distance in reaching the target — 
# in a grid system in which the search can only move up, down, left, or right.
def man_heuristic(start, target):
  x_distance = abs(start.position[0] - target.position[0])
  y_distance = abs(start.position[1] - target.position[1])
  return x_distance + y_distance

def euc_heuristic(start, target):
  x_distance = abs(start.position[0] - target.position[0])
  y_distance = abs(start.position[1] - target.position[1])
  return sqrt(x_distance**2 + y_distance**2)


def a_star(graph, start, target):
  print("Starting A* algorithm!")
  count = 0
  paths_and_distances = {}
  for vertex in graph:
    paths_and_distances[vertex] = [inf, [start.name]]
  
  paths_and_distances[start][0] = 0
  vertices_to_explore = [(0, start)]
  while vertices_to_explore and paths_and_distances[target][0] == inf:
    current_distance, current_vertex = heappop(vertices_to_explore)
    for neighbor, edge_weight in graph[current_vertex]:
      new_distance = current_distance + edge_weight + man_heuristic(neighbor, target)
      new_path = paths_and_distances[current_vertex][1] + [neighbor.name]
      
      if new_distance < paths_and_distances[neighbor][0]:
        paths_and_distances[neighbor][0] = new_distance
        paths_and_distances[neighbor][1] = new_path
        heappush(vertices_to_explore, (new_distance, neighbor))
        count += 1
        print("\nAt " + vertices_to_explore[0][1].name)
        
  print("Found a path in {0} steps: ".format(count), paths_and_distances[target][1])
  
  return paths_and_distances[target][1]