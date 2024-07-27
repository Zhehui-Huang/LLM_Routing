import math
from itertools import permutations

# Data initialization
cities_coord = [(54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30), 
                (52, 82), (93, 44), (21, 78), (68, 14), (51, 28), (44, 79), 
                (56, 58), (72, 43), (6, 99)]
city_groups = [[8, 12, 14], [7, 10, 11], [4, 6, 9], [1, 3, 13], [2, 5]]

# Calculate Euclidean distance
def dist(a, b):
    return math.sqrt((cities_coord[a][0] - cities_coord[b][0])**2 + (cities_coord[a][1] - cities_coord[b][1])**2)

# Generate feasible initial tour
def get_initial_tour():
    tour = [0] 
    # Choose the nearest city from each group to the depot
    for group in city_groups:
        nearest = min(group, key=lambda city: dist(0, city))
        tour.append(nearest)
    tour.append(0)  # end at the depot
    return tour

# Compute the total cost of the tour
def tour_cost(tour):
    return sum(dist(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Function performing an iterative local improvement based on city swapping inside tours
def optimize_tour(tour):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if tour[i] != 0 and tour[j] != 0:
                    # Try swapping cities i and j
                    new_tour = tour[:]
                    new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                    if tour_cost(new_tour) < tour
_cost(tour):
                        tour = new_tour
                        improved = True
    return tour

# Main execution
initial_tour = get_initial_tour()
optimized_tour = optimize_tour(initial_tour)
total_cost = tour_cost(optimized_tour)

# Output results
print("Tour:", optimized_tour)
print("Total travel cost:", total_cost)