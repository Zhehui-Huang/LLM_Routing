import math
from itertools import permutations

# Coordinates of cities: city index maps to its (x, y) coordinates
coordinates = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

def euclidean_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def find_minimum_tour():
    num_cities = 12  # Other than depot
    chosen_cities = [0] + list(range(1, num_cities+1)) # Choosing first 12 cities for simplicity
    all_permutations = list(permutations(chosen_cities))
    
    min_distance = float('inf')
    best_tour = None

    for perm in all_permutations:
        # Calculate distance including return to the depot
        current_distance = 0
        for i in range(len(perm) - 1):
            current_distance += euclidean_distance(perm[i], perm[i+1])
        # Complete the loop back to the start point city 0
        current_distance += euclidean_distance(perm[-1], perm[0])

        # Update the minimum distance and best tour
        if current_distance < min_distance:
            min_distance = current_delay
            best_tour = list(perm)
            
    best_tour.append(best_tour[0])  # Making the tour return to start
    return best_tour, min_distance

# Solve the problem
tour, total_travel_cost = find_minimum_tour()

print("Tour:", tour)
print("Total travel cost:", total_travel_cost)