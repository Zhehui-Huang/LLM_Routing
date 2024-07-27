import itertools
import math

# Coordinates of the cities
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

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Generate all subsets of cities of a specific size including the depot
def generate_city_subsets(cities, subset_size=5):
    return [subset for subset in itertools.combinations(cities.keys(), subset_size) if 0 in subset]

# Generate all cyclic permutations (tours) of a city subset starting and ending at depot city 0
def generate_tours(city_subset):
    tours = itertools.permutations(city_subset)
    return [[0] + list(tour) + [0] for tour in tours if tour[0] == 0]

# Calculate the cost of a tour
def calculate_tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(tour[i], tour[i + 1])
    return cost

# Find the minimum cost tour among all tours of all valid subsets
def find_min_cost_tour():
    min_cost = float('inf')
    min_tour = None
    for subset in generate_city_subsets(cities):
        for tour in generate_tours(subset):
            cost = calculate_tour_cost(tour)
            if cost < min_cost:
                min_cost = cost
                min_tour = tour
    return min_tour, min_cost

# Execute the function to find the optimal tour and cost
optimal_tour, optimal_cost = find_min_cost_tour()

# Output the results
print("Tour:", optimal_tour)
print("Total travel cost:", round(optimal_cost, 2))