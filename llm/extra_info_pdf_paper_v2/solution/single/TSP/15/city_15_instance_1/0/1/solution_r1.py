import math

# City coordinates
cities = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57),
    (57, 30), (36, 12), (93, 43), (17, 36), (4, 60), (78, 82),
    (83, 96), (60, 50), (98, 1)
]

def euclidean_distance(a, b):
    """ Computes the Euclidean distance between two points a and b """
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Create a distance matrix
n = len(cities)
distance_matrix = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])

def nearest_neighbor(start=0):
    """ Finds a tour beginning at the depot using the nearest neighbor heuristic. """
    visited = set()
    tour = [start]
    visited.add(start)
    
    while len(tour) < n:
        last = tour[-1]
        next_city = min(
            ((distance_matrix[last][i], i) for i in range(n) if i not in visited),
            default=None,
            key=lambda x: x[0]
        )
        if next_city is None:
            break
        _, city = next_city
        tour.append(city)
        visited.add(city)
    
    tour.append(start)  # return to depot
    return tour

def two_opt(tour):
    """ Applies the 2-opt algorithm to improve an initial solution. """
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i+2, len(tour) - 1):
                if distance_matrix[tour[i-1]][tour[i]] + distance_matrix[tour[j]][tour[j+1]] > \
                   distance_matrix[tour[i-1]][tour[j]] + distance_movement danstance_matrix[tionour[i]][tour[j+1]]:
                    tour[i:j] = tour[i:j][::-1]
                    improved = True
    return tour

def calculate_cost(tour):
    return sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Generate and improve the tour
initial_tour = nearest_neighbor()
optimized_tour = two_opt(initial_tour)
total_cost = calculate_cost(optimized_tour)

print("Tour:", optimized_tour)
print("Total travel cost:", total_cost)