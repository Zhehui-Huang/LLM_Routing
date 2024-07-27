import math
from scipy.spatial.distance import pdist, squareform

# Define cities and their coordinates
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35)
]

# Calculating pairwise distances between cities
distance_matrix = squareform(pdist(cities))

def nearest_neighbor_tour(start, visited):
    n = len(distance_matrix)
    tour = [start]
    current = start
    while len(tour) < n:
        visited[current] = True
        # Find the nearest unvisited city
        next_city = min(
            (i for i in range(n) if not visited[i]),
            key=lambda i: distance_matrix[current][i], default=None
        )
        
        # If no unvisited cities are left, break
        if next_city is None:
            break
        
        tour.append(next_city)
        current = next_city
    
    return tour

# Assign tours to robots starting from two different depots
visited = [False] * len(cities)
robot0_tour = nearest_neighbor_tour(0, visited.copy())
robot1_tour = nearest_neighbor_tour(1, visited.copy())  # Assign cities not visited by robot 0

def calculate_tour_cost(tour):
    return sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

robot0_cost = calculate_tour_cost(robot0_tour)
robot1_cost = calculate_tour_cost(robot1_tour)

# Output results
print(f"Robot 0 Tour: {robot0_tour}")
print(f"Robot 0 Total Travel Cost: {round(robot0_cost, 2)}")

print(f"Robot 1 Tour: {robot1_tour}")
print(f"Robot 1 Total Travel Cost: {round(robot1_cost, 2)}")

overall_cost = robot0_cost + robot1_cost
print(f"Overall Total Travel Cost: {round(overall_cost, 2)}")