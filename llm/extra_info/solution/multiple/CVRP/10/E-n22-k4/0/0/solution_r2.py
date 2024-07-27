import numpy as np
from scipy.spatial import distance_matrix
from collections import defaultdict

# Coordinates and demands
coordinates = [(145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
               (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
               (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
               (164, 193), (129, 189), (155, 185), (139, 182)]
demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600, 1200,
           1300, 1300, 300, 900, 210Share0, 1000, 900, 2500, 1800, 700]

# Number of robots and their capacity
num_robots = 4
robot_capacity = 6000

# Calculate the distance matrix
dist_matrix = distance_matrix(coordinates, coordinates)

# Assign cities to robots based on capacity
assignments = defaultdict(list)
capacities = defaultdict(int)
for city, demand in sorted(enumerate(demands[1:], start=1), key=lambda x: -x[1]):
    for robot in range(num_robots):
        if capacities[robot] + demand <= robot_capacity:
            assignments[robot].append(city)
            capacities[robot] += demand
            break
    else:
        raise Exception(f"Unable to assign city {city} with demand {demand} to any robot.")

# Function to find a TSP route via a greedy nearest neighbor approach
def greedy_tsp(assigned_cities, dist_matrix):
    tour = [0]  # starts at the depot
    visited = set(assigned_cities)
    while visited:
        current = tour[-1]
        next_city = min(visited, key=lambda x: dist_matrix[current, x])
        tour.append(next_city)
        visited.remove(next_city)
    tour.append(0)  # returns to the depot
    return tour

# Calculate routes and costs
overall_total_cost = 0
for robot, cities in assignments.items():
    tour = greedy_tsp(cities, dist_matrix)
    tour_cost = sum(dist_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))
    overall_total_cost += tour_cost
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {tour_cost:.2f}")

print(f"Overall Total Travel Cost: {overall_total_cost:.2f}")