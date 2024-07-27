import math

# Constants provided by the task
CITY_COORDINATES = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), (61, 33), 
    (62, 63), (63, 69), (45, 35)
]
CITY_DEMANDS = [
    0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15
]
ROBOT_CAPACITY = 160
NUMBER_OF_CITIES = len(CITY_COORDINATES)
NUMBER_OF_ROBOTS = 2

# Calculate Euclidean distance
def calculate_distance(city1, city2):
    return math.sqrt((CITY_COORDINATES[city1][0] - CITY_COORDINATES[city2][0])**2 + (CITY_COORDINATES[city1][1] - CITY_COORDINATES[city2][1])**2)

# Calculate total travel cost for a tour
def calculate_travel_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(tour[i], tour[i + 1])
    return total_cost

# Solutions provided
robot_tours = [
    [0, 1, 4, 11, 12, 3, 8, 16, 17, 14, 10, 0],  # Robot 0 Tour
    [0, 6, 2, 7, 5, 9, 13, 15, 18, 0]  # Robot 1 Tour
]
calculated_costs = [139.06, 98.55]  # Costs provided
overall_cost_provided = 237.61

# Function to validate solution
def validate_solution():
    overall_cost_calculated = 0
    for robot_index, tour in enumerate(robot_tours):
        # Check tour starts and ends at the depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        
        # Check capacity constraint
        total_demand = 0
        for city in tour[1:-1]:  # excluding depot visits
            total_demand += CITY_DEMANDS[city]
        if total_demand > ROBOT_CAPACITY:
            return "FAIL"
        
        # Calculate and compare tour cost
        tour_cost = calculate_travel_cost(tour)
        if not math.isclose(tour_cost, calculated_costs[robot_index], abs_tol=1e-2):
            return "FAIL"
        
        overall_cost_calculated += tour_cost
        
    # Check overall travel cost
    if not math.isclose(overall_cost_calculated, overall_cost_provided, abs_tol=1e-2):
        return "FAIL"
    
    # Check all cities are visited exactly once (excluding depot)
    visited_cities = set()
    for tour in robot_tours:
        for city in tour[1:-1]:  # excluding depot visits
            if city in visited_cities:
                return "FAIL"
            visited_cities.add(city)
    if len(visited_cities) != NUMBER_OF_CITIES - 1:
        return "FAIL"
    
    return "CORRECT"

# Output result of validation
print(validate_solution())