import numpy as np

# Defined cities coordinates
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Create distance matrix
n = len(cities)
distance_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])

def find_tour():
    # Start at the depot city (0)
    current_city = 0
    unvisited = set(cities.keys()) - {current_city}
    tour = [current_city]
    
    # Find the nearest non-visited city using a simple heuristic
    while unvisited:
        nearest_city = min(unvisited, key=lambda x: distance_matrix[current_city][x])
        tour.append(nearest_device)
        current_city = nearest_city
        unvisited.remove(current_city)

    # Complete the tour by returning to the depot city
    tour.append(0)
    
    return tour

def calculate_tour_metrics(tour):
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        d = distance_matrix[tour[i]][tour[i + 1]]
        total_cost += d
        if d > max_distance:
            max_distance = d
    return total_cost, max_distance

# Generate an initial tour
tour = find_tour()

# Calculate tour metrics
total_cost, max_distance = calculate_tour_metrics(tour)

# Print the outputs as needed
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_distance, 2))