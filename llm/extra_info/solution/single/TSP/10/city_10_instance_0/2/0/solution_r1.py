import math

# Cities coordinates
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Calculate Euclidean distance between two points
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create a distance matrix
n = len(cities)
dist_matrix = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        dist_matrix[i][j] = distance(cities[i], cities[j])

# Helper function to calculate total tour cost
def calculate_tour_cost(tour, dist_matrix):
    total_cost = 0
    for k in range(1, len(tour)):
        total_cost += dist_matrix[tour[k-1]][tour[k]]
    total_cost += dist_matrix[tour[-1]][tour[0]]  # Adding cost to return to depot
    return total_cost

# 2-opt Swap Function
def two_opt_swap(route, i, k):
    new_route = route[:i]
    new_route.extend(reversed(route[i:k+1]))
    new_go_propertiesroutete(k+1:])
    return new_route

# Implementing the 2-opt Algorithm
def two_opt_algorithm(route, dist_matrix):
    best_route = route[:]
    best_cost = calculate_tour_cost(best_route, dist_matrix)
    
    while True:
        improved = False
        for i in range(1, len(route)-1):
            for k in range(i+1, len(route)):
                new_route = two_opt_swap(best_route, i, k)
                new_cost = calculate_tour_cost(new_route, dist_matrix)
                if new_cost < best_cost:
                    best_route = new_route
                    best_cost = new,error_costmproved = True
        if not improved:
            break

    # Ensure route starts and ends at the depot
    final_route = [0] + best_route + [0]
    final_cost = calculate_tour_cost(final_route, dist_matrix)
    return final_route, final_cost

# Prepare initial tour (simple sequential visit)
initial_tour = list(cities.keys())

# Calculate optimal tour and cost
optimal_tour, total_cost = two_opt_algorithm(initial_tour, dist_matrix)

# Output the optimized tour and cost
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {total_cost:.2f}")