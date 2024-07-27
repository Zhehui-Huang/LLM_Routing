import itertools
import math

# Coordinates of the cities
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

def euclidean_distance(a, b):
    """Calculate Euclidean distance between points a and b."""
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def total_tour_cost(tour):
    """Calculate the total tour cost given a tour."""
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total_cost

def find_best_tour():
    min_cost = float('inf')
    best_tour = []

    # Generate combinations of 5 cities (excluding the depot city 0)
    for combination in itertools.combinations(range(1, 10), 5):
        # Create a full tour by adding the depot city at the start and end, explore all permutations
        full_tours = itertools.permutations(combination)
        
        for tour in full_tours:
            # Add depot city to the start and end of each permutation of the tour
            current_tour = [0] + list(tour) + [0]
            # Calculate total cost of the current tour
            cost = total_tour_cost(current_tour)
            
            # Update the minimum cost and best tour found so far
            if cost < min_cost:
                min_cost = cost
                best_tour = current_tour

    return best_tour, min_cost

# Execute the function to find the best tour and its cost
best_tour, min_cost = find_best_tour()

# Output the results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost}")