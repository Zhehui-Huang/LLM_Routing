import math

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two cities. """
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_tour(tour, travel_cost):
    # Cities coordinates
    cities = [(79, 15), (79, 55), (4, 80), (65, 26), (92, 9), (83, 61), (22, 21), (97, 70), (20, 99), (66, 62)]
    
    # [Requirement 1] Start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] Visit exactly 8 cities, including the depot
    visited_cities = set(tour)
    if len(visited_cities) != 8 or 0 not in visited_cities:
        return "FAIL"
    
    # [Requirement 3] Check if the total travel cost is correctly calculated
    computed_cost = 0
    for i in range(len(tour) - 1):
        computed_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])

    if not math.isclose(computed_cost, travel_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Example solution being verified
tour_solution = [0, 3, 6, 9, 1, 5, 7, 4, 0]
total_travel_cost_solution = 235.37735391753955

# Verify the correctness of the solution
result = verify_tour(tour_solution, total_travel_cost_solution)
print(result)