import math

# Define the cities and coordinates
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69)
}

# Function to calculate the Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Robot tours and their reported costs
robot_data = {
    0: ([0, 1, 9, 0], 72.88070710888512),
    1: ([0, 10, 2, 0], 52.4625939010481),
    2: ([0, 11, 3, 0], 86.03587467520119),
    3: ([0, 4, 12, 0], 64.98936367308863),
    4: ([0, 5, 13, 0], 68.36272673975597),
    5: ([0, 6, 14, 0], 64.17258428512785),
    6: ([0, 7, 15, 0], 83.62034367443502),
    7: ([0, 8, 0], 64.89992295835181)
}

# Validate the solution
def validate_solution(robot_data, cities):
    # Check that each city is visited exactly once
    visited_cities = set()
    for tour, _ in robot_data.values():
        for ci in tour[1:-1]:  # Ignore the depot city in start and end
            if ci in visited_cities:
                return ("FAIL", "A city is visited more than once.")
            visited_cities.add(ci)
        
    if len(visited_cities) != (len(cities) - 1):
        return ("FAIL", "Not all cities are visited.")

    # Verify distances match the provided costs
    total_cost_calculated = 0
    for tour, reported_cost in robot_data.values():
        calculated_cost = sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
        total_cost_calculated += calculated_cost
        if not math.isclose(calculated_cost, reported_cost, rel_tol=1e-5):
            return ("FAIL", "Mismatch in calculated and reported travel costs for a tour.")

    # If all tests pass
    return ("CORRECT", total_cost_calculated)

# Run validation and produce output
result, detail = validate_solution(robot_data, cities)
print(result)
if result == "FAIL":
    print(detail)