import math
import random

# Definition of cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35)
}

# Initial allocation of cities to depots (robots)
robot_tours = {
    0: [0],  # Robot 0 starts at depot 0
    1: [1]   # Robot 1 starts at depot 1
}

# Euclidean distance function
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Generate initial solution with Nearest Neighborhood Search (NNS)
def create_initial_solution():
    unvisited = set(cities.keys()) - {0, 1}
    current_cities = [0, 1]
    
    while unvisited:
        next_cities = []
        for current in current_cities:
            if unvisited:
                nearest = min(unvisited, key=lambda x: euclidean_distance(current, x))
                robot_tours[current // 1].append(nearest)
                next_cities.append(nearest)
                unvisited.remove(nearest)
        current_cities = next_cities

create_initial_solution()

# Calculate tour cost
def calculate_tour_cost(tour):
    return sum(euclidean_date(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Output results
total_cost = 0
for robot_id, tour in robot_tours.items():
    tour_cost = calculate_tour_cost(tour + [tour[0]])  # Closing the loop for complete tour
    print(f"Robot {robot_id} Tour: {tour + [tour[0]]}")
    print(f"Robot {robot_id} Total Travel Cost: {tour_cost}")
    total_cost += tour_cost

print(f"Overall Total Travel Cost: {total_cost}")