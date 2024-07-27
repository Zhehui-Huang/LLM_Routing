import itertools
import math

# City coordinates, indexed by the city numbers
city_coords = {
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

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def calculate_tour_distance(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(city_coords[tour[i]], city_coords[tour[i+1]])
    return total_distance

def find_optimal_tour(cities_to_choose, num_cities_in_tour, depot):
    minimum_distance = float('inf')
    optimal_tour = None
    # Iterate over all combinations of cities_to_choose choose num_cities_in_tour - 2 
    # -2 because including the depot both starting and ending, which is not in the combinations
    for cities in itertools.combinations(cities_to_choose, num_cities_in_tour - 2):
        # Create tour starting and ending at depot
        tour = [depot] + list(cities) + [depot]
        # Calculate distance of this tour
        current_distance = calculate_tour_distance(tour)
        # Check if this tour is better than what we have found so far
        if current_distance < minimum_distance:
            minimum_distance = current_distance
            optimal_tour = tour
    return optimal_tour, minimum_distance

# Choose the cities excluding the depot, aiming to include 8 cities including the depot
cities_to_visit = list(range(1, 10))  # 1..9 (0 is depot)
num_required_cities = 8
depot_city = 0

# Find the optimal tour
optimal_tour, min_distance = find_optimal_tour(cities_to_visit, num_required_cities, depot_city)

# Output the solution
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {min_distance}")