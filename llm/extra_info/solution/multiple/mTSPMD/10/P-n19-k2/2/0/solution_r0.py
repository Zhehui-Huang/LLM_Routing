from scipy.spatial.distance import euclidean
from itertools import permutations

# Cities and their coordinates.
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 27), 14: (37, 69), 15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Function to calculate tour cost
def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean(cities[tour[i]], cities[tour[i + 1]])
    return total_cost

# All city indices except the depots
all_cities = list(range(2, 19))

# Find best split of cities between two robots
best_total_cost = float('inf')
best_robot_0_tour = []
best_robot_1_tour = []

# Try all permutations of city assignments to find the best combination
for length in range(len(all_cities) // 2 + 1):
    for robot_0_cities in permutations(all_cities, length):
        robot_1_cities = [c for c in all_cities if c not in robot_0_cities]
        
        # Include depots
        robot_0_cities = [0] + list(robot_0_cities) + [0]
        robot_1_cities = [1] + list(robot_1_cities) + [1]
        
        # Find shortest path for robot 0
        robot_0_permutations = list(permutations(robot_0_cities[1:-1]))
        robot_1_permutations = list(permutations(robot_1_cities[1:-1]))
        
        for perm_0 in robot_0_permutations:
            tour_0 = [0] + list(perm_0) + [0]
            cost_0 = calculate_tour_cost(tour_0)
            for perm_1 in robot_1_permutations:
                tour_1 = [1] + list(perm_1) + [1]
                cost_1 = calculate_tour_cost(tour_1)
                
                total_cost = cost_0 + cost_1
                if total_cost < best_total_cost:
                    best_total_cost = total_cost
                    best_robot_0_tour = tour_0
                    best_robot_1_tour = tour_1

# Print the best tours and costs
cost_robot_0 = calculate_tour_cost(best_robot_0_tour)
cost_robot_1 = calculate_tour_cost(best_robot_1_tour)

print(f"Robot 0 Tour: {best_robot_0_tour}")
print(f"Robot 0 Total Travel Cost: {cost_robot_0:.2f}")

print(f"Robot 1 Tour: {best_robot_1_tour}")
print(f"Robot 1 Total Travel Cost: {cost_robot_1:.2f}")

print(f"Overall Total Travel Cost: {best_total_cost:.2f}")