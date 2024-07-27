import math
import random

# Euclidean distance function
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Calculate total tour distance
def tour_cost(tour, cities):
    return sum(distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

# Function to conduct a local search for an optimal path variation
def local_search(initial_tour, cities, iterations=1000):
    best_tour = initial_tour[:]
    best_cost = tour_cost(initial_tour, cities)
    for _ in range(iterations):
        new_tour = best_tour[:]
        # Swap two cities in the tour (excluding depot-0 index)
        i, j = sorted(random.sample(range(1, len(best_tour) - 1), 2))
        new_tour[i:j+1] = reversed(new_tour[i:j+1])
        new_cost = tour_cost(new_tour, cities)
        if new_cost < best_cost:
            best_tour, best_cost = new_tour[:], new_cost
    return best_tour, best_cost

# Define cities coordinates
cities = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93), (34, 73),
    (6, 61), (86, 69), (30, 50), (35, 73), (42, 64),
    (64, 30), (70, 95), (29, 64), (32, 79)
]

# Initialize parameters
num_cities_to_visit = 10

# Generate a random sample of cities to visit including the depot
best_overall_tour = None
best_overall_cost = float('inf')

# Repeated random sampling and local search
for _ in range(1000):
    sampled_cities = random.sample(range(1, 15), num_cities_to_visit - 1)
    initial_tour = [0] + sampled_cities + [0]
    refined_tour, refined_cost = local_search(initial_tour, cities)
    if refined_cost < best_overall_cost:
        best_overall_tour, best_overall_cost = refined_tour, refined_cost

# Output best found solution
print("Tour:", best_overall_tour)
print("Total travel cost:", best_overall_cost)