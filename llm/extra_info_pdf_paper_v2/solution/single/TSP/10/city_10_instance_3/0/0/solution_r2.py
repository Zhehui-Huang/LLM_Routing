import math
import random

# City coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Function for calculating Euclidean distance
def euclidean_distance(a, b):
    dx = cities[a][0] - cities[b][0]
    dy = cities[a][1] - cities[b][1]
    return math.sqrt(dx * dx + dy * dy)

# Generate an initial random tour
def generate_initial_tour():
    tour = list(cities.keys())
    random.shuffle(tour)
    if tour[0] != 0:
        tour.remove(0)
        tour.insert(0, 0)
    tour.append(0)
    return tour

# Calculate the total cost of the tour
def total_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(tour[i], tour[i+1])
    return total_cost

# Perform a 2-opt swap to improve the tour
def two_opt(tour):
    min_change = True
    while min_change:
        min_change = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                if j - i == 1:  # consecutive nodes
                    continue
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                if total_tour_cost(new_tour) < total_tour_cost(tour):
                    tour = new_tour
                    min_change = True
    return tour

# Main function to solve the TSP
def solve_tsp():
    initial_tour = generate_initial_tour()
    best_tour = two_opt(initial_tour)
    best_cost = total_tour_cost(best_tour)
    return best_tour, best_cost

# Running the solver
tour, cost = solve_tsp()

# Print the shortest tour and the cost
print(f"Tour: {tour}")
print(f"Total travel cost: {cost}")