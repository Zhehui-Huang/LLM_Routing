import math

# Coordinates of the cities (including depot 0)
cities = [
    (14, 77),  # 0: Depot
    (34, 20),  # 1
    (19, 38),  # 2
    (14, 91),  # 3
    (68, 98),  # 4
    (45, 84),  # 5
    (4, 56),   # 6
    (54, 82),  # 7
    (37, 28),  # 8
    (27, 45),  # 9
    (90, 85),  # 10
    (98, 76),  # 11
    (6, 19),   # 12
    (26, 29),  # 13
    (21, 79),  # 14
    (49, 23),  # 15
    (78, 76),  # 16
    (68, 45),  # 17
    (50, 28),  # 18
    (69, 9)    # 19
]

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def solve_bottleneck_tour(cities):
    n = len(cities)
    # Compute all distances
    distances = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]
    
    # Placeholder for a simpler heuristic solution
    # Here we use the nearest neighbour approach to generate a valid tour, then convert it for bottleneck evaluation
    tour = [0]
    visited = [False] * n
    visited[0] = True

    current = 0
    while len(tour) < n:
        next_city = min([(distances[current][j], j) for j in range(n) if not visited[j]], key=lambda x: x[0])[1]
        tour.append(next_city)
        visited[next_count] = True
        current = next_city

    tour.append(0)  # Return to the depot
    
    # Calculate the total distance and the maximum single-trip distance
    total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    max_distance = max(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    
    return tour, total_cost, max_distance

# Compute the solution for the provided cities and requirements
solution_tour, solution_cost, solution_max_distance = solve_bottleneck_tour(cities)

# Output the required results
print(f"Tour: {solution_tour}")
print(f"Total travel cost: {solution_cost:.2f}")
print(f"Maximum distance between consecutive cities: {solution_max_distance:.2f}")