import numpy as np
from itertools import permutations

# Positions of all cities including the depot
city_positions = [
    (54, 87),  # Depot city 0
    (21, 84),  # City 1
    (69, 84),  # City 2
    (53, 40),  # City 3
    (54, 42),  # City 4
    (36, 30),  # City 5
    (52, 82),  # City 6
    (93, 44),  # City 7
    (21, 78),  # City 8
    (68, 14),  # City 9
    (51, 28),  # City 10
    (44, 79),  # City 11
    (56, 58),  # City 12
    (72, 43),  # City 13
    (6, 99)    # City 14
]

# Number of cities to visit including depo
k = 8

def euclidean_distance(pos1, pos2):
    return np.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)

def calculate_total_distance(tour):
    return sum(euclidean_distance(city_positions[tour[i]], city_positions[tour[i+1]]) for i in range(len(tour)-1))

def find_best_tour():
    best_tour = None
    min_distance = float('inf')
    
    for subset in permutations(range(1, len(city_positions)), k-1):
        tour = [0] + list(subset) + [0]
        distance = calculate_total_distance(tour)
        if distance < min_distance:
            min_distance = distance
            best_tour = tour
            
    return best_tour, min_distance

# Find the best tour
best_tour, min_distance = find_best_tour()

# Output the results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_distance:.2f}")