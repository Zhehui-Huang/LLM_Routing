from itertools import permutations, combinations
from math import sqrt

# Define the cities coordinates
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

def calculate_distance(city1, city2):
    """ Euclidean distance between two cities based on coordinates. """
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Generate all possible city subsets that include the depot (city 0) and have a total of 5 cities
city_sets = combinations([i for i in range(10)], 4)
city_combinations = [tuple([0]) + city_set for city_set in city_s...

def find_optimal_tour():
    # Minimum path initialization
    min_cost = float('inf')
    best_tour = None

    # Iterate over all city combinations
    for city_combination in city_combinations:
        # Consider each permutation of the current city combination
        for perm in permutations(city_combination):
            # To ensure the tour starts and ends at the depot
            if perm[0] == 0:
                # Calculate the cost of this permutation
                cost = sum(calculate_distance(perm[i], perm[i+1]) for i in range(len(perm) - 1)) + calculate_distance(perm[-1], perm[0])
                # Find the minimum cost and corresponding tour
                if cost < min_cost:
                    min_cost = cost
                    best_tour = perm + (0,)

    return best_t ><|...|> # Returns the best found tour and the minimum cost

optimal_tour, total_cost = find_optimal_tour()
print(f"Tour: {list(optimal_tour)}")
print(f"Total travel cost: {total_cost:.2f}")