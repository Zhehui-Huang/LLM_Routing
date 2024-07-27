import math
import random
from copy import deepcopy

# Define the cities and their coordinates
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

# Initialize variables
num_robots = 8
starting_city = 0  # All robots start from city 0
num_cities = len(cities)

# Helper function to calculate Euclidean distance
def euclidean_distance(idx1, idx2):
    return math.sqrt((cities[idx1][0] - cities[idx2][0])**2 + (cities[idx1][1] - cities[idx2][1])**2)

# Initially distribute cities to robots
tours = {i: [starting_city] for i in range(num_robots)}
assigned_cities = {starting_city}
count = 0

# Distribute remaining cities round-robin style, skipping the starting city
for city in range(1, num_cities):
    if city != starting_city and city not in assigned_cities:
        tours[count % num_robots].append(city)
        assigned_cities.add(city)
        count += 1

# Simulated Annealing parameters
def simulated_annealing(tour):
    T = 1000  # Initial temperature
    T_min = 1  # Minimum temperature
    alpha = 0.95  # Cooling rate

    current_cost = calculate_tour_cost(tour)
    current_tour = deepcopy(tour)

    while T > T_min:
        new_tour = deepcopy(current_tour)
        i, j = random.randint(1, len(new_tour) - 1), random.randint(1, len(new_tour) - 1)
        new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
        new_cost = calculate_tour_cost(new_tour)

        if new_cost < current_cost or math.exp((current_cost - new_cost) / T) > random.random():
            current_tour, current_cost = new_tour, new_cost

        T *= alpha

    return current_tour

# Function to calculate tour cost
def calculate_tour_cost(tour):
    cost = 0
    for i in range(1, len(tour)):
        cost += euclidean_distance(tour[i - 1], tour[i])
    return cost

# Optimize tours
optimized_tours = {}
overall_total_cost = 0

for robot in tours:
    optimized_tour = simulated_annealing(tours[robot])
    tour_cost = calculate_tour_cost(optimized_tour)
    overall_total_cost += tour_cost
    optimized_tours[robot] = optimized_tour
    print(f'Robot {robot} Tour: {optimized_tour}')
    print(f'Robot {robot} Total Travel Cost: {tour_cost}')

print(f'Overall Total Travel Cost: {overall_total_cost}')