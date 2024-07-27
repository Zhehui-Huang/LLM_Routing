import math
import random

# Cities and their coordinates
cities = {
  0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
  5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
  10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
  15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
  20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Euclidean distance function
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Function to generate a random solution using a simple nearest neighbor algorithm
def generate_initial_solution(depot, cities_list):
    tour = [depot]
    current_city = depot
    unvisited = set(cities_list)
    unvisited.remove(depot)

    while unvisited:
        next_city = min(unvisited, key=lambda x: distance(current_city, x))
        unvisited.remove(next_city)
        tour.append(next_city)
        current_city = next_city

    tour.append(depot)
    return tour

# Function to calculate total travel cost of a tour
def calculate_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Assign non-depot cities to each robot
depot_start = list(range(8))  # Robots 0 to 7 start at depots 0 to 7
assigned_cities = {i: [] for i in depot_start}
remaining_cities = set(range(8, 23))  # Cities 8 to 22 are not depots

# Distribute cities to robots
for city in remaining_cities:
    nearest_depot = min(depot_start, key=lambda x: distance(city, x))
    assigned_cities[nearest_depot].append(city)

# Solution initialization
robot_tours = {}
total_costs = {}
total_cost = 0

# Generate initial solution and perform simple optimization
for robot, starting_depot in enumerate(depot_start):
    tour_cities = [starting_depot] + assigned_cities[starting_depot] + [starting_depot]
    if len(tour_cities) > 2:
        tour = generate_initial_solution(starting_depot, tour_cities)
        cost = calculate_cost(tour)
    else:
        tour = [starting_depot, starting_depot]
        cost = 0
    robot_tours[robot] = tour
    total_costs[robot] = cost
    total_cost += cost

# Output the result
for robot in robot_tours:
    print(f"Robot {robot} Tour: {robot_tours[robot]}")
    print(f"Robot {robot} Total Travel Cost: {total_costs[robot]}")

print(f"Overall Total Travel Cost: {total_cost}")