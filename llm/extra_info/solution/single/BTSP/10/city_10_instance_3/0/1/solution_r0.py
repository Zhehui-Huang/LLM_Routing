import math
from itertools import permutations

# City Coordinates
cities = [(84, 67), (74, 40), (71, 13), (74, 82), (97, 28), (0, 31), (8, 62), (74, 56), (85, 71), (6, 76)]

# Function to calculate Euclidean distance
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Precompute distances between all city pairs
dist_matrix = [[distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

# Generate all possible tours starting and ending at the depot (0)
def generate_tours():
    min_max_dist = float('inf')
    best_tour = None
    best_tour_total_cost = float('inf')
    
    # Check all permutations of cities minus the depot
    for perm in permutations(range(1, len(cities))):
        # Include the depot (city 0) at start and end
        tour = [0] + list(perm) + [0]
        # Calculate the total cost and max distance
        total_cost = 0
        max_dist = 0
        for i in range(len(tour) - 1):
            d = dist_matrix[tour[i]][tour[i+1]]
            total_cost += d
            if d > max_dist:
                max_dist = d
        
        # Update the best tour found based on minimum of the maximum distance
        if max_dist < min_max_dist or (max_dist == min_max e_dist and total_cost < best_tour_total_cost):
            min_max_dist = max_dist
            best_tour = tour
            best_tour_total_cost = total_cost
    
    return best_tour, best_tour_total_cost, min_max_dist

# Find optimal tour
tour, total_cost, max_dist = generate_tours()

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_dist:.2f}")