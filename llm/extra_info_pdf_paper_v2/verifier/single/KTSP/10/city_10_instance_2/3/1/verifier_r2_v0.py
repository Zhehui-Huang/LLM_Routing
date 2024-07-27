import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_tour_and_cost(tour, total_travel_cost, cities):
    # Verifying the starting and ending city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Verifying the count of cities including the depot
    if len(set(tour)) != 6:
        return "FAIL"
    
    # Calculating the correct travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = cities[tour[i]]
        x2, y2 = cities[tour[i + 1]]
        calculated_cost += calculate_euclidean_distance(x1, y1, x2, y2)
    
    # Verifying the travel cost is as expected
    if not math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-9):
        return "FAIL"
    
    # Correct tour length & requirement meets the count of exactly 6 cities
    return "CORRECT"

# Cities coordinates, mapped by their indices.
cities_coordinates = {
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

# The provided solution
tour_solution = [0, 8, 5, 2, 1, 9, 0]
total_travel_cost_solution = 183.85354044487238

# Checking the solution
result = verify_tour_and_cost(tour_solution, total_travel_cost_solution, cities_coordinates)
print(result)