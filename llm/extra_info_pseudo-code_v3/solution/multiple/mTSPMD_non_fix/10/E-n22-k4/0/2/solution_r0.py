import math
import random
from itertools import permutations

# Coordinates and configuration
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 
    4: (128, 252), 5: (163, 247), 6: (146, 246), 7: (161, 242), 
    8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231), 
    12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208), 
    16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

num_robots = 4
robots = range(num_robots)

def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Nearest Neighbor Search (NNS) for initial solutions
def nearest_neighbor_solution(starting_city):
    remaining_cities = set(cities.keys()) - {starting_city}
    tour = [starting_city]
    current_city = starting_city

    while remaining_cities:
        next_city = min(remaining_cities, key=lambda city: calculate_distance(current_city, city))
        tour.append(next_city)
        remaining_cities.remove(next_city)
        current_city = next_city

    return tour

# Get initial solutions for each robot
robot_tours = {robot: nearest_neighbor_solution(0) for robot in robots}

# Initial Total Travel Cost Calculation
def calculate_tour_cost(tour):
    return sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

total_cost = 0

for robot, tour in robot_tours.items():
    tour_cost = calculate_tour_cost(tour)
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {tour_cost}")
    total_cost += tour_cost

print(f"Overall Total Travel Cost: {total_cost}")