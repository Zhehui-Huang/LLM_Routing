import math

# Given data
city_positions = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]
city_demands = [
    0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7,
    14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10
]
robot_capacity = 40
num_robots = 8

# Tours and costs from the provided solution
robots_tours = [
    [0, 1, 2, 0],
    [0, 3, 4, 0],
    [0, 5, 6, 21, 0],
    [0, 7, 10, 11, 22, 0],
    [0, 8, 9, 0],
    [0, 12, 13, 14, 0],
    [0, 15, 16, 18, 0],
    [0, 17, 19, 0]
]
robots_tour_costs = [
    47.28555690793142, 75.67537984747364, 60.36874281957374, 177.083135984926,
    81.27545517717891, 135.16522263935212, 131.67359997697682, 111.76777519175889
]

# Function to calculate Euclidean distance
def calculate_distance(pos1, pos2):
    return math.sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2)

# Check each requirement
def check_tours_requirements():
    covered_cities = [0] * len(city_positions)
    total_demand_meet = [0] * len(city_positions)
    
    for index, tour in enumerate(robots_tours):
        # Requirement 1
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL: Requirement 1"
        
        # Calculate load and tour cost
        load = 0
        tour_cost = 0
        for i in range(1, len(tour)):
            load += city_demands[tour[i]]
            tour_cost += calculate_distance(city_positions[tour[i - 1]], city_positions[tour[i]])
        tour_cost += calculate_distance(city_positions[tour[-1]], city_positions[tour[0]])
        
        # Requirement 2
        if load > robot_capacity:
            return "FAIL: Requirement 2"
        
        # Check tour cost accuracy
        if abs(tour_cost - robots_tour_costs[index]) > 1e-9:
            return f"FAIL: Requirement 4 - Calculated Cost: {tour_cost}, Expected Cost: {robots_tour_costs[index]}"
        
        # Requirement 3
        for city in tour[1:-1]:  # Ignoring depot 0 at start and end
            total_demand_meet[city] += city_demands[city]
        
        # Mark cities as covered
        for city in tour:
            covered_cities[city] = 1
    
    # Requirement 5
    if sum(covered_cities) != len(city_positions) or not all(total_demand_meet[i] == city_demands[i] for i in range(1, len(city_demands))):
        return "FAIL: Requirement 5"
    
    # If all checks are passed
    return "CORRECT"

# Output the result of the verification
print(check_tours_requirements())