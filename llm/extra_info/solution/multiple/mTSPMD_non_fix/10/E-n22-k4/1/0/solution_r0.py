import math
from itertools import permutations

# Define cities and their coordinates
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254),
    4: (128, 252), 5: (163, 247), 6: (146, 246), 7: (161, 242),
    8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
    12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208),
    16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

# Distance function based on Euclidean distance
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Optimization function using the nearest neighbor algorithm
def nearest_neighbor_tour(start_city, cities, all_cities):
    unvisited = set(all_cities)
    unvisited.remove(start_city)
    tour = [start_city]
    current_city = start_city
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: distance(cities[current_city], cities[city]))
        unvisited.remove(next_city)
        tour.append(next_city)
        current_city = next_city
        
    return tour

# Robots information
num_robots = 4
robots = {i: nearest_neighbor_tour(i, cities, list(cities.keys())) for i in range(num_robots)}

# Calculate total cost for each robot
def calculate_travel_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distance(cities[tour[i]], cities[tour[i + 1]])
    return total_cost

# Collect tours and costs
total_costs = []
for robot_id, tour in robots.items():
    tour_cost = calculate_travel_cost(tour)
    total_costs.append(tour_cost)
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {round(tour_cost, 2)}")

# Display overall results
overall_total_cost = sum(total_costs)
print(f"Overall Total Travel Cost: {round(overall_total_cost, 2)}")