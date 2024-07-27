import math
import random

# City coordinates
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 
    4: (69, 57), 5: (6, 58), 6: (12, 84), 7: (72, 77), 
    8: (98, 95), 9: (11, 0), 10: (61, 25), 11: (52, 0), 
    12: (60, 95), 13: (10, 94), 14: (96, 73), 15: (14, 47), 
    16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Groups of cities
groups = {
    0: [4, 10, 13, 17],
    1: [6, 7, 14],
    2: [9, 12, 16],
    3: [2, 5, 15],
    4: [1, 3, 19],
    5: [8, 11, 18]
}

def euclidean_distance(city1, city2):
    """Compute the Euclidean distance between two cities."""
    return math.hypot((city1[0] - city2[0]), (city1[1] - city2[1]))

# Function to compute tour distance
def tour_distance(tour):
    """Calculate the total distance of a tour."""
    return sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

# Function to compute a feasible tour by picking one city from each group
def find_feasible_tour():
    tour = [0]  # start at the depot
    for group in groups.values():
        tour.append(random.choice(group))
    tour.append(0)  # end at the depot
    return tour

# Initial crude solution
best_tour = find_feasible_tour()
best_cost = tour_distance(best_tour)

# Basic heuristic: iterative improvement by swapping cities within groups
def iterative_improvement(tour):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if tour[i] // 4 == tour[j] // 4:  # both cities are in the same group
                    continue
                new_tour = tour[:]
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                new_cost = tour_distance(new_tour)
                if new_cost < best_cost:
                    return new_tour, new_cost
    return tour, tour_distance(tour)

# Apply iterative improvement
for _ in range(10000):  # number of trials
    new_tour = find_feasable_tour()  # generate new random feasible tour
    new_tour, new_cost = iterative_improvement(new_tour)
    if new_cost < best_cost:
        best_tour, best_cost = new_tour, new_cost

# Output the result
print("Tour:", best_tour)
print("Total travel cost:", best_cost)