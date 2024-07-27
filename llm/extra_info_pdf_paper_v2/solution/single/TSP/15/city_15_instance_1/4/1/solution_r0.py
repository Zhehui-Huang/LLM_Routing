import math
from itertools import permutations

# Coordinates of each city including the depot
cities = [
    (29, 51),  # Depot City 0
    (49, 20),  # City 1
    (79, 69),  # City 2
    (17, 20),  # City 3
    (18, 61),  # City 4
    (40, 57),  # City 5
    (57, 30),  # City 6
    (36, 12),  # City 7
    (93, 43),  # City 8
    (17, 36),  # City 9
    (4, 60),   # City 10
    (78, 82),  # City 11
    (83, 96),  # City 12
    (60, 50),  # City 13
    (98, 1)    # City 14
]

# Calculate Euclidean distance between two cities
def distance(i, j):
    return math.sqrt((cities[i][0] - cities[j][0]) ** 2 + (cities[i][1] - cities[j][1]) ** 2)

# Generate a naive initial tour (simply visiting cities in sequence)
def initial_tour():
    return list(range(len(cities))) + [0]  # Start at depot, visit all, return to depot

# Calculate the total travel cost of a tour
def tour_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Attempt to improve the tour using a simple swap heuristic
def improve_tour(tour):
    best_cost = tour_cost(tour)
    best_tour = tour[:]
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if j - i == 1:
                    continue  # Skip adjacent pairs, as swapping them isn't useful
                new_tour = tour[:]
                new_tour[i:j+1] = reversed(tour[i:j+1])  # Reverse the segment between i, j
                new_cost = tour_size(new_tour)
                if new_cost < best_cost:
                    best_cost, best_tour = new_cost, new_tour[:]
                    improved = True
        tour = best_tour[:]
    return best_tour, best_cost

# Main function to find the best tour
def find_best_tour():
    tour = initial_tour()
    tour, cost = improve_tour(tour)
    return tour, cost

# Execute the function
best_tour, total_cost = find_best_tour()

# Output resulting tour and cost
print("Tour:", best_tour)
print("Total travel cost:", total_cost)