import math

def calculate_cost(city1, city2, coordinates):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 +
                     (coordinates[city1][1] - coordinates[city2][1]) ** 2)

def validate_solution(solution, city_coordinates, num_robots, cost_solution):
    if len(city_coordinates) != 19: # Including two depots
        return "FAIL"

    if num_robots != 2:
        return "FAIL"

    # Parse solution to build the actual tours
    tours = []
    current_tour = []
    visited_cities = set()

    for city in solution:
        # Check if negative (depot marker)
        if city < 0:
            if current_tour:
                tours.append(current_tour)
                current_tour = []
        else:
            if city in visited_cities:
                return "FAIL"  # City visited more than once
            visited_cities.add(city)
            current_tour.append(city)
    
    if current_tour:
        tours.append(current_tour)

    # Each city exactly once check, excluding depots
    if len(visited_cities) != 18:
        return "FAIL"

    if any(city not in visited_cities for city in range(2, 19)):
        return "FAIL"

    # Verify starting positions
    if tours[0][0] != 0 or solution[0] != 0:
        return "FAIL"
    
    # Calculate total travel cost
    total_cost = 0
    for tour in tours:
        # Ensure tours start and optionally end at a depot 
        if tour[0] != 0:  # Should start from depot 0
            return "FAIL"
        # Calculate tour cost
        tour_cost = 0
        for i in range(1, len(tour)):
            tour_cost += calculate_cost(tour[i - 1], tour[i], city_coordinates)
        # Add distance back to depot for the first robot if the tour does not end on a depot
        if tour[-1] != 1:
            tour_cost += calculate_cost(tour[-1], 0, city_coordinates)  # Back to depot 0
        total_cost += tour_cost
    
    # Checking to match the provided total cost solution
    if not math.isclose(total_cost, cost_solution, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Assumed input setup
num_cities = 19
city_coordinates = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 43),
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
    13: (58, 27),
    14: (37, 69),
    15: (61, 33),
    16: (62, 63),
    17: (63, 69),
    18: (45, 35)
}

solution_example = [0, 16, 10, 4, 2, -1, 13, 12, 11, 14, 15, 18, 5, 9, 7, 6, 8, 3, 17, 1]
cost_solution = 365.3580612012282

# Run the validation check
print(validate_solution(solution_example, city_coordinates, 2, cost_solution))