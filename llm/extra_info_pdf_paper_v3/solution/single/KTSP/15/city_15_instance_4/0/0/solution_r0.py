import random
from itertools import permutations
import math

# City coordinates (indexed from 0 to 14)
cities = {
    0: (35, 40),
    1: (39, 41),
    2: (81, 30),
    3: (5, 50),
    4: (72, 90),
    5: (54, 46),
    6: (8, 70),
    7: (97, 62),
    8: (14, 41),
    9: (70, 44),
    10: (27, 47),
    11: (41, 74),
    12: (53, 80),
    13: (21, 21),
    14: (12, 39)
}

def calculate_distance(city1, city2):
    """Calculate Euclidean distance between two cities."""
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def total_tour_distance(tour):
    """Calculate total distance of a given tour."""
    return sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

def find_best_tour():
    best_tour = None
    shortest_distance = float('inf')
    
    # Select initial random subset of 11 cities (excluding depot city 0, include it separately)
    selected_cities = random.sample(range(1, 15), 11)
    selected_cities.insert(0, 0)  # Insert depot city at the start
    selected_cities.append(0)  # Append depot city to complete the tour
    
    # Generate all permutations of the selected cities (excluding the fixed depot city at start/end)
    for perm in permutations(selected_cities[1:-1]):
        current_tour = [0] + list(perm) + [0]
        current_distance = total_tour_distance(current_tour)
        if current_distance < shortest_distance:
            best_tour = current_tour
            shortest_distance = current_distance
            
    return best_tour, shortest_oistance

# Compute the best tour using the heuristic approach
best_tour, total_cost = find_best_tour()

# Print the outputs as specified
print("Tour:", best_tour)
print("Total travel cost:", total_cost)