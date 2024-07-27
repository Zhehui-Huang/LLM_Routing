import itertools
import math

# City Coordinates
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90), 
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53,80), 13:(21, 21), 14:(12, 39)
}

def calculate_distance(p1, p2):
    """ Calculate Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Function to find the minimum tour visiting exactly 12 cities starting and ending at depot city 0
def find_min_tour():
    min_cost = float('inf')
    best_tour = []
    all_cities = list(cities.keys())

    # Iterate through combinations of 11 cities to visit, including the depot city
    for subset in itertools.combinations([i for i in all_cities if i != 0], 11):
        full_subset = [0] + list(subset)  # include depot city at the start
        
        # For each subset, check all permutations
        for perm in itertools.permutations(full_subset[1:]):
            tour = [0] + list(perm) + [0]  # start and end at depot (0)
            # Calculate cost of this tour
            cost = sum(calculate_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

            if cost < min_cost:
                min_cost = cost
                best_tour = tour
    
    return best_tour, min_cost

# Retrieve the optimal tour and its cost
optimal_tour, total_cost = find_min_tour()

# Output the result as specified
print("Tour:", optimal_tour)
print("Total travel cost:", total_cost)