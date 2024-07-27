import itertools
import math

# Provided city coordinates
cities = {
    0: (8, 11),
    1: (40, 6),
    2: (95, 33),
    3: (80, 60),
    4: (25, 18),
    5: (67, 23),
    6: (97, 32),
    7: (25, 71),
    8: (61, 16),
    9: (27, 91),
    10: (91, 46),
    11: (40, 87),
    12: (20, 97),
    13: (61, 25),
    14: (5, 59),
    15: (62, 88),
    16: (13, 43),
    17: (61, 28),
    18: (60, 63),
    19: (93, 15)
}

# Function to calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Function to compute the total cost of a given tour
def tour_cost(tour):
    total_cost = sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    return total_cost

# Function to find the shortest tour visiting exactly k cities starting and ending at the depot city
def find_shortest_k_tour(cities, k):
    min_cost = float('inf')
    best_tour = None

    # Generate all possible tours visiting exactly k cities
    for combo in itertools.combinations(cities.keys() - {0}, k - 1):
        full_tour = [0] + list(combo) + [0]
        for permuted_tour in itertools.permutations(full_tour[1:-1]):
            candidate_tour = [0] + list(permuted_tour) + [0]
            cost = tour_cost(candidate_tour)
            if cost < min_cost:
                min_cost = cost
                best_tour = candidate_tour
            
    return best_tour, min_cost

# Compute best 4-city tour
best_tour, min_cost = find_shortest_k_tour(cities, 4)

# Output the results
print("Tour:", best_tour)
print("Total travel cost:", min_cost)