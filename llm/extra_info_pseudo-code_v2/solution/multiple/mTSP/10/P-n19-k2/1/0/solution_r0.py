import math
from itertools import permutations

# City coordinates
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 43),
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
    13: (58, 27),
    14: (37, 69),
    15: (61, 33),
    16: (62, 63),
    17: (63, 69),
    18: (45, 35)
}

# Calculate Euclidean distance between two cities
def calculate_distance(i, j):
    return math.sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)

# Finding optimal tours for the robots
def solve_mTSP(cities, num_robots):
    cities_to_visit = list(cities.keys())[1:]  # Excluding the depot which is 0
    min_total_cost = float('inf')
    best_robot_tours = []
    
    # Generate all permutations of city visits and split them among robots
    for perm in permutations(cities_to_visit):
        # Split the permutation into `num_robots` segments
        tour_splits = [0] + [len(perm) * i // num_robots for i in range(1, num_robots)]
        tour_splits.append(len(perm))
        
        robot_tours = []
        total_cost = 0
        feasible = True

        for i in range(num_robots):
            tour = [0] + list(perm[tour_splits[i]:tour_splits[i + 1]]) + [0]
            tour_cost = sum(calculate_distance(tour[j], tour[j + 1]) for j in range(len(tour) - 1))
            robot_tours.append((tour, tour_cost))
            total_cost += tour_cost
        
        # Check if this configuration is better
        if total_cost < min_total_cost:
            min_total_transfer_cost = total_cost
            best_robot_tours = robot_tours

    return best_robot_tours, min_total_transfer_cost

# Number of robots
num_robots = 2

# Solving the mTSP
tours, overall_cost = solve_mTSP(cities, num_robots)

# Output the results
for robot_id, (tour, cost) in enumerate(tours):
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {overall_cost}")