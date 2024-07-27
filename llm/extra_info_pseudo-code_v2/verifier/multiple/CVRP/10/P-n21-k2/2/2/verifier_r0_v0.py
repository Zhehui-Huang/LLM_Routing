import math

# City coordinates and demands
cities = [
    (30, 40, 0),   # City 0: Depot
    (37, 52, 7),   # City 1
    (49, 49, 30),  # City 2
    (52, 64, 16),  # City 3
    (31, 62, 23),  # City 4
    (52, 33, 11),  # City 5
    (42, 41, 19),  # City 6
    (52, 41, 15),  # City 7
    (57, 58, 28),  # City 8
    (62, 42, 8),   # City 9
    (42, 57, 8),   # City 10
    (27, 68, 7),   # City 11
    (43, 67, 14),  # City 12
    (58, 48, 6),   # City 13
    (58, 27, 19),  # City 14
    (37, 69, 11),  # City 15
    (38, 46, 12),  # City 16
    (61, 33, 26),  # City 17
    (62, 63, 17),  # City 18
    (63, 69, 6),   # City 19
    (45, 35, 15)   # City 20
]

# Provided solution details
robot_tours = [
    [0, 18, 19, 0, 3, 8, 0, 14, 17, 0, 9, 13, 0, 12, 15, 0],
    [0, 4, 11, 0, 5, 7, 0, 2, 10, 0, 6, 20, 0, 1, 16, 0]
]
robot_costs = [366.11795273858655, 227.50256931683597]

# Constants
robot_capacity = 160

def calculate_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Function to check the solution requirements
def verify_solution(tours, costs, capacity):
    overall_cost = 0
    visited = set()
    
    for i, tour in enumerate(tours):
        starting_city = 0
        demand_covered = 0
        tour_cost = 0
        
        for j in range(1, len(tour)):
            current_city = tour[j]
            
            # Check if every city is visited from depot and returns to depot
            if current_city != 0 and tour[j-1] == 0:
                demand_covered = 0  # Reset capacity for each trip from depot
            demand_covered += cities[current_city][2]
            
            # Check if any trip exceeds the robot's capacity
            if demand_covered > capacity:
                return "FAIL"
            
            # Calculate travel cost
            last_city = tour[j-1]
            trip_cost = calculate_euclidean_distance(cities[last_city], cities[current_city])
            tour_cost += trip_cost

            # Check if every tour starts and ends at depot
            if j == len(tour) - 1 and current_city != 0:
                return "FAIL"

            # Ensure no city is visited more than once
            if current_city != 0 and current_city in visited:
                return "FAIL"
            visited.add(current_city)
        
        # Validate calculated costs closely match provided costs
        if not math.isclose(tour_cost, costs[i], abs_tol=1e-6):
            return "FAIL"
        
        overall_cost += tour_cost
    
    # check if every city has been visited exactly once excluding the depot
    if len(visited) != len(cities):
        return "FAIL"

    # check overall cost
    if not math.isclose(overall_cost, sum(costs), abs_tol=1e-6):
        return "FAIL"

    return "CORRECT"

# Call the function and print the result
result = verify_solution(robot_tours, robot_costs, robot_capacity)
print(result)