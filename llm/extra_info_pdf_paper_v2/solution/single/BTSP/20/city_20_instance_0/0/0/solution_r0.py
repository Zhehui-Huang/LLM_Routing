import math
from itertools import permutations

# Define the cities' coordinates
cities = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), 
    (97, 32), (25, 71), (61, 16), (27, 91), (91, 46), (40, 87),
    (20, 97), (61, 25), (5, 59), (62, 88), (13, 43), (61, 28),
    (60, 63), (93, 15)
]

# Calculate the Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Initial tour using a naive heuristic (nearest neighbor)
def initial_tour():
    n = len(cities)
    unvisited = list(range(1, n))
    tour = [0]
    current = 0
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: distance(cities[current], cities[city]))
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city
    
    tour.append(0)  # return to the depot
    return tour

# Calculate the total cost and maximum distance between consecutive cities in the tour
def evaluate_tour(tour):
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = distance(cities[tour[i]], cities[tour[i+1]])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    return total_cost, max_distance

# Optimize the initial tour by trying to swap two cities that would reduce the max distance in the tour
def optimize_tour(tour):
    n = len(tour)
    best_max_distance = float('inf')
    best_tour = tour.copy()
    
    for _ in range(1000):  # Iterative improvement attempts
        new_tour = best_tour[:]
        i, j = sorted(random.sample(range(1, n-1), 2))
        new_tour[i:j] = new_tour[i:j][::-1]
        
        _, new_max_distance = evaluate_tour(new_tour)
        if new_max_distance < best_max_distance:
            best_max_distance = new_max_distance
            best_tour = new_tour[:]
    
    return best_tour

# Let's find a tour
tour = initial_tour()
optimized_tour = optimize_tour(tour)
total_cost, max_distance = evaluate_tour(optimized_tour)

# Output format as required
output = {
    "Tour": optimized_tour,
    "Total travel cost": round(total_cost, 2),
    "Maximum distance between consecutive cities": round(max_distance, 2)
}

print(output)