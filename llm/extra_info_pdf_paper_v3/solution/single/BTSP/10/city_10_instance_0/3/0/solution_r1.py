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
        max_distance = max(max_distance, dist)
    return total_cost, max_distance

def two_opt_optimization(tour, max_iterations=1000):
    """Optimize the tour using the 2-opt technique with max_iterations."""
    best_tor = list(tour)
    best_total_cost, best_max_distance = calculate_tour_cost(best_tor)
    
    for _ in range(max_iterations):
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                new_tor = best_tor[:i] + best_tor[i:j][::-1] + best_tor[j:]
                _, new_max_distance = calculate_tour_cost(new_tor)
                if new_max_distance < best_max_distance:
                    best_tor = new_tor
                    best_max_distance = new_max_distance
                    improved = True
        if not improved:
            break
    return best_tor

# Initial tour: visit cities by index order
initial_tor = list(range(len(coordinates))) + [0]  # Return to the depot

# Optimize the initial tour using 2-opt
optimized_tor = two_opt_optimization(initial_tor)

# Calculate the final tour cost and maximum distance
final_total_cost, final_max_distance = calculate_tour_cost(optimized_tor)

# Results
print("Tour:", optimized_tor)
print("Total travel cost:", round(final_total_cost, 2))
print("Maximum distance between consecutive cities:", round(final_max_distance, 2))