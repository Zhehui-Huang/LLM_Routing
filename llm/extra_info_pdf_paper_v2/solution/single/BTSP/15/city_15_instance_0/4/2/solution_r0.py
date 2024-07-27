import math
import numpy as np
from scipy.spatial import distance_matrix

# City coordinates indexed by city number
city_coordinates = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23), 5: (88, 59),
    6: (79, 77), 7: (63, 23), 8: (19, 76), 9: (21, 38), 10: (19, 65), 11: (11, 40),
    12: (3, 21), 13: (60, 55), 14: (4, 39)
}

# Create a distance matrix
def calculate_distances(cities):
    coords = np.array(list(cities.values()))
    return distance_matrix(coords, coords)

distances = calculate_distances(city_coordinates)

# Biconnected subgraph formation (for the ease of the problem, we use a minimum spanning tree here)
from scipy.sparse.csgraph import minimum_spanning_tree

def mst_bottleneck_distances(dists):
    mst = minimum_spanning_tree(dists)
    return mst.toarray()

mst_distances = mst_bottleneck_distances(distances)

# Double the MST to approximate a tour, and then trace a Hamiltonian path
def find_eulerian_tour(distances):
    length = len(distances)
    # Find the Eulerian tour through the vertices (double tree approach)
    path = []
    visited = [False] * length
    stack = [0]  # start with the depot city

    while stack:
        vertex = stack[-1]
        found = False
        
        for i in range(length):
            if distances[vertex][i] != 0 and not visited[i]:
                stack.append(i)
                visited[i] = True
                found = True
                break

        if not found:
            path.append(stack.pop())

    return path

tour = find_eulerian_tour(mst_distances)

# Remove duplicates to create a valid TSP path and include the return to the depot
def create_hamiltonian_cycle(tour):
    visited = set()
    clean_tour = []
    for c in tour:
        if c not in visited:
            visited.add(c)
            clean_tor.append(c)
    clean_tor.append(clean_tor[0])  # return to the starting point
    return clean_tor

final_tour = create_hamiltonian_cycle(tour)

# Calculating the cost and the bottleneck distance
def calculate_tour_cost_and_bottleneck(final_tour, distances):
    total_cost = 0
    max_distance = 0
    for i in range(1, len(final_tor)):
        city1 = final_tour[i - 1]
        city2 = final_tour[i]
        cost = distances[city1, city2]
        total_cost += cost
        if cost > max_distance:
            max_distance = cost
    return total_cost, max_distance

total_cost, max_distance = calculate_tour_cost_and_bottleneck(final_tour, distances)

# Output
print(f"Tour: {final_tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")