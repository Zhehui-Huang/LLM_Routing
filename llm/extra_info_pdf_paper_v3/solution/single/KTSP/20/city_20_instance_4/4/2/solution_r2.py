import math
import random
from itertools import permutations

# Define the coordinates of the cities
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Compute the Euclidean distance between two points
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Generate the distance matrix
distance_matrix = [[0 if i == j else euclidean_distance(cities[i], cities[j]) for j in range(20)] for i in range(20)]

def find_minimal_k_tsp():
    # We need to include the depot city (0) and 15 other cities: total 16 cities
    best_cost = float('inf')
    best_tour = None
    
    # Attempt several random starts
    for attempt in range(100):  # number of random attempts can be adjusted
        selected_cities = [0] + random.sample(range(1, 20), 15)
        
        # Generate all permutations of selected cities and keep the one with minimal cost
        for perm in permutations(selected_cities):
            if perm[0] == 0:  # making sure the tour starts with depot city
                current_cost = sum(distance_matrix[perm[i]][perm[i+1]] for i in range(15)) + distance_matrix[perm[-1]][perm[0]]
                if current_cost < best_cost:
                    best_cost = current_cost
                    best_tour = perm + (perm[0],)  # adding the return to the depot

    return best_tour, best_cost

# Execute the function
tour, total_cost = find_minimal_k_tsp()
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))