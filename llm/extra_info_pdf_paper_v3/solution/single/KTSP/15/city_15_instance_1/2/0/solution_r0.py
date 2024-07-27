import math
import itertools

# Coordinates of cities including the depot
cities = {
    0: (29, 51),
    1: (49, 20),
    2: (79, 69),
    3: (17, 20),
    4: (18, 61),
    5: (40, 57),
    6: (57, 30),
    7: (36, 12),
    8: (93, 43),
    9: (17, 36),
    10: (4, 60),
    11: (78, 82),
    12: (83, 96),
    13: (60, 50),
    14: (98, 1)
}

def euclidean_distance(city1, city2):
    """Calculate the Euclidean distance between two cities."""
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def total_tour_cost(tour):
    """Calculate the total travel cost of a tour."""
    return sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

def find_best_tour():
    best_tour = None
    best_cost = float('inf')
    
    # Start from depot and choose 5 more cities (6 including depot)
    for subset in itertools.combinations(range(1, 15), 5):
        current_subset = [0] + list(subset) + [0]  # Start and end at the depot city 0
        
        # Generate all permutations of the selected cities, maintaining depot as start and end
        for perm in itertools.permutations(current_subset[1:-1]):
            current_tour = [0] + list(perm) + [0]
            current_cost = total_tour_cost(current_tour)
            
            if current_cost < best_cost:
                best_cost = current_cost
                best_tour = current_tour
    
    return best_tour, best_cost

# Compute the best tour
best_tour, best_cost = find_best_tour()

# Output the best tour and the total travel cost
print("Tour:", best_tour)
print("Total travel cost:", best_cost)