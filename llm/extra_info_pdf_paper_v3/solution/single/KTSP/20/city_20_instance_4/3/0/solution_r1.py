import random
import math
from itertools import permutations

# Define the coordinates of cities as tuples in a list
cities = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), 
    (69, 22), (28, 11), (70, 2), (47, 50), (60, 29), 
    (29, 26), (85, 68), (60, 1), (71, 73), (82, 47),
    (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def calculate_total_distance(tour):
    total_dist = 0
    for i in range(len(tour) - 1):
        total_dist += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    total_dist += euclidean_distance(cities[tour[-1]], cities[tour[0]])  # Closing the loop back to depot
    return total_dist

def find_shortest_tour():
    selected_cities = [0]  # Start with depot
    selected_cities.extend(random.sample(range(1, 20), 15))  # Choose 15 other cities randomly
    
    best_tour = None
    best_distance = float('inf')
    
    # Generate permutations and find the shortest possible tour
    for perm in permutations(selected_cities):
        perm = list(perm) + [0]  # Return to the depot to close the loop
        current_distance = calculate_total_distance(perm)
        if current_distance < best_distance:
            best_distance = current_distance
            best_tour = perm
    
    return best_tour, best_distance

# Find the shortest tour
best_tour, best_distance = find_shortest_tour()

# Output the results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_distance:.2f}")