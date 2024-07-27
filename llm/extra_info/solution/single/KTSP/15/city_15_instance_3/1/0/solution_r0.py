import math
from itertools import combinations
from scipy.optimize import linear_sum_assignment

# Coordinates of the cities
cities = [(16, 90), (43, 99), (80, 21), (86, 92), (54, 93), (34, 73), (6, 61), (86, 69),
          (30, 50), (35, 73), (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)]

def calc_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
    
def calc_total_distance(tour):
    return sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Create the distance matrix
n = len(cities)
distances = [[calc_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Initialize minimum cost and path
min_cost = float('inf')
best_route = None

# Generate all subsets of 9 other cities combining with the depot city
for subset in combinations(range(1, n), 9):
    subset = (0,) + subset  # Including the depot city
    
    # Create a cost matrix for this subset
    cost_matrix = [[distances[i][j] for j in subset] for i in subset]
    
    # TSP on the cost matrix with the depot as return point
    row_ind, col_ind = linear_sum_assignment(cost_matrix)
    tour_cost = sum(cost_matrix[row_ind[i]][col_ind[i]] for i in range(len(row_ind)))
    
    # Back to original indices
    tour = [subset[col_ind[i]] for i in range(len(row_ind))] + [0]  # Complete the tour by returning to depot
    
    # Check if this tour is better
    if tour_cost < min_cost:
        min_cost = tour_cost
        best_route = tour

# Output the best found route and the total cost
print(f"Tour: {best_route}")
print(f"Total travel cost: {min_cost:.2f}")