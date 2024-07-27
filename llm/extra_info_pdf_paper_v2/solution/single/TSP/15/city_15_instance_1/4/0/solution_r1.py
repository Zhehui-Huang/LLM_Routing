import math
import random

# City coordinates
cities = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61),
    5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
    10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# 2-opt Swap function
def two_opt(route):
    best = route
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):
                if j - i == 1: continue
                new_route = route[:i] + route[i:j][::-1] + route[j:]
                if sum(distance(new_route[k], new_route[k + 1]) for k in range(len(new_route) - 1)) < sum(distance(best[k], best[k + 1]) for k in range(len(best) - 1)):
                    best = new_route
                    improved = True
        route = best
    return best

# Generate an initial random tour
def initial_tour():
    tour = list(cities.keys())
    random.shuffle(tour)
    if tour[0] != 0:
        tour.insert(0, tour.pop(tour.index(0)))
    tour.append(0)
    return tour

# Iteratively improve the tour
def minimize_tour():
    tour = initial_tour()
    tour = two_opt(tour)
    min_distance = sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    for _ in range(1000):  # Number of iterations
        new_tour = two_opt(initial_tour())
        new_distance = sum(distance(new_tour[i], new_tour[i + 1]) for i in range(len(new_tour) - 1))
        if new_distance < min_distance:
            min_distance = new_distance
            tour = new_tour
    return tour, min_distance

# Execute the function to find the tour and distance
best_tour, best_distance = minimize_tour()

# Output the results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_distance:.2f}")