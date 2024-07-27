import math

# Coordinates of cities (index corresponds to city number)
coordinates = [
    (30, 40),  # Depot
    (37, 52),
    (49, 49),
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
    (58, 48),
    (58, 27),
    (37, 69)
]

# Demands for each city
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]

# Robot tours and solution provided
robot_tours = [
    [0, 3, 1, 0],
    [0, 2, 0],
    [0, 4, 5, 0],
    [0, 6, 0],
    [0, 7, 10, 9, 0],
    [0, 8, 11, 0],
    [0, 12, 15, 13, 0],
    [0, 14, 0]
]

# Checking the correctness of the solution
def calculate_distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 +
                     (coordinates[city1][1] - coordinates[city2][1]) ** 2)

def check_requirements(robot_tours, demands, max_capacity=35):
    demand_fulfilled = [0] * len(demands)
    
    total_cost = 0
    for tour in robot_tours:
        current_load = 0
        current_cost = 0
        for i in range(len(tour)-1):
            city = tour[i]
            next_city = tour[i+1]
            
            # Travel cost calculation
            current_cost += calculate_distance(city, next_city)
        
            # Update fulfilled demands
            if i != 0:  # Ignoring the depot for demand fulfillment
                current_load += demands[city]
                demand_fulfilled[city] += demands[city]
        
        if current_load > max_capacity:
            return "FAIL"  # Capacity constraint violated

        total_cost += current_cost
    
    # Check if all demands are met
    for i in range(1, len(demands)):
        if demand_fulfilled[i] != demands[i]:
            return "FAIL"
    
    # Minimized cost concern -- Here we just acknowledge it but can't verify optimality without computation
    if total_cost == 0:
        return "FAIL"  # It's not possible for total cost to be zero if distances are correct

    return "CORRECT"

# Run the unit tests
result = check_requirements(robot_tours, demands)
print(result)  # Output: "CORRECT" or "FAIL" based on test results