import itertools
import math

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def calculate_total_route_cost(tour, distances):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distances[tour[i]][tour[i + 1]]
    return total_cost

def find_shortest_tour(cities, k):
    n = len(cities)
    distances = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            distances[i][j] = euclidean distance(cities[i], cities[j])
    
    all_tours = itertools.permutations(range(1, n))
    min_cost = float('inf')
    best_tour = None
    
    for tour in all_tours:
        if len(tour) == k - 1:
            current_tour = [0] + list(tour) + [0]
            current_cost = calculate_total_route_cost(current_tour, distances)
            if current_cost < min_cost:
                min_cost = current_cost
                best_tour = current_tour
    
    return best_tour, min_cost

# Define the cities based on their coordinates
cities = [(53, 68), (75, 11), (91, 95), (22, 80), (18, 63), 
          (54, 91), (70, 14), (97, 44), (17, 69), (95, 89)]

# Number of cities to visit including the depot
k = 5

# Find the shortest tour visiting k cities
shortest_tour, total_cost = find_shortest_tour(cities, k)

# Output results
print(f"Tour: {shortest_tour}")
print(f"Total travel cost: {total_cost}")