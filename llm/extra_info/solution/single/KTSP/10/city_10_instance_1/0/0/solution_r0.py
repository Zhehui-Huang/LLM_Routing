import itertools
import math

# Coordinates of the cities
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

def find_shortest_tour():
    shortest_distance = float('inf')
    best_tour = []
    
    # Create all combinations of 4 cities except the depot (0), then add the depot to each combination
    city_combinations = itertools.combinations(cities.keys() - {0}, 4)
    
    for comb in city_combinations:
        current_cities = [0] + list(comb) + [0]
        # Generate all permutations of the selected 5 cities keeping 0 fixed at the start
        for perm in itertools.permutations(current_cities[1:-1]):
            tour = [0] + list(perm) + [0]
            # Calculate the total distance for this tour
            distance = 0
            for i in range(len(tour) - 1):
                distance += calculate_distance(tour[i], tour[i + 1])
            
            # Check if this tour is better than what we have found so far
            if distance < shortest_distance:
                shortest_distance = distance
                best_tour = tour
    
    return best_tour, shortest_distance

# Find the optimal tour and its cost
optimal_tour, optimal_cost = find_shortest_tour()

# Outputting the results in the required format
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {optimal_cost}")