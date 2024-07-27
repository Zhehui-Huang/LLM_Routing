import math
from itertools import permutations

# Define function to calculate Euclidean distance between two points
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Coordinates of the cities
coords = {
    0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98),
    5: (45, 84), 6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45),
    10: (90, 85), 11: (98, 76), 12: (6, 19), 13: (26, 29), 14: (21, 79),
    15: (49, 23), 16: (78, 76), 17: (68, 45), 18: (50, 28), 19: (69, 9)
}

def find_btsp_solution():
    cities = list(coords.keys())
    min_max_distance = float('inf')
    best_tour = None
    best_total_distance = 0

    for perm in permutations(cities[1:]):  # Generate permutations excluding the depot
        current_perm = [0] + list(perm) + [0]  # Start and end at the depot city
        max_leg_distance = 0
        total_distance = 0

        # Calculate maximum leg distance and total distance for the current permutation
        for i in range(len(current_perm) - 1):
            distance = euclidean_distance(coords[current_perm[i]], coords[current_perm[i + 1]])
            total_distance += distance
            if distance > max_leg_distance:
                max_leg_distance = distance

        if max_leg_distance < min_max_distance:  # Update the best tour if a better max leg distance is found
            min_max_distance = max_leg_distance
            best_tour = current_perm
            best_total_distance = total_distance

    return best_tour, best_total_distance, min_max_distance

# Call function to solve the problem
tour, total_cost, max_distance = find_btsp_solution()

# Output the results
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_distance, 2))