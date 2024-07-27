import math
import itertools

# Given city coordinates
coordinates = [
    (14, 77),  # Depot city 0
    (34, 20),
    (19, 38),
    (14, 91),
    (68, 98),
    (45, 84),
    (4, 56),
    (54, 82),
    (37, 28),
    (27, 45),
    (90, 85),
    (98, 76),
    (6, 19),
    (26, 29),
    (21, 79),
    (49, 23),
    (78, 76),
    (68, 45),
    (50, 28),
    (69, 9) 
]

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Distance matrix calculation
num_cities = len(coordinates)
distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(num_cities)] for i in range(num_cities)]

# Heuristic to find a short tour visiting exactly k cities
def find_shortest_tour(k):
    minimum_cost = float('inf')
    best_tour = None
    
    # Generate all combinations of k-1 cities excluding depot (since including depot)
    for cities in itertools.combinations(range(1, num_cities), k-1):
        full_tour = list(cities) + [0]  # Include depot at the start and will add to end later
        full_permutations = itertools.permutations(full_tour)
        
        for perm in full_permutations:
            # Ensure starting from depot
            if perm[0] != 0:
                continue
            
            # Calculate tour cost
            cost = 0
            for i in range(1, k):
                cost += distance_matrix[perm[i-1]][perm[i]]
            cost += distance_matrix[perm[-1]][0]  # Return to depot
            
            if cost < minimum_cost:
                minimum_cost = cost
                best_tour = list(perm) + [0]  # close the tour
    
    return best_tour, minimum_cost

# Given k value is 7 including depot
tour, total_cost = find_shortest_tour(7)

# Output results
print("Tour:", tour)
print("Total travel cost:", total_cost)