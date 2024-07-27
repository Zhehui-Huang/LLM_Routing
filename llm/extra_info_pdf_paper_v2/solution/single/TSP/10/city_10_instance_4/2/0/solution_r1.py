import math
from itertools import permutations

# Coordinates of the depot and the cities
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Calculate the tour cost
def tour_cost(tour):
    return sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Generate all possible tours starting and ending at the depot (city 0)
def find_best_tour():
    min_cost = float('inf')
    best_tour = None
    # Iterate over all permutations of cities 1 to 9
    for perm in permutations(list(cities.keys())[1:]):  
        # Form a tour that starts and ends at the depot (city 0)
        current_tour = [0] + list(perm) + [0]
        current_cost = tour_cost(current_tour)
        if current_cost < min_cost:
            min_cost = current_cost
            best_tour = current_tour
    return best_tour, min_cost

# Finding the best tour
best_tour, min_cost = find_best_tour()

# Output the best tour and the minimum cost
print("Tour:", best_tour)
print("Total travel cost:", min_cost)