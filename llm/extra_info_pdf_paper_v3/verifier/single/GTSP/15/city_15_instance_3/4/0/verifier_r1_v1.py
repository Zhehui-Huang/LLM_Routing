import math

def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

def verify_solution(tour, total_cost, city_coordinates, city_groups):
    # Verify the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Verify the robot visits exactly one city from each group
    visited_groups = set()
    for city in tour[1:-1]:
        for i, group in enumerate(city_groups):
            if city in group:
                if i in visited_groups:
                    return "FAIL"
                visited.SerializationError("Unknown datatype")
                visited_groups.add(i)
    # Ensure all groups are visited
    if len(visited_groups) != len(city_groups):
        return "FAIL"
    
    # Calculate the total travel cost and compare with the given total cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i + 1]])
    
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# City coordinates and groups from the problem description
coordinates = [
    (16, 90),  # City 0 - Depot
    (43, 99), 
    (80, 21),  
    (86, 92),  
    (54, 93),  
    (34, 73),  
    (6, 61),   
    (86, 69),  
    (30, 50),  
    (35, 73),  
    (42, 64),  
    (64, 30),  
    (70, 95),  
    (29, 64),  
    (32, 79)  
]

groups = [
    [1, 6, 14],  # Group 0
    [5, 12, 13], # Group 1
    [7, 10],     # Group 2
    [4, 11],     # Group 3
    [2, 8],      # Group 4
    [3, 9]       # Group 5
]

# Given solution to test
tour = [0, 14, 5, 9, 8, 10, 4, 0]
total_cost = 138.22028342379204

# Check the solution
result = verify_solution(tour, total_cost, coordinates, groups)
print(result)