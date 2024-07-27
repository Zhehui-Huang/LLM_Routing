import math
from typing import List, Tuple

# Coordinates of the cities
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

# Number of robots
num_robots = 4

def euclidean_distance(p1: Tuple[int, int], p2: Tuple[int, int]) -> float:
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Calculate the distances matrix
distances = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))]

def nearest_neighbor_tour(start: int, unvisited: List[int]) -> List[int]:
    tour = [start]
    current = start
    while unvisited:
        next_city = min(unvisited, key=lambda x: distances[current][x])
        unvisited.remove(next_city)
        tour.append(next_city)
        current = next_city
    tour.append(start)  # return to depot
    return tour

def calculate_tour_cost(tour: List[int]) -> float:
    return sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Divide cities into clusters for each robot
cities = list(range(1, len(coordinates)))  # excluding depot
clusters = [cities[i::num_robots] for i in range(num_robots)]

# Solve TSP for each cluster
tours = []
total_costs = []

for i in range(num_robots):
    cluster = clusters[i]
    tour = nearest_neighbor_tour(0, cluster[:])  # each robot starts from the depot
    tour_cost = calculate_tour_cost(tour)
    tours.append(tour)
    total_costs.append(tour_cost)

overall_total_cost = sum(total_costs)

# Print the solution
for i in range(num_robots):
    print(f"Robot {i} Tour: {tours[i]}")
    print(f"Robot {i} Total Travel Cost: {total_costs[i]}")

print(f"Overall Total Travel Cost: {overall_total_cost}")