import math
import random

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def calculate_total_distance(tour, cities):
    total_distance = 0
    for i in range(1, len(tour)):
        total_distance += euclidean_distance(cities[tour[i-1]], cities[tour[i]])
    total_distance += euclidean_distance(cities[tour[-1]], cities[tour[0]])
    return round(total_distance, 2)

def create_initial_tour(total_cities):
    tour = list(range(1, total_cities))  # Start tours from city 1 to last city
    random.shuffle(tour)
    tour = [0] + tour + [0]  # Start and end at the depot city 0
    return tour

def two_opt(tour, cities):
    best = tour[:]
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                if j - i == 1: continue
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                if calculate_total_distance(new_tour, cities) < calculate_total_distance(best, cities):
                    best = new_tour[:]
                    improved = True
        tour = best[:]
    return best

# Define the cities by their coordinates
cities = [
    (14, 77),  # Depot city 0
    (34, 20),  # City 1
    (19, 38),  # City 2
    (14, 91),  # City 3
    (68, 98),  # City 4
    (45, 84),  # City 5
    (4, 56),   # City 6
    (54, 82),  # City 7
    (37, 28),  # City 8
    (27, 45),  # City 9
    (90, 85),  # City 10
    (98, 76),  # City 11
    (6, 19),   # City 12
    (26, 29),  # City 13
    (21, 79),  # City 14
    (49, 23),  # City 15
    (78, 76),  # City 16
    (68, 45),  # City 17
    (50, 28),  # City 18
    (69, 9)    # City 19
]

# Generate an initial tour and optimize it
initial_tour = create_initial_tour(len(cities))
optimized_tour = two_opt(initial_tour, cities)

print("Tour:", optimized_tour)
print("Total travel cost:", calculate_total_distance(optimized_tall above.
print(city_distances(distance, citiesl_distance, two_distance)))