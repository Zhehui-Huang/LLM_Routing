import math

def calculate_distance(city_a, city_b):
    return math.sqrt((city_b[0] - city_a[0])**2 + (city_b[1] - city_a[1])**2)

def verify_tour(tour, total_cost):
    # Define city coordinates
    city_coordinates = [
        (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30), 
        (52, 82), (93, 44), (21, 78), (68, 14), (51, 28), (44, 79), 
        (56, 58), (72, 43), (6, 99)
    ]
    
    # Check Requirement 1: Start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check Requirement 2: Visit all cities exactly once, except depot city 0
    visited_cities = set(tour)
    if len(visited_cities) != len(city_coordinates) or len(tour) != len(city_coordinates) + 1:
        return "FAIL"
    
    # Check Requirement 3: Correct calculation of the total travel cost
    computed_cost = 0
    for i in range(len(tour) - 1):
        computed_cost += calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i + 1]])
    
    if not math.isclose(computed_cost, total_cost, rel_tol=1e-9):
        return "FAIL"

    # Requirement 4 & 5 are output format related which is correct by existing check logic.
    
    return "CORRECT"

# Provided solution
tour = [0, 6, 11, 14, 1, 8, 12, 4, 3, 5, 10, 9, 13, 7, 2, 0]
total_cost = 311.877641807867

# Verify the tour and costs
print(verify_tour(tour, total_cost))