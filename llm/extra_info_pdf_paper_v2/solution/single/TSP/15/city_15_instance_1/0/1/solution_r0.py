import math
from itertools import permutations

# City coordinates
cities = [(29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57), 
          (57, 30), (36, 12), (93, 43), (17, 36), (4, 60), (78, 82), 
          (83, 96), (60, 50), (98, 1)]

def euclidean_distance(a, b):
    """ Computes the Euclidean distance between two points a and b """
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Distance matrix
n = len(cities)
distance_matrix = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        distance_matrix[i][j] = euclid ean_distance(cities[i], cities[j])

# Heuristic: Nearest Neighbor Tour
def nearest_neighbor():
    tour = [0]
    used = [False] * n
    used[0] = True

    current_city = 0
    count = 1
    while count < n:
        next_city = None
        min_dist = float('inf')
        for j in range(1, n):
            if not used[j] and distance_matrix[current_city][j] < min_dist:
                min_dist = distance_matrix[current_city][j]
                next_city = j
        tour.append(next_city)
        used[next_city] = True
        current_city = next_city
        count += 1
    
    tour.append(0)  # returning to the depot
    return tour

# Calculate the total cost of the tour
def calculate_cost(tour):
    cost = 0
    for i in range(1, len(tour)):
        cost += distance_matrix[tour[i-1]][tour[i]]
    return cost

# Improvement heuristic: 2-opt Swap
def two_opt(tour):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i+2, len(tour) - 1):
                if distance_matrix[tour[i-1]][tour[i]] + distance_matrix[tour[j]][tour[j+1]] > \
                   distance_matrix[tour[i-1]][tour[j]] + distance_matrix[tour[i]][tour[j+1]]:
                    tour[i:j] = tour[i:j][::-1]  # reverse the segment
                    improved = True
    return tour

# Perform the nearest neighbor tour, then improve it with 2-opt.
initial_tour = nearest_neighbor()
optimized_tour = two_opt(initial_tour)
total_cost = calculate_cost(optimized_tour)

# Output the solutions
print(f"Tour: {optimized_tour}")
print(f"Total travel cost: {total_cost}")