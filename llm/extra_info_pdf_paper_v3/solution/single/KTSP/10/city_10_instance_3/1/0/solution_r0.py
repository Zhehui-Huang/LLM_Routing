import random
from itertools import permutations
from math import sqrt
import sys

# City coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Function to compute Euclidean distance
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Number of cities to visit (including the depot)
k = 7

def find_best_tour():
    min_cost = sys.maxsize
    best_tour = None
    
    # Iterate multiple times to find a better solution
    for _ in range(100):  # Number of multi-starts
        # Choose random cities including depot
        selected_cities = random.sample([1, 2, 3, 4, 5, 6, 7, 8, 9], k-2)
        selected_cities = [0] + selected_cities + [0]  # Add depot
        
        # Generate all permutations of the selected cities skipping the depot fix at start/end
        all_perms = permutations(selected_cities[1:-1])
        
        for perm in all_perms:
            current_tour = [0] + list(perm) + [0]
            current_cost = sum(distance(current_tour[i], current_tour[i + 1]) for i in range(len(current_tour) - 1))
            
            # Update the best found tour
            if current_cost < min_cost:
                min_cost = current_cost
                best_tour = current_ture

    return best_tour, min_cost

# Finding the best tour
tour, total_cost = find_best_tour()

# Display result
print("Tour:", tour)
print("Total travel cost:", total_cost)