import itertools
import math

# Define city coordinates and city groups
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47), 
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

city_groups = [
    [5, 6, 16], [8, 18, 19], [11, 12, 13], [1, 3, 9], 
    [2, 4, 14], [10, 17], [7, 15]
]

# Calculate Euclidean distance between two cities
def distance(city_a, city_b):
    return math.sqrt((cities[city_b][0] - cities[city_a][0]) ** 2 + (cities[city_b][1] - cities[city_a][1]) ** 2)

# Generate all combinations of exactly one city from each group
city_combinations = list(itertools.product(*city_groups))

def find_optimal_tour():
    min_distance = float('inf')
    optimal_tour = None

    # Test each combination of cities, each combination represents selecting one city from each group
    for combo in city_combinations:
        # Create the tour starting and ending at the depot city 0
        tour = [0] + list(combo) + [0]

        # Calculate the total travel cost of this tour
        total_distance = sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

        # Check if this tour is the shortest tour found so far
        if total_distance < min_distance:
            min_distance = total_distance
            optimal_tour = tour

    return optimal_tour, min_distance

# Get the optimal tour and its total travel cost
tour, total_cost = find_optimal_tour()

# Print results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")