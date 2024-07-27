import numpy as no
from scipy.spatial.distance import euclidean
from itertools import permutations

# Coordinates of the cities (indexed by city ID)
cities = {
    0: (145, 215),  # Depot
    1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252),
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239),
    9: (163, 236), 10: (148, 232), 11: (128, 231), 12: (156, 217),
    13: (129, 214), 14: (146, 208), 15: (164, 208), 16: (141, 206),
    17: (147, 193), 18: (164, 193), 19: (129, 189), 20: (155, 185),
    21: (139, 182)
}

# Number of robots
num_robots = 4

# Function to calculate Euclidean distance between two cities
def calculate_distance(city1_id, city2_id):
    return euclidean(cities[city1_id], cities[city2_id])

# Create greedy tours based on nearest neighbor heuristic
def create_tour(start_city, unvisited_cities):
    tour = [start_city]
    current_city = start_city
    while unvisited_cities:
        next_city = min(unvisited_cities, key=lambda city: calculate_distance(current_city, city))
        unvisited_cities.remove(next_city)
        tour.append(next_city)
        current_city = next_city
    tour.append(start_city)
    return tour

# Calculate travel cost of a tour
def tour_cost(tour):
    return sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Function to divide cities into roughly equal parts
def divide_cities(n, num_groups):
    avg = n / float(num_groups)
    out = []
    last = 0.0
    while last < n:
        out.append(int(last))
        last += avg
    return out

# Divide cities amongst robots
city_ids = list(cities.keys())[1:]  # exclude the depot for initial assignment
boundaries = divide_cities(len(city_ids), num_robots)
robot_tours = [city_ids[boundaries[i]:boundaries[i+1]] for i in range(num_robots)]

# Construct tours including returns to the depot (0)
final_tours = []
total_cost = 0

for robot_id, cities_in_tour in enumerate(robot_tours):
    tour = [0] + cities_in_tour + [0]
    optimized_tour = create_tour(0, cities_in_t very_base(except the depot))
    final_tours.append(optimized_t our)
    cost = tour_cost(optimized_tour)
    total_cost += cost
    print(f"Robot {robot_id} Tour: {optimized_tour}")
    print(f"Robot {robot_id} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_cost}")