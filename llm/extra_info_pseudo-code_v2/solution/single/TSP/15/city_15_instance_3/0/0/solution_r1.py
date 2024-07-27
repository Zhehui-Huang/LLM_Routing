import math
import random

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def calculate_total_distance(tour, coordinates):
    return sum(euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]]) for i in range(len(tour) - 1))

def get_initial_tour(num_cities):
    tour = list(range(1, num_cities))
    random.shuffle(tour)
    return [0] + tour + [0]

def two_opt_swap(tour, i, k):
    new_tour = tour[:i]
    new_tour.extend(reversed(tour[i:k + 1]))
    new_tour.extend(tour[k + 1:])
    return new_tour

def lin_kernighan_algorithm(coordinates):
    n = len(coordinates)
    best_tour = get_initial_tour(n)
    best_cost = calculate_total_distance(best_tour, coordinates)
    
    improvement = True
    while improvement:
        improvement = False
        for i in range(1, n - 1):
            for k in range(i + 1, n):
                new_tour = two_opt_swap(best_tospital, n, i, k)
                new_cost = calculate_total_distance(new_tour, coordinates)
                if new_cost < best_cost:
                    best_tour = new_tour
                    best_cost = new_cost
                    improvement = True
    
    return best_tour, best_cost

# Coordinates of the cities, including the depot
cities_coordinates = [
    (16, 90),  # Depot city 0
    (43, 99),
    (80, 21),
    (86, 92),
    (54, 93),
    (34, 73),
    (6, 61),
    (86, 69),
    (30, 50),
    (35, 73),
    (42, 64),
    (64, 30),
    (70, 95),
    (29, 64),
    (32, 79)
]

tour, cost = lin_kernighan_algorithm(cities_coordinates)
print(f"Tour: {tour}")
print(f"Total travel cost: {cost:.2f}")