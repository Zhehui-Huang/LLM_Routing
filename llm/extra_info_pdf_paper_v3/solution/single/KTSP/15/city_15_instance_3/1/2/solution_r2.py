import math
from itertools import combinations, permutations

# City coordinates
cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93),
    5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73),
    10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
}

# Calculate Euclidean distance
def euclidean_distance(ci, cj):
    x1, y1 = cities[ci]
    x2, y2 = cities[cj]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Generate all possible tours starting and ending at depot including exactly 10 cities
def all_possible_tours():
    all_positions = list(cities.keys())[1:] # excludes depot initially
    best_distance = float('inf')
    best_path = []

    # Use combinations to choose any 9 cities in addition to the depot city
    for sub_tour in combinations(all_positions, 9):
        for order in permutations(sub_tour):
            tour = [0] + list(order) + [0] # Creating tour starting and ending at depot
            # Calculate tour distance
            total_distance = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
            if total_distance < best_distance:
                best_distance = total_distance
                best_path = tour
            
    return best_path, best_distance

# Get the best tour and its distance
best_tour, min_distance = all_possible_tours()

# Printing results
print("Tour:", best_tour)
print("Total travel cost:", round(min_distance, 2))