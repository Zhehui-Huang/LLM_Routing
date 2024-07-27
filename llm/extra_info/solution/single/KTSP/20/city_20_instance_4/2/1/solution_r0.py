import math
from itertools import permutations

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# List of cities coordinates (index corresponds to city number)
coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0),
    (11, 10), (69, 22), (28, 11), (70, 2),
    (47, 50), (60, 29), (29, 26), (85, 68),
    (60, 1), (71, 73), (82, 47), (19, 25),
    (75, 9), (52, 54), (64, 72), (14, 89)
]

# Number of cities to visit including the depot
n_cities = 16

# Calculate distances between each pair of cities
distance_matrix = {}
for i in range(len(coordinates)):
    for j in range(len(coordinates)):
        if i != j:
            distance_matrix[(i, j)] = euclidean_distance(
                coordinates[i][0], coordinates[i][1],
                coordinates[j][0], coordinates[j][1]
            )

# Find a preliminary tour using nearest neighbor method
def nearest_neighbor_tour(start, n_cities):
    tour = [start]
    cities_to_visit = set(range(len(coordinates))) - {start}
    
    current_city = start
    while len(tour) < len(coordinates):
        next_city = min(cities_to_visit, key=lambda city: distance_matrix[(current_city, city)])
        if len(tour) == n_cities and next_city == start:
            tour.append(next_city)
            break
        elif len(tour) < n_cities:
            tour.append(next_city)
            cities_to_visit.remove(next_city)
            current_city = next_city
    
    return tour

# Perform 2-opt optimization on the tour
def two_opt(tour):
    improvement = True
    while improvement:
        improvement = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                if j - i == 1: continue  # Consequent points, no need to swap
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                if tour_distance(new_tour) < tour_distance(tour):
                    tour = new_tour
                    improvement = True
                    break
            if improvement:
                break
    return tour

def tour_distance(tour):
    return sum(distance_matrix[(tour[i], tour[i+1])] for i in range(len(tour) - 1))

# Get an initial tour and optimize it
initial_tour = nearest_neighbor_tour(0, n_cities)
optimized_tour = two_opt(initial_tour)
tour_cost = tour_distance(optimized_tour)

print(f"Tour: {optimized_tour}")
print(f"Total travel cost: {tour_cost:.2f}")