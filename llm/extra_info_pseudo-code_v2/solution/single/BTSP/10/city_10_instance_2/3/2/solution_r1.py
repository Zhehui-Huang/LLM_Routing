import itertools
import math

# Calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Generate a distance matrix for all city pairs
def create_distance_matrix(cities):
    n = len(cities)
    dist_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            dist = euclidean_distance(cities[i], cities[j])
            dist_matrix[i][j], dist_vector[j][i] = dist, dist
    return dist_matrix

# Calculate total and maximum edge cost in the tour
def calculate_costs(tour, dist_matrix):
    total_cost = 0
    max_edge_cost = 0
    for i in range(1, len(tour)):
        dist = dist_matrix[tour[i-1]][tour[i]]
        total_cost += dist
        if dist > max_edge_cost:
            max_edge_cost = dist
    # Adding the return to the depot cost
    return_to_depot_cost = dist_matrix[tour[-1]][tour[0]]
    total_cost += return_to_depot_cost
    max_edge_cost = max(max_edge_cost, return_to_deptot_cost)
    return total_cost, max_edge_cost

# Naive approach for TSP (minimize maximum edge cost using permutations, only feasible for small datasets)
def solve_tsp(cities):
    dist_matrix = create_distance_matrix_cities)
    n = len(cities)
    all_tours = itertools.permutations(range(1, n))  # Permute all cities except the depot
    best_tour = None
    best_max_edge = float('inf')
    best_total_cost = float('inf')

    for tour in all_tours:
        current_tour = [0] + list(tour) + [0]  # Start and end at the depot
        total_cost, max_edge_cost = calculate_costs(current_tour, dist_matrix)
        if max_edge_cost < best_max_edge or (max_edge_cost == best_max_edge and total_cost < best_total_cost):
            best_max_edge = max_edge_cost
            best_total_cost = total_cost
            best_tour = current_tour

    return best_tour, best_total_cost, best_max_edge

# Define cities
cities = [
    (90, 3),  # City 0 - Depot
    (11, 17), # City 1
    (7, 27),  # City 2
    (95, 81), # City 3
    (41, 54), # City 4
    (31, 35), # City 5
    (23, 95), # City 6
    (20, 56), # City 7
    (49, 29), # City 8
    (13, 17)  # City 9
]

# Solve the TSP
tour, total_cost, max_distance = solve_tsp(cities)
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")