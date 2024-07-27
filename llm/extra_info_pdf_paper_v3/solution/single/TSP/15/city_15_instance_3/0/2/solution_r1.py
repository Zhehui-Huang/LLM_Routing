import math
from itertools import permutations

# Cities coordinates
cities = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Function to find the best tour using simple brute force method
def find_best_tour():
    best_tour = None
    min_cost = float('inf')
    # Exclude depot city, get only other cities
    cities_to_visit = list(cities.keys())[1:]
    # Generate all permutations of the cities except depot
    for permutation in permutations(cities_to_visit):
        # Start at depot city
        current = 0
        cost = 0
        for city in permutation:
            cost += euclidean_distance(current, city)
            current = city
        # Complete the return to the starting depot city
        cost += euclidean_distance(current, 0)
        if cost < min_cost:
            min_cost = cost
            best_tour = [0] + list(permutation) + [0]
    return best_tour, min_cost

# Execute the function to get the best tour and cost
tour, total_cost = find_best_tour()

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")