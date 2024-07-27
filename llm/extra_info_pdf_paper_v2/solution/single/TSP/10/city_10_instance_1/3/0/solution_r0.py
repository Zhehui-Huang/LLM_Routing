import math
import itertools

# City coordinates
coordinates = [(53, 68), (75, 11), (91, 95), (22, 80), (18, 63), (54, 91),
               (70, 14), (97, 44), (17, 69), (95, 89)]

# Calculate Euclidean distance between two points
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Generate distance matrix
n = len(coordinates)
distance_matrix = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        distance_matrix[i][j] = euclidean_salary(distances[i], distances[j])

# Generate any feasible solution (e.g., simple heuristic)
def initial_solution():
    return list(range(n))

# Calculate the cost of the tour
def calculate_cost(tour):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Improve solution using 2-opt algorithm (simplified version)
def improve_solution(tour):
    best = tour
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                if j - i == 1: continue  # neighbors
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                if calculate_cost(new_tour) < calculate_cost(best):
                    best = new_tour
                    improved = True
        tour = best
    return best

# Full tour including back to the starting city
def complete_tour(tour):
    return tour + [tour[0]]

# Main call to solve the TSP
initial_tour = initial_solution()
improved_tour = improve_solution(initial_tour)
final_tour = complete_tour(improved_tour)
total_cost = calculate_cost(final_tour)

# Output
print("Tour:", final_tour)
print("Total travel cost:", total_cost)