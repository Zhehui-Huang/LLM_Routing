import math
from itertools import permutations

# Coordinates for each city including depot
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), 
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
    (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Euclidean distance calculator
def calculate_distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

# Solving individual TSP for a set of cities starting and ending at the depot
def solve_tsp(cities):
    min_tour = None
    min_cost = float('inf')
    
    for perm in permutations(cities):
        cost = calculate_distance(0, perm[0])  # start from depot
        for i in range(len(perm) - 1):
            cost += calculate_distance(perm[i], perm[i + 1])
        cost += calculate_distance(perm[-1], 0)  # return to depot
        
        if cost < min_cost:
            min_cost = cost
            min_tour = [0] + list(perm) + [0]
    
    return min_tour, min_cost

# Assign cities to robots heuristically
# For simplicity, divide number of cities (excluding depot) as evenly as possible
num_robots = 2
city_indices = list(range(1, 19))
chunk_size = len(city_indices) // num_robots
tours = []
costs = []

for i in range(num_robots):
    if i < num_robots - 1:
        robot_cities = city_indices[i * chunk_size:(i + 1) * chunk_size]
    else:
        robot_cities = city_indices[i * chunk_size:]
    
    tour, cost = solve_tsp(robot_cities)
    tours.append(tour)
    costs.append(cost)

# Output results
overall_cost = sum(costs)
for i in range(num_robots):
    print(f"Robot {i} Tour: {tours[i]}")
    print(f"Robot {i} Total Travel Cost: {costs[i]}")

print(f"Overall Total Travel Cost: {overall_cost}")