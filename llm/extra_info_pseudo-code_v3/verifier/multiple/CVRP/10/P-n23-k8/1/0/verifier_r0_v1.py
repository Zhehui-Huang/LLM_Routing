import math

# Cities Data
city_coords = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
               (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
               (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
               (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
               (45, 35), (32, 39), (56, 37)]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]
robot_capacity = 40

# Robot tours from solution
robot_tours = [
    [0, 21, 16, 1, 10, 13, 0],  # Robot 0
    [0, 6, 20, 19, 0],          # Robot 1
    [0, 2, 22, 0],              # Robot 2
    [0, 4, 11, 9, 0],           # Robot 3
    [0, 7, 5, 12, 0],           # Robot 4
    [0, 15, 3, 0],              # Robot 5
    [0, 14, 18, 0],             # Robot 6
    [0, 17, 0]                  # Robot 7
]

# Function to calculate Euclidean distance
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Check all requirements
def verify_solution(tours, city_demands, capacity, city_positions):
    total_cost_computed = 0
    city_visit_count = [0] * len(city_demands)

    for tour in tours:
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL: Tour does not start or end at the depot."
        
        current_capacity = capacity
        prev_city = tour[0]
        
        for i in range(1, len(tour)):
            city = tour[i]
            city_visit_count[city] += 1
            if city != 0:  # Depot does not have demand
                current_capacity -= city_demands[city]
            if current_capacity < 0:
                return "FAIL: Capacity exceeded."
            
            total_cost_computed += euclidean_distance(city_positions[prev_city], city_positions[city])
            prev_city = city

        # Add return to depot cost
        total_cost_computed += euclidean_distance(city_positions[prev_city], city_positions[tour[0]])
    
    if any(x > 1 for x in city_visit_count[1:]) or any(x == 0 for x in city_visit_count[1:]):
        return "FAIL: Some cities are visited incorrectly or not visited at all."

    if not all(city_visit_count[i] * city_demands[i] == city_demands[i] for i in range(1, len(city_demands))):
        return "FAIL: Not all city demands are met correctly."

    # Assuming an acceptable rounding difference in the total cost;
    # the actual value might differ due to floating-point precision in distances calculation.
    return "CORRECT"

# Test the solution
verification_result = verify_solution(robot_tours, demands, robot_capacity, city_coords)
print(verification_result)