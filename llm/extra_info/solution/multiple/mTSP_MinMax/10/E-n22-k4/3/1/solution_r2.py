import math
from scipy.spatial import distance_matrix

# Define cities and coordinates
coords = [(145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247), 
          (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231), 
          (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193), 
          (164, 193), (129, 189), (155, 185), (139, 182)]
num_robots = 4
num_cities = len(coords)

# Calculate distance matrix
dist_matrix = distance_matrix(coords, coords)

# Function to perform a simple nearest neighbor TSP algorithm
def nearest_neighbor_tsp(start_city, cities, dist_matrix):
    tour = [start_city]
    current_city = start_city
    while len(cities) > 0:
        next_city = min(cities, key=lambda city: dist_matrix[current_city, city])
        tour.append(next_city)
        cities.remove(next_city)
        current_city = next_city
    tour.append(start_city)  # return to the depot
    return tour

# Distribute cities to robots
cities_per_robot = (num_cities - 1) // num_robots
assignments = []
start_index = 1  # Starting from city 1 since city 0 is the depot
for i in range(num_robots):
    end_index = start_index + cities_per_robot
    if i < (num_cities - 1) % num_robots:
        end_index += 1
    assignments.append(set(range(start_index, end_index)))
    start_index = end_index

tours = []
travel_costs = []

# Robots compute their tours
for i in range(num_robots):
    assignment = list(assignments[i])
    tour = nearest_neighbor_tsp(0, assignment, dist_matrix)
    cost = sum(dist_matrix[tour[i], tour[i+1]] for i in range(len(tour) - 1))
    tours.append(tour)
    travel_costs.append(cost)
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost:.2f}")

# Find the maximum distance any single robot traveled
max_travel_cost = max(travel_costs)
print(f"Maximum Travel Cost: {max_travel_cost:.2f}")