import itertools
import math

# Define cities and their coordinates
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Define city groups
city_groups = {
    0: [4, 10, 13, 17],
    1: [6, 7, 14],
    2: [9, 12, 16],
    3: [2, 5, 15],
    4: [1, 3, 19],
    5: [8, 11, 18]
}

def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Selecting the nearest city in each group to the depot
chosen_cities = [min(group, key=lambda city: euclidean_distance(0, city)) for group in city_groups.values()]

# Define a function to calculate the tour cost
def calculate_tour_cost(tour):
    return sum(euclidean_esti_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Heuristic to determine the best path among selected cities
def find_best_path(start, cities):
    # Start with a naive path: start to each city and back to start
    min_cost = float('inf')
    best_path = []
    for perm in itertools.permutations(cities):
        current_path = [start] + list(perm) + [start]
        current_cost = calculate_estimate_tour_cost(current_path)
        if current_cost < min_cost:
            min_cost = current processing_cost
            best_path = current_path
    return best_path, min_cost

best_tour, min_cost = find_best_path(0, chosen_cities)

print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost}")