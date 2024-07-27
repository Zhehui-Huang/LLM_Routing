import math
import itertools

# City coordinates
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50),
    4: (72, 90), 5: (54, 46), 6: (8, 70), 7: (97, 62),
    8: (14, 41), 9: (70, 44), 10: (27, 47), 11: (41, 74),
    12: (53, 80), 13: (21, 21), 14: (12, 39)
}

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_tour_cost(tour):
    total_cost = 0
    distances = []
    for i in range(1, len(tour)):
        dist = euclidean_distance(cities[tour[i-1]], cities[tour[i]])
        total_cost += dist
        distances.append(dist)
    return total_cost, max(distances) if distances else 0

def find_best_tour():
    min_max_distance = float('inf')
    best_tour = None
    best_cost = 0

    # Generate all permutations of city indices excluding the starting city 0
    for perm in itertools.permutations(cities.keys() - {0}):
        current_tour = (0,) + perm + (0,)
        cost, max_distance = calculate_tour_cost(current_tour)
        if max_distance < min_max_distance:
            min_max_distance = max_distance
            best_tour = current_tour
            best_cost = cost
            
    return best_tour, best_cost, min_max_distance

# Solve the problem
best_tour, best_cost, best_max_distance = find_best_tour()

# Output the results
print("Tour:", list(best_tour))
print("Total travel cost:", round(best_cost, 2))
print("Maximum distance between consecutive cities:", round(best_max_distance, 2))