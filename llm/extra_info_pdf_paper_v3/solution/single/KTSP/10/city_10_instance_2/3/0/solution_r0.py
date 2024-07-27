import math
import itertools

# Given cities with coordinates
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

# Function to calculate Euclidean distance between two cities
def calc_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Function to evaluate total travel cost of a given tour
def tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += calc_distance(tour[i], tour[i+1])
    return cost

# Generate subset combinations of the cities to visit (excluding the depot)
def viable_subsets(depot, number_of_cities_to_visit):
    non_depot_cities = list(cities.keys())
    non_depot_cities.remove(depot)
    return list(itertools.combinations(non_depot_cities, number_of_cities_to_visit-1))

# Evaluate each subset by forming tours and calculating their costs
def find_best_tour(depot, number_of_cities_to_visit):
    best_tour = None
    best_cost = float('inf')
    
    for subset in viable_subsets(depot, number_of_cities_to_visit):
        # Create all permutations of the cities subset tour starting and ending at the depot
        for permutation in itertools.permutations(subset):
            current_tour = [depot] + list(permutation) + [depot]
            current_cost = tour_cost(current_tour)
            if current_cost < best_cost:
                best_tour = current_tour
                best_cost = current_cost
    
    return best_tour, best_cost

# Finding the best tour visiting exactly 6 cities including the depot
best_tour, best_cost = find_best_tour(0, 6)

# Output the tour and its total cost
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_cost}")