import math
import random

# Coordinates for depot and each city
coordinates = [
    (84, 67), (74, 40), (71, 13), (74, 82), (97, 28), 
    (0, 31), (8, 62), (74, 56), (85, 71), (6, 76)
]

# Groups of cities
city_groups = [[7, 9], [1, 3], [4, 6], [8], [5], [2]]

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def calculate_tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    return cost

def generate_initial_tour(groups, depot):
    # Generate a random initial tour by selecting one city from each group
    tour = [depot]
    for group in groups:
        tour.append(random.choice(group))
    tour.append(depot)  # return to depot
    return tour

def local_optimize(tour):
    # Simple local optimization using 2-opt strategy
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 2, len(tour) - 1):
                if tour[i] != tour[j]:
                    new_tour = tour[:i] + tour[i:j+1][::-1] + tour[j+1:]
                    if calculate_tour_cost(new_tour) < calculate_tour_cost(tour):
                        tour = new_tour
                        improved = True
    return tour

def find_best_tour(groups, depot, iterations=1000):
    best_tour = None
    best_cost = float('inf')
    for _ in range(iterations):
        tour = generate_initial_tour(groups, depot)
        tour = local_optimize(tour)
        cost = calculate_tour_cost(tour)
        if cost < best_cost:
            best_cost = cost
            best_tour = tour
    return best_tour, best_cost

# Find the best tour
best_tour, total_cost = find_best_tour(city_groups, 0)

# Print the results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {total_cost:.2f}")