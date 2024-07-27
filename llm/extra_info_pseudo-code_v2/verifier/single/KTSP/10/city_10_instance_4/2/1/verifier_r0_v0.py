import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def is_valid_tour(tour, total_cost, cities):
    # Requirement 1: Starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return False
    
    # Requirement 2: Exactly 8 different cities visited (9 including the start and end at the depot)
    if len(set(tour)) != 9:  # Includes the depot city twice
        return False
    
    # Requirement 4: Tour should have correct format and be a sequence of indices
    if not all(isinstance(city, int) and 0 <= city < len(cities) for city in tour):
        return False
    
    # Validate the computed total cost with the actual tour distance
    computed_cost = 0
    for i in range(len(tour) - 1):
        computed_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])

    # Checking if the computed cost is sufficiently close to the provided total cost
    # to account for floating point arithmetic issues
    if not math.isclose(computed_cost, total_cost, rel_tol=1e-5):
        return False
    
    return True

# Cities positions indexed from 0 to 9
cities_positions = [
    (79, 15),  # Depot city 0
    (79, 55),
    (4, 80),
    (65, 26),
    (92, 9),
    (83, 61),
    (22, 21),
    (97, 70),
    (20, 99),
    (66, 62)
]

# Given tour solution
tour = [0, 9, 1, 3, 6, 7, 4, 2, 0]  # Starting and ending at city 0
given_total_cost = 269.51

# Perform test
if is_valid_tour(tour, given_total_cost, cities_positions):
    print("CORRECT")
else:
    print("FAIL")