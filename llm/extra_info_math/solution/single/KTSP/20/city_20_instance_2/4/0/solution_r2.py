import math
from itertools import permutations, combinations

# Define the cities with their coordinates
cities = {
    0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89),
    5: (91, 56), 6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8),
    10: (30, 88), 11: (30, 53), 12: (11, 14), 13: (52, 49), 14: (18, 49),
    15: (64, 41), 16: (28, 49), 17: (91, 94), 18: (51, 58), 19: (30, 48)
}

# Calculate Euclidean distance between two cities
def euclidean_distance(city1_idx, city2_idx):
    x1, y1 = cities[city1_idx]
    x2, y2 = cities[city2_idx]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Find the shortest tour using the brute force approach
def find_shortest_tour():
    all_city_indices = list(cities.keys())
    shortest_distance = float('inf')
    best_tour = None

    for combo in combinations(all_city_indices[1:], 9):  # all combinations of 9 cities excluding the depot
        current_combo = [0] + list(combo) + [0]  # start and end at the depot
        for perm in permutations(current_combo[1:-1]):  # permute the intermediate cities
            current_tour = [0] + list(perm) + [0]
            current_distance = sum(euclidean_distance(current_tour[i], current_tour[i+1]) for i in range(len(current_tour) - 1))
            if current_distance < shortest_distance:
                shortest_distance = current_distance
                best_tour = current_tour

    return best_tour, shortest_distance

# Run the function and print the result
tour, cost = find_shortest_tour()
print("Tour:", tour)
print("Total travel cost:", cost)