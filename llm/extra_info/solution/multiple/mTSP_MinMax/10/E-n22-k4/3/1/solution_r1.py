import math
import itertools

# Function to compute Euclidean distance
def euclidean_distance(pt1, pt2):
    return math.sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)

# Generate all possible assignments of cities to robots
def generate_assignments(num_cities, num_robots):
    base_list = list(range(1, num_cities))
    return set(itertools.permutations(base_list))

# Calculate the overall cost for the robot tours
def calculate_total_cost(tours, coords):
    def path_cost(path):
        return sum(euclidean_distance(coords[path[i]], coords[path[i+1]]) for i in range(len(path) - 1))

    costs = [path_cost([0] + tour + [0]) for tour in tours]
    return costs, max(costs)

# Split a permutation into more balanced tours for robots
def balanced_split(permutation, num_robots):
    n = len(permutation)
    k = n // num_robots  # minimum number of cities per robot
    tours = []
    for i in range(num_robots-1):
        tours.append(permutation[i*k:(i+1)*k])
    tours.append(permutation[(num_robots-1)*k:])  # Last robot takes the remainder
    return tours

# Coordinates: city index to (x, y)
coordinates = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254),
    4: (128, 252), 5: (163, 247), 6: (146, 246), 7: (161, 242),
    8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
    12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208),
    16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}
num_robots = 4
all_perms = generate_assignments(22, num_robots)

# Evaluate each assignment
best_max_cost = float('inf')
best_tours = None
for perm in all_perms:
    splits = balanced_split(list(perm), num_robots)
    costs, max_cost = calculate_total_cost(splits, coordinates)
    if max_cost < best_max_cost:
        best_max_cost = max_cost
        best_tours = splits
        best_costs = costs

# Output the results
for idx, tour in enumerate(best_tours):
    full_tour = [0] + list(tour) + [0]
    cost = best_costs[idx]
    print(f"Robot {idx} Tour: {full_tour}")
    print(f"Robot {idx} Total Travel Cost: {cost:.2f}")

print(f"Maximum Travel Cost: {best_max_cost:.2f}")