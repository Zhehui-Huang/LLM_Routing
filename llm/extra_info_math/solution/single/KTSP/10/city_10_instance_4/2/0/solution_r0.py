import math
from itertools import permutations

# Coordinates of the cities
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

# Function to calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Generate all combinations of 7 cities (excluding the depot) to visit along with the depot.
def generate_city_combinations():
    from itertools import combinations
    city_indices = list(cities.keys())[1:]  # Exclude the depot city for combinations
    return [tuple([0] + list(comb)) for comb in combinations(city_indices, 7)]

# Compute the total cost of visiting cities in a specified order
def tour_cost(city_order):
    total_cost = 0
    num_cities = len(city_order)
    for i in range(num_cities - 1):
        city1 = city_order[i]
        city2 = city_order[i + 1]
        total_cost += calculate_distance(cities[city1], cities[city2])
    return total_cost

# Find the shortest path that includes the depot and exactly 7 other cities
def find_shortest_path():
    best_tour = None
    best_cost = float('inf')
    
    for city_combination in generate_city_combinations():
        # Generate all permutations to find the shortest tour
        for perm in permutations(city_combination):
            # Ensure the tour starts and ends at the depot
            current_tour = list(perm) + [0]
            current_cost = tour_cost(current_tour)
            
            if current_cost < best_cost:
                best_tour = current_tour
                best_cost = current_cost
                
    return best_tour, best_cost

# Main execution to find and display the solution
best_tour, best_cost = find_shortest_path()
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_cost:.2f}")