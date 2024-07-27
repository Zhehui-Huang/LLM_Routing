import itertools
import math

def calculate_distance(city1, city2):
    """Calculate Euclidean distance between two cities."""
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def total_path_distance(cities, path):
    """Calculate the total travel distance for the given path."""
    return sum(calculate_distance(cities[path[i]], cities[path[i+1]]) for i in range(len(path)-1))

def find_k_tsp(cities, k):
    # Initialize variables
    min_cost = float('inf')
    best_tour = None
    
    # Create all combinations of k-1 cities (excluding the depot city)
    for subset in itertools.combinations(range(1, len(cities)), k - 1):
        # Create tours starting and ending at the depot city, and visiting the subset cities
        tours = [0] + list(subset) + [0]
        
        # Generate all permutations of the current subset tour
        for permuted_tour in itertools.permutations(tours[1:-1]):
            # Form the complete tour starting and ending at the depot
            full_tour = [0] + list(permuted_tour) + [0]
            
            # Calculate the cost of the current tour
            current_cost = total_path_distance(cities, full_tour)
            
            # Update the best tour and cost if current is better
            if current_cost < min_cost:
                min_cost = current_cost
                best_tour = full_tour

    return best_tour, min_cost

# Define city coordinates
cities = [
    (90, 3),   # Depot city 0
    (11, 17),  # City 1
    (7, 27),   # City 2
    (95, 81),  # City 3
    (41, 54),  # City 4
    (31, 35),  # City 5
    (23, 95),  # City 6
    (20, 56),  # City 7
    (49, 29),  # City 8
    (13, 17)   # City 9
]

# Number of cities to visit (including the depot)
k = 6

# Compute the solution
tour, cost = find_k_tsp(cities, k)

# Display the results
print("Tour:", tour)
print("Total travel cost:", cost)