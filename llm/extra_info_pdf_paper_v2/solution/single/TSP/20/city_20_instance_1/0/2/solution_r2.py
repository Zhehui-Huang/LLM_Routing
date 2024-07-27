import math

# Coordinates definition for the cities including the depot city at index 0
cities = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98),
    (45, 84), (4, 56), (54, 82), (37, 28), (27, 45),
    (90, 85), (98, 76), (6, 19), (26, 29), (21, 79),
    (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def calculate_total_distance(tour, dist_matrix):
    total = 0
    for i in range(len(tour)-1):
        total += dist_matrix[tour[i]][tour[i+1]]
    return total

def find_initial_tour(dist_matrix):
    n = len(dist_matrix)
    unvisited = set(range(1, n))
    tour = [0]
    current = 0
    while unvisited:
        next_city = min(unvisited, key=lambda city: dist_matrix[current][city])
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city
    tour.append(0)  # Returning to the depot
    return tour

def two_opt(tour, dist_matrix):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if j - i == 1: continue
                if dist_matrix[tour[i-1]][tour[i]] + dist_matrix[tour[j]][tour[j+1]] > dist_matrix[tour[i-1]][tour[j]] + dist_matrix[tour[i]][tour[j+1]]:
                    tour[i:j+1] = tour[i:j+1][::-1]
                    improved = True
    return tour

# Compute the distance matrix
distance_matrix = [[euclidean_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

# Find an initial tour using the nearest neighbor heuristic
tour = find_initial_tour(distance_matrix)

# Apply the 2-opt improvement heuristic
optimized_tour = two_opt(tour, distance_matrix)

# Calculate the total distance of the optimized tour
total_travel_cost = calculate_total_distance(optimized_tour, distance_add_matrix)

print("Tour:", optimized_tour)
print("Total travel cost:", total_travel_cost)