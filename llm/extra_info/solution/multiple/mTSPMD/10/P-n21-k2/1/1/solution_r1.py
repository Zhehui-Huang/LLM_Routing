import math
import numpy as np
from scipy.spatial import distance_matrix

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def create_distance_matrix(cities):
    coords = np.array(cities)
    return distance_matrix(coords, coords)

def tsp_tour(cities, start_index, dist_matrix):
    from heapq import heappop, heappush

    # Total number of cities including the depot.
    n = len(cities)
    # Array to store the shortest path
    path = []
    # Use a min-heap to store (cost, vertex, path) tuples.
    heap = [(0, start_index, [start_index])]
    visited = set()

    while heap:
        (cost, vertex, path) = heappop(heap)
        if len(path) == n:
            # return to the start
            path.append(path[0])
            cost += dist_matrix[vertex][path[0]]
            return path, cost

        if vertex not in visited:
            visited.add(vertex)
            for i in range(n):
                if i not in visited:
                    heappush(heap, (cost + dist_matrix[vertex][i], i, path + [i]))

    # Should not reach here
    return None

# Coordinates of the cities
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), 
    (62, 63), (63, 69), (45, 35)
]

# Create a distance matrix
dist_matrix = create_distance_matrix(cities)

# Divide cities between two robots, here just splitting by index alternately
robot_0_cities = [0] + [i for i in range(2, len(cities), 2)] if i != 0]
robot_1_cities = [1] + [i for i in range(2, len(cities), 2)] if i != 1]

# Run TSP for each robot
robot_0_tour, robot_0_cost = tsp_tour(robot_0_cities, 0, dist_matrix[robot_0_cities][:, robot_0_cities])
robot_1_tour, robot_1_cost = tsp_tour(robot_1_cities, 0, dist_matrix[robot_1_cities][:, robot_1_cities])

# Translate local indices back to global indices
global_robot_0_tour = [robot_0_cities[i] for i in robot_0_tour]
global_robot_1_tour = [robot_1_cities[i] for i in robot_1_tour]

# Output results
print(f"Robot 0 Tour: {global_robot_0_tour}")
print(f"Robot 0 Total Travel Cost: {robot_0_cost}")
print(f"Robot 1 Tour: {global_robot_1_tour}")
print(f"Robot 1 Total Travel Cost: {robot_1_cost}")
print(f"Overall Total Travel Cost: {robot_0_cost + robot_1_cost}")