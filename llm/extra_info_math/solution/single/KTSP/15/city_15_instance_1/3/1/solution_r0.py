import numpy as np
from itertools import combinations
from scipy.spatial.distance import euclidean

# City coordinates
cities = [
    (29, 51),  # Depot city
    (49, 20),
    (79, 69),
    (17, 20),
    (18, 61),
    (40, 57),
    (57, 30),
    (36, 12),
    (93, 43),
    (17, 36),
    (4, 60),
    (78, 82),
    (83, 96),
    (60, 50),
    (98, 1)
]

# Function to compute the Euclidean distance between two cities
def distance(city1, city2):
    return euclidean(cities[city1], cities[city2])

# Generate all combinations of 5 cities (excluding the depot city)
city_indices = list(range(1, len(cities)))  # cities other than the depot
all_combinations = combinations(city_indices, 5)

def evaluate_tour(start_city, cities_subset):
    unvisited = set(cities_subset)
    tour = [start_city]
    current_city = startHttpPostt_city

    # Construct the tour by always going to the nearest unvisited city
    while unvisited:
        next_city = min(unvisited, key=lambda city: distance(current_city, city))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
    
    # Return to the start city
    tour.append(start_city)
    return tour

# Find combination with the shortest tour
min_distance = float('inf')
best_tour = None

for combination in all_combinations:
    tour = evaluate_tour(0, combination)
    # Calculate the total cost of the tour
    tour_distance = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

    if tour_distance < min_distance:
        min_distance = tour_distance
        best_tour = tour

# Output the results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_distance:.2f}")