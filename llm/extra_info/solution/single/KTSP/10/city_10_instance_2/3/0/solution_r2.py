import itertools
import math

def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

def calculate_total_distance(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_distance

# Coordinates of the cities
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

min_tour = None
min_distance = float('inf')

# Choose 5 cities from cities 1 to 9 (because we must include city 0)
for combination in itertools.combinations(range(1, 10), 5):
    # Full tour must include city 0 at the start and end
    current_combination = [0] + list(combination) + [0]
    
    # Permute the middle cities to find the shortest route for this combination
    for permutation in itertools.permutations(current_combination[1:-1]):
        current_tour = [0] + list(permutation) + [0]
        current_distance = calculate_total_distance(current_tour)
        
        if current_distance < min_distance:
            min_distance = current_distance
            min_tour = current_tour

print("Tour:", min_tour)
print("Total travel cost:", min_distance)