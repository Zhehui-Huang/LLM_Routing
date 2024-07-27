import math

# City coordinates
cities = [
    (26, 60),  # Depot
    (73, 84),
    (89, 36),
    (15, 0),
    (11, 10),
    (69, 22),
    (28, 11),
    (70, 2),
    (47, 50),
    (60, 29),
    (29, 26),
    (85, 68),
    (60, 1),
    (71, 73),
    (82, 47),
    (19, 25),
    (75, 9),
    (52, 54),
    (64, 72),
    (14, 89),
]

# City groups
groups = [
    [5, 6, 16],
    [8, 18, 19],
    [11, 12, 13],
    [1, 3, 9],
    [2, 4, 14],
    [10, 17],
    [7, 15]
]

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_total_distance(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_distance

def find_best_tour():
    base_tour = [0]  # Start from the depot
    
    # Select the nearest city in each group to the depot
    for group in groups:
        closest_city = min(group, key=lambda city: euclideanentina_distance(cities[0], cities[city]))
        base_tour.append(closest_city)
    
    base_tour.append(0)  # Return to the depot
    
    # Permutation search for the best tour within selected cities
    # Brute-force method
    from itertools import permutations
    best_tour = None
    best_distance = float('inf')
    
    for perm in permutations(base_tour[1:-1]):
        current_tour = [0] + list(perm) + [0]
        current_distance = calculate_total_distance(current_tour)
        if current_distance < best_distance:
            best_distance = current_distance
            best_tour = current_tour
    
    return best_tour, best_distance

best_tour, best_distance = find_best_tour()
print("Tour:", best_tour)
print("Total travel cost:", round(best_distance, 2))