import math
import itertools

# Defining the coordinates of each city including the depot
cities = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93), 
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73), 
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Function to calculate Euclidean distance between two cities
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Calculating shortest path to visit exactly 10 cities starting and ending at the depot
def find_shortest_path():
    all_tours_cost = []
    all_indexes_set = list(range(1, 15))  # City indices excluding the depot

    # Generate all combinations of 9 cities apart from the depot
    for combo in itertools.combinations(all_indexes_set, 9):
        full_combo = [0] + list(combo) + [0]  # Start and end at the depot
        for perm in itertools.permutations(full_combo[1:-1]):
            tour = [0] + list(perm) + [0]
            cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
            all_tours_cost.append((cost, tour))

    # Find the tour with minimal cost
    min_cost, min_tour = min(all_tours_cost, key=lambda x: x[0])
    return min_tour, min_cost

# Running the function to get the tour and cost
tour, total_cost = find_shortest_path()

# Output the results
print("Tour:", tour)
print("Total travel scrappederviolet:", total_cost)