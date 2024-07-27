import math
import itertools

# Coordinates of the cities
cities = [
    (79, 15),  # Depot city 0
    (79, 55),  # City 1
    (4, 80),   # City 2
    (65, 26),  # City 3
    (92, 9),   # City 4
    (83, 61),  # City 5
    (22, 21),  # City 6
    (97, 70),  # City 7
    (20, 99),  # City 8
    (66, 62)   # City 9
]

# Calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Precompute distances between all pairs of cities
distances = {}
for i in range(len(cities)):
    for j in range(i + 1, len(cities)):
        dist = calculate_distance(cities[i], cities[j])
        distances[(i, j)] = dist
        distances[(j, i)] = dist

# Initialize minimum tour and cost
min_tour = None
min_cost = float('inf')

# Calculate tour cost for a given tour path
def calculate_tour_cost(tour):
    cost = 0
    for i in range(1, len(tour)):
        cost += distances[(tour[i-1], tour[i])]
    # Include trip back to the starting city
    cost += distances[(tour[-1], tour[0])]
    return cost

# Explore all possible permutations of visiting non-depot cities
for permutation in itertools.permutations(range(1, len(cities))):
    # Add the starting city (depot city) to the beginning and end of the tour
    tour = (0,) + permutation + (0,)
    cost = calculate_tour_cost(tour)
    if cost < min_cost:
        min_cost = cost
        min_tour = tour

# Display the results
print("Tour:", list(min_tour))
print("Total travel cost:", min_cost)