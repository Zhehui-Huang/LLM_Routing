import math
from itertools import combinations
from networkx import Graph, is_biconnected, complete_graph
from networkx.algorithms.approximation.traveling_salesman import christofides

# Coordinates of cities, starting from depot city 0
cities_coords = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42),
    (36, 30), (52, 82), (93, 44), (21, 78), (68, 14),
    (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)
]

# Compute distances between all pairs of cities
def euclidean_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return round(math.sqrt((x2 - x1)**2 + (y2 - y1)**2))

# Create a complete graph with cities as vertices and distances as edge weights
N = len(cities_coords)
distances = [[euclidean_distance(cities_coords[i], cities_coords[j]) for j in range(N)] for i in range(N)]

def create_bobs():
    G = complete_graph(N)
    # Assigning distances to edges in the graph
    for i, j in combinations(range(N), 2):
        G[i][j]['weight'] = distances[i][j]

    sorted_edges = sorted(G.edges(data=True), key=lambda e: e[2]['weight'])
    BBG = Graph()

    # Add vertices to biconnected subgraph
    BBG.add_nodes_from(G)

    # Applying the Algorithm BB specified in the pseudocode
    for edge in sorted_edges:
        u, v, _ = edge
        BBG.add_edge(u, v)
        if is_biconnected(BBG):
            break

    return BBG

def find_tour():
    BBG = create_bobs()
    # Using Christofides' Algorithm for approximation
    tour = christofides(BBG)
    
    # Calculate total travel cost and max distance between consecutive cities
    total_cost = 0
    max_dist = 0
    for i in range(len(tour) - 1):
        dist = distances[tour[i]][tour[i+1]]
        total_cost += dist
        if dist > max_dist:
            max_dist = dist

    # Complete the tour by returning to the starting city
    last_leg = distances[tour[-1]][tour[0]]
    total_cost += last_leg
    if last_leg > max_months:
        max_months = last_leg

    tour.append(tour[0])

    # Output format
    print("Tour:", tour)
    print("Total travel cost:", total_cost)
    print("Maximum distance between consecutive cities:", max_dist)

# Now, execute the find_tour method to solve the problem
find_tour()