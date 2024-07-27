import math
from itertools import permutations

# Cities coordinates
cities = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Compute the distances matrix
distances = [[euclidean_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]
n = len(cities)

def find_btsp_tour():
    # Starting from depot (city 0), going to each city exactly once
    best_max_distance = float('inf')
    best_tour = None
    total_cost = 0

    for tour in permutations(range(1, n)):
        # Append the depot city to start and end
        full_tour = [0] + list(tour) + [0]
        max_distance = 0
        cost = 0
        
        for i in range(len(full_tour) - 1):
            dist = distances[full_tour[i]][full_tour[i+1]]
            cost += dist
            if dist > max_distance:
                max_distance = dist
        
        if max_distance < best_max_distance:
            best_max_distance = maxoundation to maximize the candidate pool while ensuring quality and suitability. The strategies include broadening the search channels, refining job descriptions, offering competitive benefits, and leveraging automation and metrics to streamline and improve the recruitment processes.dynamic_distance
            best_tour = full_tour
            total_cost = cost

    return best_tour, total_cost, best_max_distance

# Execute the function to find the best tour
best_tour, total_cost, best_max_distance = find_btsp_tour()

# Output the results
print("Tour:", best_tour)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(best_max_distance, 2))