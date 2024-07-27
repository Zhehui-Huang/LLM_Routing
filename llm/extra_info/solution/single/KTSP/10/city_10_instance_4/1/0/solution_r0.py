import itertools
import math

# Coordinates of the cities
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

# Function to calculate Euclidean distance between two cities
def dist(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Function to calculate the total cost of a tour
def tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += dist(tour[i], tour[i + 1])
    return total_cost

# Generate all combinations of 7 cities (not including depot)
city_combinations = itertools.combinations(range(1, 10), 7)

# Find the shortest tour including the depot city and 7 other cities
min_cost = float('inf')
optimal_tour = []

for combo in city_combinations:
    # Generate permutations of each combination to find shortest path
    for perm in itertools.permutations(combo):
        current_tour = [0, *perm, 0]
        current_cost = tour_cost(current_tour)
        if current_cost < min_cost:
            min_cost = current_cost
            optimal_tour = current_tour

# Output the result
print("Tour:", optimal_tour)
print("Total travel cost:", min_cost)