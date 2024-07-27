import math

def calculate_distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35)
]

# Tours and reported travel cost
tours = {
    0: ([0, 4, 10, 3, 8, 2, 7, 9, 5, 6, 0], 107.69),
    1: ([1, 11, 15, 12, 1, 16, 20, 14, 17, 13, 18, 19], 110.53)
}
total_reported_cost = 218.21

# Verify the solution
def test_solution(tours, coordinates, total_reported_cost):
    total_calculated_cost = 0
    visited_cities = set()

    for robot_id, (tour, reported_cost) in tours.items():
        # Requirement 1: Check depot start and end
        if tour[0] != robot_id or tour[-1] != robot_id:
            return "FAIL"

        # Calculate the travel cost
        calculated_cost = 0
        for i in range(len(tour) - 1):
            calculated_cost += calculate_distance(coordinates[tour[i]], coordinates[tour[i+1]])
        
        # Round to 2 decimal places for comparison
        calculated_cost = round(calculated_cost, 2)

        if abs(calculated_cost - reported_cost) > 0.01:
            return "FAIL"
        
        total_calculated_cost += calculated_cost
        
        # Requirement 2: Check city visitation but ignore depots as they are visited twice
        visited_cities.update(tour[1:-1])

    # Round and compare total cost
    if abs(round(total_calculated_cost, 2) - total_reported_cost) > 0.01:
        return "FAIL"
    
    # Requirement 2 continued: Check all cities are visited
    if len(visited_cities) != 20:  # 21 cities including 2 depots visited exactly twice
        return "FAIL"

    return "CORRECT"

# Execute the test
result = test_solution(tours, coordinates, total_reported_cost)
print(result)