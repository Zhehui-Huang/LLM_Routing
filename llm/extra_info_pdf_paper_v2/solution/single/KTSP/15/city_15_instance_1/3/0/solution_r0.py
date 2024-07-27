import math
import itertools

# Define cities with their coordinates
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

# Function to calculate Euclidean distance between two cities
def calc_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Implementing variable neighborhood search for k-TSP
def find_optimal_tour():
    min_tour = None
    min_cost = float('inf')
    
    # Generate all combinations of 5 cities (excluding the depot city 0 which is fixed)
    for combination in itertools.combinations(range(1, 15), 5):
        # Always start and end at the depot city 0
        full_tour = [0] + list(combination) + [0]

        # Generate all permutations of the 5 cities, keeping depot as the start and end
        for perm in itertools.permutations(combination):
            current_tour = [0] + list(perm) + [0]
            # Calculate the cost of the current tour
            current_cost = sum(calc_distance(current_tour[i], current_tour[i+1]) for i in range(len(current_tour) - 1))
            
            # Update the minimal tour if a new lower cost tour is found
            if current_cost < min_cost:
                min_tour = current_tour
                min_dr_cost = current_cost
                min_cost = current_cost

    return min_tour, min_cost

# Run the function and print the optimal tour and cost
optimal_tour, total_cost = find_optimal_tour()
print("Tour:", optimal_tour)
print("Total travel cost:", total_cost)