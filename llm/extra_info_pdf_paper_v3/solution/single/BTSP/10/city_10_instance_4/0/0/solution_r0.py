from itertools import permutations
import math

# Coordinates of the cities (depot city inclusive)
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

def calculate_distance(city1, city2):
    # Calculate Euclidean distance between two cities
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Function to calculate the total cost and max distance of a tour
def evaluate_tour(tour):
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = calculate_distance(tour[i], tour[i + 1])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    return total_cost, max_distance

def find_optimal_tour():
    city_indices = list(range(1, 10))  # All city indices except the depot
    best_tour = None
    best_max_distance = float('inf')
    best_total_cost = float('inf')
    
    # Generate all possible permutations (all tours)
    for perm in permutations(city_indices):
        tour = [0] + list(perm) + [0]
        total_cost, max_distance = evaluate_tour(tour)
        
        # Check if current max_distance is the smallest encountered
        if max_distance < best_max_distance:
            best_tour = tour
            best_max_distance = max_distance
            best_total_cost = total_cost
        elif max_distance == best_max_distance:
            # Check total distance as secondary criteria
            if total_cost < best_total_cost:
                best_tour = tour
                best_total_cost = total_cost

    # Return the best found tour, its total cost and maximum distance between consecutive cities
    return best_tour, best_total_cost, best_max_distance

# Execute the function to find the optimal tour
optimal_tour, optimal_cost, optimal_max_distance = find_optimal_tour()

# Output the results
print("Tour:", optimal_tour)
print("Total travel cost:", round(optimal_cost, 2))
print("Maximum distance between consecutive cities:", round(optimal_max_distance, 2))