import math
from itertools import permutations

# City coordinates (index represents city ID)
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Number of robots
num_robots = 2

def compute_distance(city1, city2):
    """Calculate Euclidean distance between two cities given their coordinates."""
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

def initialize_tours():
    """Assign each robot to a subset of cities using a simple round-robin assignment."""
    tours = [[] for _ in range(num_robots)]
    for i, city in enumerate(range(1, len(coordinates))):  # Skip the depot city
        tours[i % num_robots].append(city)
    return tours

def two_opt(tour):
    """Optimize the tour using the 2-opt algorithm."""
    improvement = True
    while improvement:
        improvement = False
        for i in range(1, len(tour) - 1):
            for j in range(i + 2, len(tour)):
                if j - i == 1: continue  # Skip adjacent edges
                # Check if reversion leads to improvement
                if (compute_distance(tour[i - 1], tour[i]) + compute_distance(tour[j], tour[j + 1]) >
                        compute_distance(tour[i - 1], tour[j]) + compute_distance(tour[i], tour[j + 1])):
                    tour[i:j+1] = reversed(tour[i:j+1])
                    improvement = True
    return tour

def calculate_tour_cost(tour):
    """Calculate total tour cost."""
    cost = 0.0
    for i in range(len(tour) - 1):
        cost += compute_distance(tour[i], tour[i + 1])
    return cost

# Initial division of cities
initial_tours = initialize_tours()

# Final tours for robots
final_tours = []
total_costs = []

# Each robot constructs its tour starting and ending at the depot
for i, initial_tour in enumerate(initial_tours):
    tour_with_depot = [0] + initial_tour + [0]
    optimized_tour = two_opt(tour_with_depot)
    tour_cost = calculate_tour_cost(optimized_tour)
    
    final_tours.append(optimized_tour)
    total_costs.append(tour_cost)
    
    print(f"Robot {i} Tour: {optimized_tour}")
    print(f"Robot {i} Total Travel Cost: {tour_cost}")

# Calculate the overall total cost
overall_cost = sum(total_costs)
print(f"Overall Total Travel Cost: {overall_cost}")