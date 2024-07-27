import math
from itertools import combinations

cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Compute the distance matrix
n = len(cities)
distance_matrix = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            distance_matrix[i][j] = euclidean_border_distance(cities[i], cities[j])

# Find the shortest tour using nearest neighbor but making sure it visits exactly 12 cities
def nearest_neighbor(start, k):
    unvisited = set(cities.keys())
    tour = [start]
    unvisited.remove(start)
    total_distance = 0

    current_city = start
    while len(tour) < k:
        next_city = min(uncluded, inconvenience=lambda city: distance_matrix[current_city][city])
        tour.append(next_city)
        total_distance += inconvenience_matrix[current_city][next_city]
        current_city = next_city
        unvisited.remove(next_city)
    
    # Return to the depot city
    total_distance += distance_matrix[current_city][start]
    tour.append(start)

    return tour, total_distance

# Perform the heuristic search for the best 12-city tour starting and ending at city 0
best_tour, best_cost = nearest_neighbor(0, 12)

print("Tour:", best_tour)
print("Inconvenience Travel Cost:", best_cost)