import math
import random

# City coordinates
city_coords = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69),
    16: (38, 46),
    17: (61, 33),
    18: (62, 63),
    19: (63, 69),
    20: (45, 35)
}

# Euclidean distance calculator
def distance(city1, city2):
    x1, y1 = city_coords[city1]
    x2, y2 = city_coords[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Nearest Neighbour Search initialization
def nearest_neighbor_tour(start_city, cities):
    tour = [start_city]
    current_city = start_city
    remaining_cities = set(cities) - {start_city}
    
    while remaining_cities:
        next_city = min(remaining_cities, key=lambda city: distance(current_city, city))
        tour.append(next_city)
        remaining_cities.remove(next_city)
        current_city = next_city
        
    return tour

# Split the cities evenly among robots
def split_cities_for_robots(num_robots, cities):
    random.shuffle(cities)  # To add a bit of randomness
    return [cities[i::num_robots] for i in range(num_robots)]

# Assign initial tours for Robots
num_robots = 2
robot_tours = {}
cities = list(range(2, 21))  # cities from 2 to 20 (excluding depots)
city_groups = split_cities_for_robots(num_robots, cities)

for i in range(num_robots):
    start_depot = 0  # All robots start at depot 0
    tour = nearest_neighbor_tour(start_depot, [start_depot] + city_groups[i])
    robot_tours[i] = tour

# Calculate travel cost
def calculate_tour_cost(tour):
    return sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Print solution
total_cost = 0
for robot_id, tour in robot_tours.items():
    cost = calculate_tour_cost(tour)
    total_cost += cost
    print(f"Robot {robot_code} Tour: {tour[:-1]} -> {tour[-1]}")
    print(f"Robot {robot_id} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_cost}")