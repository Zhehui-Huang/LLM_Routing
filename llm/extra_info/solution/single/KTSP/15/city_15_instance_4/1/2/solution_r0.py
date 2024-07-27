import itertools
import math
from scipy.spatial import distance_matrix
import numpy as np

# City Coordinates
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90), 
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53,80), 13:(21, 21), 14:(12, 39)
}

def calculate_distance(p1, p2):
    """ Calculate Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create a distance matrix
n = len(cities)
distance_matrix = np.zeros((n, n))

for i in range(n):
    for j in range(n):
        if i != j:
            distance_matrix[i][j] = calculate_distance(cities[i], cities[j])

# Function to find the minimum tour visiting exactly 12 cities
def find_min_tour():
    min_cost = float('inf')
    best_tour = []
    all_cities = set(cities.keys())
    
    # Iterate through combinations of 11 cities to visit excluding the depot city
    for subset in itertools.combinations(all_cities - {0}, 11):
        tour_cities = [0] + list(subset) + [0]  # start and end at depot (0)
        
        # Generate all permutations of the inner 11 cities
        for tour in itertools.permutations(tour_cities[1:-1]):
            current_tour = [0] + list(tour) + [0]
            # Calculate cost of tour
            cost = sum(distance_matrix[current_tour[i]][current_tour[i + 1]] for i in range(len(current_tour) - 1))

            if cost < min_cost:
                min_cost = cost
                best_tour = current_tour
    
    return best_tour, min_cost

# Retrieve the optimal tour and its cost
optimal_tour, total_cost = find_min_tour()

# Output the result as specified
print("Tour:", optimal_tour)
print("Total travel cost:", total_cost)