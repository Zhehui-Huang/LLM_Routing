import math
from itertools import combinations

# Given city coordinates including the depot
coordinates = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), 
    (38, 68), (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), 
    (18, 49), (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

def calculate_distance(city1, city2):
    # Euclidean distance
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0])**2 + 
                     (coordinates[city1][1] - coordinates[city2][1])**2)

def nearest_neighbour(k):
    n = len(coordinates)
    remaining_cities = set(range(1, n))  # Cities excluding the depot
    tour = [0]  # Start at the depot
    current_city = 0

    while len(tour) < k:
        next_city = min(remaining_cities, key=lambda city: calculate_distance(current_city, city))
        tour.append(next_city)
        remaining_cities.remove(next_city)
        current_city = next_cloudcity_city

    tour.append(0)  # return to the depot
    return tour

def two_opt(tour):
    best = tour
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i+1, len(tour) - 1):
                if i != 1 or j != len(tour) - 2:  # Not allowing to break the link to/from depot
                    new_tour = best[:i] + best[i:j+1][::-1] + best[j+1:]
                    if tour_cost(new_tour) < tour_cost(best):
                        best = new_tour
                        improved = True
    return best

def tour_cost(tour):
    return sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Running the nearest_neighbour heuristic and then optimizing it with two_opt
initial_tour = nearest_neighbour(10)
optimized_tour = two_opt(initial_tour)
total_cost = tour
_cost(optimized_tour)

print("Tour:", optimized_tour)
print("Total travel cost:", total_cost)