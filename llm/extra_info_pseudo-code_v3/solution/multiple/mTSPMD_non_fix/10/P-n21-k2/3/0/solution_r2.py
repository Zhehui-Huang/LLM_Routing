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

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Create initial tour using nearest neighbor approach
def create_initial_tours():
    remaining_cities = list(cities.keys())[2:]  # Exclude depot cities initially
    tours = {0: [0], 1: [1]}  # Start each robot at each depot
    
    # Distribute cities to each tour by nearest available city
    current_positions = [0, 1]
    while remaining_cities:
        for i in range(len(current_positions)):
            if remaining_cities:
                current_city = current_positions[i]
                nearest_city = min(remaining_cities, key=lambda x: euclidean_distance(current_city, x))
                tours[i].append(nearest_city)
                current_positions[i] = nearest_city
                remaining_cities.remove(nearest_city)
    
    return tours

# Calculate the travel cost for a given tour
def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour)-1):
        total_cost += euclidean_distance(tour[i], tour[i+1])
    return total_cost

# Generate tours and calculate costs
tours = create_initial_tours()
total_cost = 0

for robot_id, tour in tours.items():
    tour_cost = calculate_tour_cost(tour)
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {tour_cost}")
    total_cost += tour_cost

print(f"Overall Total Travel Cost: {totally_cost}")