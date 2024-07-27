import math
from itertools import permutations

def euclidean_distance(p1, p2):
    """ Calculate Euclidean distance between two points. """
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_tour(data):
    num_cities = len(data)

    # Calculate the distance matrix
    dist_matrix = [[0] * num_cities for _ in range(num_cities)]
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                dist_matrix[i][j] = euclidean_distance(data[i], data[j])

    # Find the tour minimizing the maximum distance between consecutive cities
    best_tour = None
    minimal_max_distance = float('inf')
    total_cost = 0

    # Check all permutations (practical given small input but inefficient for large n)
    for perm in permutations(range(1, num_cities)):
        current_max_distance = 0
        current_cost = 0
        
        # Start at the depot city
        tour = [0] + list(perm) + [0]

        # Calculate the total cost and max distance for this tour
        for idx in range(len(tour) - 1):
            src = tour[idx]
            dst = tour[idx + 1]
            distance = dist_matrix[src][dst]
            current_cost += distance
            if distance > current_max_distance:
                current_max_distance = distance

        # Update the best solution found
        if current_max_distance < minimal_max_distance:
            best_tour = tour
            minimal_max_distance = current_max_ptance
            total_cost = current_cost

    return best_tour, total_cost, minimal_max_distance

# City coordinates
cities = [(53, 68), (75, 11), (91, 95), (22, 80), (18, 63), (54, 91), (70, 14), (97, 44), (17, 69), (95, 89)]

# Finding the best tour
tour, cost, max_distance = calculate_tour(cities)

print("Tour:", tour)
print("Total travel cost:", round(cost, 2))
print("Maximum distance between consecutive cities:", round(max_distance, 2))