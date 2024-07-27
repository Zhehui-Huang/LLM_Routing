import math
from itertools import permutations

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def total_distance(tour, coordinates):
    distance = 0
    for i in range(1, len(tour)):
        x1, y1 = coordinates[tour[i - 1]]
        x2, y2 = coordinates[tour[i]]
        distance += euclidean_distance(x1, y1, x2, y2)
    return distance

def find_initial_tour(depot, coordinates, k):
    distances = [(i, euclidean_distance(coordinates[depot][0], coordinates[depot][1], coord[0], coord[1])) for i, coord in enumerate(coordinates)]
    sorted_cities = sorted(distances, key=lambda x: x[1])[1:k]  # Exclude the depot itself and pick closest k-1 cities
    return [depot] + [city[0] for city in sorted_cities] + [depot]

def optimize_tour(tour, coordinates):
    best_tour = tour
    best_distance = total_distance(tour, coordinates)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                new_tour = tour[:i] + tour[i:j+1][::-1] + tour[j+1:]
                new_distance = total_distance(new_tour, coordinates)
                if new_distance < best_distance:
                    best_tour, best_distance = new_tour, new_distance
                    improved = True
        if improved:
            tour = best_tour
    return best_tour, best_distance

coordinates = {
    0: (90, 3), 1: (11, 17), 2: (7, 27), 3: (95, 81), 4: (41, 54),
    5: (31, 35), 6: (23, 95), 7: (20, 56), 8: (49, 29), 9: (13, 17)
}
k = 6
initial_tour = find_initial_tour(0, coordinates, k)
optimized_tour, optimized_distance = optimize_tour(initial_tour, coordinates)

print(f"Tour: {optimized_tour}")
print(f"Total travel cost: {optimized_distance:.2f}")