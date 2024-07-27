import math

def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def verify_solution(tours, city_coordinates):
    # Each robot should start and end at its designated depot
    if not (tours[0][0] == 0 and tours[0][-1] == 0):
        return "FAIL"
    if not (tours[1][0] == 1 and tours[1][-1] == 1):
        return "FAIL"
    
    # Each city must be visited exactly once by the robots collectively
    visited = set()
    for tour in tours:
        for city in tour:
            if city in visited and city not in [0, 1]:  # depots can be revisited at the start/end
                return "FAIL"
            visited.add(city)
    if len(visited) != 19:  # total cities including depots
        return "FAIL"
    
    # The travel cost is calculated as the Euclidean distance and should have been minimized
    total_calculated_cost = 0
    for tour in tours:
        for i in range(len(tour) - 1):
            total_calculated_cost += calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i + 1]])
    
    # Given cost: Robot 0: 34.56118681213356, Robot 1: 14.142135623730951 -> Total: 28.284271247461902
    reported_cost = 28.284271247461902  # from the solver output which does not match the given costs
    if not math.isclose(total_calculated_cost, reported_cost, abs_tol=1e-9):
        return "FAIL"
    
    # Ensure no subtours within each robot's tour
    # This part can generally be ensured by the solver, but let's reconfirm as per requirement
    for tour in tours:
        if len(tour) != len(set(tour)):
            return "FAIL"
    
    return "CORRECT"

# Define city coordinates (IDs match index positions)
city_coordinates = [
    (30, 40),  # Depot city 0
    (37, 52),  # Depot city 1
    (49, 43),
    (52, 64),
    (31, 62),
    (52, 33),
    (42, 41),
    (52, 41),
    (57, 58),
    (62, 42),
    (42, 57),
    (27, 68),
    (43, 67),
    (58, 27),
    (37, 69),
    (61, 33),
    (62, 63),
    (63, 69),
    (45, 35)
]

# Tours extracted from the solver's output
robot_0_tour = [0, 6, 18, 0]
robot_1_tour = [1, 10, 1]

# Verification of the solution
result = verify_solution([robot_0_tour, robot_1_tour], city_coordinates)
print(result)  # Expected output based on the input data and the test being run