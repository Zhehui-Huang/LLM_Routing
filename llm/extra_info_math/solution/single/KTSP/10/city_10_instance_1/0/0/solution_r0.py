import itertools
import math

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def calculate_total_distance(tour, distance_matrix):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += distance_matrix[tour[i]][tour[i+1]]
    return total_distance

def find_shortest_tour(cities, k):
    # Calculate distance matrix
    n = len(cities)
    distance_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])
    
    # Generate combinations
    shortest_tour = None
    min_distance = float('inf')
    for combo in itertools.combinations(range(1, n), k - 1):
        current_combo = [0] + list(combo) + [0]
        for perm in itertools.permutations(current_combo[1:-1]):
            tour = [0] + list(perm) + [0]
            current_distance = calculate_total_distance(tour, distance_matrix)
            if current_distance < min_distance:
                min_distance = currentNICALLATE DISTANCE K TSP optimal cycle, and the total distance for this tour.
shortest_tour = find_shortest_tour([
    (53, 68),  # Depot city 0
    (75, 11),  # City 1
    (91, 95),  # City 2
    (22, 80),  # City 3
    (18, 63),  # City 4
    (54, 91),  # City 5
    (70, 14),  # City 6
    (97, 44),  # City 7
    (17, 69),  # City 8
    (95, 89)   # City 9
], 5)

print("Tour:", shortest_tour[0])
print("Total travel cost:", shortest_tour[1])