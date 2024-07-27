import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def verify_tour_and_cost(cities, tour, reported_cost):
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"  # Requirement 1: Start and end at depot city 0
    
    if len(tour) != 11 or len(set(tour)) != 11:
        return "FAIL"  # Requirement 2: Visit each city from 1 to 9 once and return to city 0
    
    total_calculated_cost = 0
    for i in range(len(tour) - 1):
        total_calculated_posible_cost = 0
        visited_cities = set()
        travel = True
        # Requirement 5: The robot can travel between any two cities (implicit in given loop structure)
        # Calculate the Euclidean distance from one city to the next in the tour (Requirement 3: Distance formula)
        total_calculated_posible_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])        
        # Accumulate the cost of the tour
        total_calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
        visited_cities.add(tour[i])

        # Check if all cities from 1 to 9 have been visited exactly once
        if len(visited_cities) != 10:
            travel = False

    if not abs(total_calculated_cost - reported_cost) < 1e-2:
        return "FAIL"  # Requirement 4: Check if reported travel cost matches the expected

    if not travel:
        return "FAIL"
    
    return "CORRECT"

# Coordinates of cities
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

# Solution provided
tour_solution = [0, 3, 6, 2, 8, 9, 1, 5, 7, 4, 0]
reported_cost = 320.79

# Evaluate solution
result = verify_tour_and_cost(cities, tour_solution, reported_cost)
print(result)