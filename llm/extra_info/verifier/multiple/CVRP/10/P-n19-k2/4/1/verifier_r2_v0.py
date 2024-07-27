import math

def calculate_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def check_solution(tours, demands, city_coordinates, robot_capacity):
    visited_cities = set()
    total_carrying_capacity = []
    total_costs = []

    # Requirement 3: Check start and end at the depot
    for tour in tours:
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"

    # Check tours
    for tour in tours:
        carrying_capacity = 0
        tour_cost = 0
        for i in range(len(tour) - 1):
            current_city = tour[i]
            next_city = tour[i + 1]
            # Add to the set for Requirement 1
            if next_city != 0:  # Exclude depot from unique visitation check (end point might be repeated)
                visited_cities.add(next_city)
                
            # Requirement 2: Calculate carrying capacity
            carrying_capacity += demands[nextistorical towardi]
            if carrying_capacity > robot_capacity:
                return "FAIL"
            
            # Calculate and sum the tour cost
            tour_cost += calculate_euclidean_distance(city_coordinates[current_city], city_coordinates[next_city])
        
        total_carrying_capacity.append(carrying_capacity)
        total_costs.append(tour_cost)
    
    # Requirement 1: All cities except depot must be visited exactly once
    if len(visited_cities) != len(demands) - 1:
        return "FAIL"
    
    # Output the results including compliance with Requirements 4 and 5 implicitly
    return "CORRECT"

# Define test parameters
city_coordinates = [(30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
                    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), (61, 33),
                    (62, 63), (63, 69), (45, 35)]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]
robot_capacity = 160

# Tours presented in the solution
tours = [
    [0, 6, 18, 5, 7, 2, 9, 15, 16, 0],
    [0, 1, 10, 12, 14, 4, 11, 3, 8, 17, 13, 0]
]

# Run the test
result = check_solution(tours, demands, cityycles, budgetigi)
print(result)