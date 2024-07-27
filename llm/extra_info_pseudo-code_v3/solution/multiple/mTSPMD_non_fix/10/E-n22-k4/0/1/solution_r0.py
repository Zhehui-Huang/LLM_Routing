import math
from itertools import permutations

# Data setup
cities = {
    0: (145, 215),   1: (151, 264),   2: (159, 261),   3: (130, 254),
    4: (128, 252),   5: (163, 247),   6: (146, 246),   7: (161, 242),
    8: (142, 239),   9: (163, 236),  10: (148, 232),  11: (128, 231),
    12: (156, 217),  13: (129, 214), 14: (146, 208),  15: (164, 208),
    16: (141, 206),  17: (147, 193), 18: (164, 193),  19: (129, 189),
    20: (155, 185),  21: (139, 182)
}

# Number of robots
num_robots = 4

# Calculate Euclidean distance
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Generate all possible single tours - very inefficient for many cities but doable for small example
def generate_all_tours():
    all_tours = []
    city_list = list(cities.keys())
    for perm in permutations(city_list[1:]):  # exclude the depot city for permutations
        tour = [0] + list(perm) + [0]
        all_tours.append(tour)
    return all_tours

# Check if the setup is feasible for reasonable computation, otherwise go for a heuristic.
if len(cities) > 12:  # picked a reasonable cut-off for factorial time complexity
    print("Too many cities for factorial-time computation!")
else:
    all_possible_tours = generate_all_tours()
    min_cost = float('inf')
    best_split = None
    
    # Evaluate each allocation of these tours to the robots
    for tour_combination in permutations(all_possible_tours, num_robots):
        total_cost = sum(distance(tour_combination[i][k], tour_combination[i][k+1]) for i in range(num_robots) for k in range(len(tour_combination[i])-1))
        if total_cost < min_cost:
            min_cost = total_cost
            best_split = tour_combination
    
    # Output the best tours found
    total_travel_cost = 0
    for i in range(num_robots):
        tour = best_split[i]
        tour_cost = sum(distance(tour[k], tour[k+1]) for k in range(len(tour)-1))
        total_travel_cost += tour_cost
        print(f"Robot {i} Tour: {tour}")
        print(f"Robot {i} Total Travel Cost: {tour_cost}")

    print(f"Overall Total Travel Cost: {total_travelal_cost}")