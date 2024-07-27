import random
import math
from itertools import permutations

# City coordinates
positions = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), 
    (69, 22), (28, 11), (70, 2), (47, 50), (60, 29), 
    (29, 26), (85, 68), (60, 1), (71, 73), (82, 47), 
    (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

def euclidean_distance(city1, city2):
    """Calculate the Euclidean distance between two cities based on their indices."""
    x1, y1 = positions[city1]
    x2, y2 = positions[city2]
    return math.hypot(x2 - x1, y2 - y1)

def calculate_total_distance(tour):
    """Calculate the total distance for the given tour."""
    total_dist = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    total_dist += euclidean_distance(tour[-1], tour[0])  # returning to starting point
    return total_dist

def find_shortest_tour():
    num_cities = 20
    chosen_k = 16
    best_tour = None
    shortest_distance = float('inf')
    
    # Perform multiple trial starts, each starting from a random selection of cities including the depot city 0.
    for _ in range(100):  # Considering multiple initial starts
        cities_to_visit = random.sample(range(1, num_cities), chosen_k - 1)  # random sample of k-1 cities
        cities_to_visit.insert(0, 0)  # include depot city
        
        # Generate all permutations of the chosen group of cities and evaluate
        for perm in permutations(cities_to_visit):
            tour_distance = calculate_total_distance(perm)
            if tour_distance < shortest_distance:
                shortest_distance = tour_distance
                best_tour = perm
    
    return best_tour, shortest_distance

# Get the shortest tour
optimal_tour, optimal_cost = find_shortest_tour()

# Ensure the tour is formatted to start and end at the depot
formatted_tour = list(optimal_tour) + [optimal_tour[0]]

# Output tour and cost
print("Tour:", formatted_tour)
print("Total travel cost:", round(optimal_cost, 2))