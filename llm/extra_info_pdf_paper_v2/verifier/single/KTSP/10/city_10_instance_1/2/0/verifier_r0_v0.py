import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solution(tour, reported_cost, coordinates):
    # Check if the robot starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if exactly 5 cities are visited including the depot
    if len(set(tour)) != 5:
        return "FAIL"
    
    # Calculate the travel cost using Euclidean distance
    total_calculated_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = coordinates[tour[i]]
        x2, y2 = coordinates[tour[i+1]]
        total_calculated_cost += calculate_distance(x1, y1, x2, y2)

    # Check if the calculated distance matches the reported distance
    if not math.isclose(total_calculated_cost, reported_cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Context setup
cities_coordinates = {
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

tour_solution = [0, 4, 8, 3, 5, 0]
reported_travel_cost = 110.38

# Run verification
result = verify_solution(tour_solution, reported_travel_cost, cities_coordinates)
print(result)