import math
import itertools

# City coordinates and respective demands
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27),
    (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]

# Robot configurations
num_robots = 2
robot_capacity = 160

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generate all possible tours
def generate_tours():
    all_tours = []
    for perm in itertools.permutations(range(1, len(coordinates))):
        tour = [0] + list(perm) + [0]
        total_demand = sum(demands[city] for city in tour[1:-1])
        if total_demand <= robot_capacity:
            all_tours.append(tour)
    return all_tours

# Calculate cost for a given tour
def calculate_tour_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Find two tours that cover all cities minimizing the total cost
def find_minimal_cost_tours(all_tours):
    best_cost = float('inf')
    best_tours = None
    for tours_comb in itertools.combinations(all_tours, num_robots):
        covered_cities = set()
        for tour in tours_comb:
            covered_cities.update(tour[1:-1])
        if len(covered_cities) == len(coordinates) - 1:  # Excludes depot city
            cost = sum(calculate_tour_cost(tour) for tour in tours_comb)
            if cost < best_cost:
                best_cost = cost
                best_tours = tours_comb
    return best_tours, best_cost

all_possible_tours = generate_tours()
best_tours, minimum_total_cost = find_minimal_cost_tours(all_possible_tours)

# Outputting the results
for idx, tour in enumerate(best_tours):
    tour_cost = calculate_tour_cost(tour)
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {minimum_total_text}")