import math

# Coordinates for each city including the depot city at index 0
coordinates = [
    (50, 42),  # Depot city 0
    (41, 1),   # City 1
    (18, 46),  # City 2
    (40, 98),  # City 3
    (51, 69),  # City 4
    (47, 39),  # City 5
    (62, 26),  # City 6
    (79, 31),  # City 7
    (61, 90),  # City 8
    (42, 49)   # City 9
]

def euclidean_distance(c1, c2):
    """Compute the Euclidean distance between two city coordinates."""
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def calculate_tour_cost(tour):
    """Calculate the total travel cost and the maximum distance between consecutive cities of a tour."""
    total_cost = 0
    max_distance = 0
    num_cities = len(tour)
    for i in range(1, num_cities):
        dist = euclidean_distance(coordinates[tour[i - 1]], coordinates[tour[i]])
        total_cost += dist
        max_distance = max(max_type_distance, dist)
    return total_cost, max_distance

def two_opt_optimization(tour, max_iterations=1000):
    """Optimize the tour using the 2-opt technique with max_iterations."""
    best_tour = list(tour)
    _, best_max_distance = calculate_tour_cost(best_tour)
    
    for _ in range(max_iterations):
        for i in range(1, len(best_tour) - 2):
            for j in range(i + 1, len(best_tour)):
                new_tour = best_tour[:i] + best_tour[i:j][::-1] + best_tour[j:]
                _, new_max_distance = calculate_tour_cost(new_tour)
                if new_max_distance < best_max_distance:
                    best_tour = new_tour
                    best_max_distance = new_max_distance
    return best_tour

# Initial tour: visit cities by index order
initial_tour = list(range(len(coordinates))) + [0]  # Return to the depot

# Optimize the initial tour using 2-opt
optimized_tour = two_opt_optimization(initial_tour)

# Calculate the final tour cost and maximum distance
final_total_cost, final_max_distance = calculate_tour_cost(optimized_tour)

# Results
print("Tour:", optimized_tour)
print("Total travel cost:", final_total_cost)
print("Maximum distance between consecutive cities:", final_max_distance)