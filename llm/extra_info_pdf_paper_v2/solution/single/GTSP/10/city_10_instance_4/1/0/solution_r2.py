import math
from itertools import product

# City coordinates: index 0 is the depot
coordinates = [
    (79, 15), (79, 55), (4, 80), (65, 26), (92, 9), (83, 61), 
    (22, 21), (97, 70), (20, 99), (66, 62)
]

# Groups of cities
groups = [
    [1, 4], [2, 6], [7], [5], [9], [8], [3]
]

# Calculate Euclidean distance between two points
def calc_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Generate all possible representative sets from each group
def generate_representative_sets():
    # Using product to simulate picking one city from each group
    product_of_groups = product(*groups)
    return list(product_of_groups)

def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calc_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
    return total_cost

# Find the shortest tour from generated representative city sets
def find_best_tour(all_sets):
    best_tour = None
    best_cost = float('inf')
    depot = 0  # Depot position in the coordinates list
    for rep_set in all_sets:
        # Start and end at the depot city
        current_tour = [depot] + list(rep_set) + [depot]
        current_cost = calculate_tour_cost(current_tour)
        if current_cost < best_cost:
            best_tour = current_tour
            best_cost = current_cost
    return best_tour, best_cost

# Main computation
representative_sets = generate_representative_sets()
optimal_tour, optimal_cost = find_best_tour(representative_sets)

# Output
print("Tour:", optimal_tour)
print("Total travel cost:", optimal_cost)