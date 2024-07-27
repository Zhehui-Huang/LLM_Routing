import math
import itertools

# Coordinates for the cities
cities = {
    0: (3, 26),
    1: (85, 72),
    2: (67, 0),
    3: (50, 99),
    4: (61, 89),
    5: (91, 56),
    6: (2, 65),
    7: (38, 68),
    8: (3, 92),
    9: (59, 8),
    10: (30, 88),
    11: (30, 53),
    12: (11, 14),
    13: (52, 49),
    14: (18, 49),
    15: (64, 41),
    16: (28, 49),
    17: (91, 94),
    18: (51, 58),
    19: (30, 48)
}

# Calculating Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Generate all possible subsets of the remaining cities of size k-1
def subsets(cities, k):
    return list(itertools.combinations(cities, k))

# Calculate the path length
def calculate_tour_length(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Find the shortest tour
def find_shortest_10_city_tour():
    all_cities = set(cities.keys())
    min_length = float('inf')
    best_tour = None
    
    # Iterate through all subsets of cities of size 9 (excluding the depot)
    for subset in subsets(all_cities - {0}, 9):
        # Create a tour starting and ending at the depot
        current_tour = [0] + list(subset) + [0]
        
        # Find the best tour permutation within the subset
        for perm in itertools.permutations(subset):
            perm_tour = [0] + list(perm) + [0]
            tour_length = calculate_tour_length(perm_tour)
            
            # Check if this permutation of the tour is the shortest found so far
            if tour_length < min_length:
                min_length = tour_length
                best_tour = perm_tour
    
    return best_tour, min_length

# Using the heuristic to find the solution
tour, total_distance = find_shortest_10_city_tour()
print("Tour:", tour)
print("Total travel cost:", total_distance)