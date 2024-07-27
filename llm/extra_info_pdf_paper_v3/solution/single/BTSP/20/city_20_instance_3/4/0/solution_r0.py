import math
import itertools

# Coordinates of the cities
cities = [
    (30, 56),  # Depot city 0
    (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), (72, 77), 
    (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94), (96, 73), 
    (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Calculate all distances between cities
distances = [[euclidean_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

def find_tour():
    # Initially start by constructing a tour starting from the depot using a greedy nearest neighbor method
    num_cities = len(cities)
    unvisited = set(range(1, num_cities))
    tour = [0]
    current_city = 0

    while unvisited:
        next_city = min(unvisited, key=lambda city: distances[current_city][city])
        tour.append(next_city)
        current_city = next_city
        unvisited.remove(next_city)
    
    tour.append(0)  # Return to depot

    # Attempt to minimize the maximum distance in the initial tour by trying possible 2-opt swaps
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if j - i == 1: continue  # Skip adjacent pairs
                if distances[tour[i - 1]][tour[i]] + distances[tour[j]][tour[j + 1]] > \
                   distances[tour[i - 1]][tour[j]] + distances[tour[i]][tour[j + 1]]:
                    tour[i:j+1] = reversed(tour[i:j+1])
                    improved = True

    return tour

def calculate_metrics(tour):
    total_travel_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    max_distance = max(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    return total_travel_cost, max_distance

# Finding an approximate solution tour
tour = find_tour()
total_travel_cost, max_distance = calculate_metrics(tour)

print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")