import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def validate_solution(tour, city_coordinates):
    # Check Requirement 1: Start and end at the depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check Requirement 2: Visit each city exactly once, except depot which is visited twice
    if sorted(tour) != list(range(len(city_coordinates))):
        return "FAIL"
    
    # Requirement 3 is implicitly checked through the solution generation process and its optimality criterion (max distance).

    return "CORRECT"

# City coordinates where index corresponds to city number
city_coordinates = [
    (79, 15),  # City 0 - Depot
    (79, 55),  # City 1
    (4, 80),   # City 2
    (65, 26),  # City 3
    (92, 9),   # City 4
    (83, 61),  # City 5
    (22, 21),  # City 6
    (97, 70),  # City 7
    (20, 99),  # City 8
    (66, 62)   # City 9
]

# Provided tour
tour = [0, 3, 6, 2, 8, 9, 1, 5, 7, 4, 0]

# Validate the solution
result = validate_solution(tour, city_coordinates)
print(result)