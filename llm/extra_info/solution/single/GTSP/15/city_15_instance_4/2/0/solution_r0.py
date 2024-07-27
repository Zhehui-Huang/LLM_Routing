import itertools
import math

# City coordinates
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# City groups
city_groups = [[3, 8], [4, 13], [1, 2], [6, 14], [5, 9], [7, 12], [10, 11]]

def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Creating a distance matrix
num_cities = len(cities)
distances = [[0] * num_cities for _ in range(num_cities)]

for i in range(num_cities):
    for j in range(num_cities):
        distances[i][j] = euclidean_distance(i, j)

def calculate_tour_cost(tour):
    # Calculate the round trip distance
    return sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Generate all combination sets of cities (one city from each group)
all_group_combinations = list(itertools.product(*city_groups))

# Find the minimal tour
min_cost = float('inf')
min_tour = None

for group_combination in all_group_combinations:
    # We create potential tours by permuting the indices in each combination.
    for perm in itertools.permutations(group_combination):
        current_tour = [0] + list(perm) + [0]
        cost = calculate_tour_cost(current_tour)
        if cost < min_cost:
            min_cost = cost
            min_tour = current_tour

print(f"Tour: {min_tour}")
print(f"Total travel cost: {min_cost:.2f}")