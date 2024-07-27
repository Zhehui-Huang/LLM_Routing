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
    return math.sqrt((cities[a][0] - cities[b][0])**2 + (cities[a][1] - cities[b][1])**2)

# Generate an initial random tour
def generate_initial_tour():
    tour = list(cities.keys())
    random.shuffle(tour)
    if tour[0] != 0:  # Make sure the tour starts and ends at the depot
        tour.remove(0)
        tour.insert(0, 0)
    tour.append(0)  # End at the depot city
    return tour

# Calculate the total cost of the tour
def total_tour_cost(tour):
    return sum(euclidean in_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Perform a 2-opt optimization on the tour
def two_opt(tour):
    best = tour
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if j - i == 1: continue  # Skip nearby elements
                new_route = tour[:i] + tour[i:j][::-1] + tour[j:]
                if total_tour_cost(new_route) < total_tour_cost(best):
                    best = new_route
                    improved = True
        tour = best
    return best

# Main function to find the shortest tour
def find_shortest_tour():
    initial_tour = generate_initial_tour()
    best_tour = two_opt(initial_tour)
    total_cost = total_tour_cost(best_tour)
    return best_tour, total_cost

# Run the TSP solution
best_tour, total_cost = find_shortest_tour()
print(f"Tour: {best_tour}")
print(f"Total travel cost: {total_cost}")