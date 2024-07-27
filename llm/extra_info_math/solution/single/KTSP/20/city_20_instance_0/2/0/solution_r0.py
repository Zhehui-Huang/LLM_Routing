from itertools import combinations
import math

# Define the cities coordinates
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

# Define a function to calculate euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Function to calculate the total travel cost of a tour
def calculate_tour_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Generate all combinations of 3 cities (excluding the depot) to be visited
city_indices = list(range(1, 20))  # city indices excluding the depot, which is 0
combinations_of_cities = combinations(city_indices, 3)

min_cost = float('inf')
best_tour = None

# Iterate through each combination and calculate the tour cost
for city_set in combinations_of_city_indices:
    current_tour = [0] + list(city_set) + [0]
    cost = calculate_tour_cost(current_tour)

    if cost < min_cost:
        min_cost = cost
        best_tour = [0] + list(city_set) + [0]

# Output the best tour and its total cost
print("Tour:", best_tour)
print("Total travel cost:", min_cost)