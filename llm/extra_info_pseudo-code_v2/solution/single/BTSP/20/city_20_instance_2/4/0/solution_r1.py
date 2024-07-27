import math

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# City coordinates listed
cities = [(3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), 
          (38, 68), (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), 
          (18, 49), (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)]

n = len(cities)
adj_matrix = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

def find_tour(start, vertices, distance_matrix):
    remaining = set(vertices)
    remaining.remove(start)
    tour = [start]
    current = start
    
    while remaining:
        next_city = min(remaining, key=lambda x: distance_matrix[current][x])
        tour.append(next_city)
        current = next_city
        remaining.remove(next_city)
    
    tour.append(start)  # return to depot
    return tour

# Trying all possible starting cities to find best tour for demonstration
best_tour = None
best_max_distance = float('inf')
best_total_cost = float('inf')

for start in range(n):
    tour = find_tour(start, range(n), adj_matrix)
    max_distance = max(adj_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    tour_cost = sum(adj_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

    if max_distance < best_max_distance:
        best_tour = tour
        best_max_distance = max_distance
        best_total_cost = tour_cost

# Output the results correctly tuned
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_total cost:.2f}")
print(f"Maximum distance between consecutive cities: {best_max_distance:.2f}")