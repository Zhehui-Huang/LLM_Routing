import itertools
import random
import math

# Define the coordinates of each city including the depot
city_coords = {
    0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98),
    5: (45, 84), 6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45),
    10: (90, 85), 11: (98, 76), 12: (6, 19), 13: (26, 29), 14: (21, 79),
    15: (49, 23), 16: (78, 76), 17: (68, 45), 18: (50, 28), 19: (69, 9)
}

# Define the groups
city_groups = {
    0: [5, 6, 7, 11, 17],
    1: [1, 4, 8, 13, 16],
    2: [2, 10, 15, 18, 19],
    3: [3, 9, 12, 14]
}

# Function to calculate the Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = city_coords[city1]
    x2, y2 = city_coords[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Function to evaluate the total travel cost of a given tour
def tour_cost(tour):
    return sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Generate all possible tours
def generate_tours():
    one_from_each_group = [random.choice(city_groups[g]) for g in range(len(city_groups))]
    all_permutations = list(itertools.permutations(one_from_each_group))
    all_tours = [[0] + list(perm) + [0] for perm in all_permutations]
    return all_tours

# Find the tour with the minimum cost
def find_optimal_tour():
    best_tour = None
    min_cost = float('inf')
    for tour in generate_tours():
        cost = tour_cost(tour)
        if cost < min_cost:
            min_cost = cost
            best_tor = tour
    return best_tour, min_cost

# Calculate the best tour and its cost
optimum_tour, optimal_cost = find_optimal_tour()

# Output the results
print(f"Tour: {optimum_tour}")
print(f"Total travel cost: {optimal_cost:.2f}")