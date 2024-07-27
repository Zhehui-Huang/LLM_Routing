import itertools
import math

# Coordinates of cities including the depot city
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

# Function to compute Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Function to compute the total tour cost
def calculate_tour_cost(tour):
    tour_cost = 0
    for i in range(len(tour) - 1):
        tour_cost += distance(tour[i], tour[i + 1])
    return tour_cost

# Generate all possible selection of 5 cities out of 9 (excluding the depot city)
city_indices = list(range(1, 10))
all_city_combinations = list(itertools.combinations(city_indices, 5))

# Search for the minimum cost tour
min_cost = float('inf')
best_tour = []

for cities_subset in all_city_combinations:
    cities_to_visit = [0] + list(cities_subset) + [0]  # include the depot city

    # Generate all permutations for the selected cities
    for perm in itertools.permutations(cities_to_visit[1:-1]):
        current_tour = [0] + list(perm) + [0]
        cost = calculate_tour_cost(current_tour)
        
        # Update the best tour if found a new minimum cost
        if cost < min_cost:
            min_cost = cost
            best_tour = current_tour

# Output the results
print(f'Tour: {best_tour}')
print(f'Total travel cost: {min_cost}')