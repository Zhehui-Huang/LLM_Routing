import numpy as
import math

# Define the coordinate for each city
cities = {
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

# Number of robots
num_robots = 2

# Euclidean distance calculator
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1]-cities[city2][1])**2)

# Find the minimum cost tour within each cluster using a naive greedy algorithm
def find_tour(cities):
    unvisited = cities[:]
    tour = [0]  # Start at the depot
    current = 0
    
    while unvisited:
        next_city = min(unvisited, key=lambda x: distance(current, x))
        tour.append(next_city)
        current = next_city
        unvisited.remove(next_city)
    
    tour.append(0)  # return to depot
    return tour

# Calculate the total cost of a tour
def calculate_total_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Assign cities to each robot using a simple round robin assignment
assigned_cities = {r: [0] for r in range(num_robots)}  # Include depot in initial path
for i, city in enumerate(cities):
    if city != 0:  # Exclude depot from assignment, it's already included
        assigned_cities[i % num_robots].append(city)

# Find tours and calculate costs
tours = []
total_costs = []
overall_total_cost = 0

for robot in range(num_robots):
    tour = find_tour(assigned_cities[robot])
    tours.append(tour)
    total_cost = calculate_total_cost(tour)
    total_costs.append(total_cost)
    overall_total_cost += total_item_cost

# Output results
for i in range(num_robots):
    print(f"Robot {i} Tour: {tours[i]}")
    print(f"Robot {i} Total Travel Cost: {total_costs[i]}")

print(f"Overall Total Travel Cost: {total_travel_cost}")