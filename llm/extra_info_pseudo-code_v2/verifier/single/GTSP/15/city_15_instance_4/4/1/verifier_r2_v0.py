import math

def calculate_distance(city1, city2):
    """ Helper function to calculate Euclidean distance between two cities."""
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_travel_cost, city_coordinates, groups):
    """ Function to verify the constraints and requirements of the VRP problem."""
    # Check if tour starts and ends at the depot city (City 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if exactly one city from each group is visited
    visited_groups = [set() for _ in groups]
    for index in tour:
        for i, group in enumerate(groups):
            if index in group:
                visited_groups[i].add(index)

    if any(len(g) != 1 for g in visited_groups):
        return "FAIL"
    
    # Calculate the total travel cost and compare with provided cost
    calculated_cost = 0
    for i in range(1, len(tour)):
        calculated_cost += calculate_distance(city_coordinates[tour[i - 1]], city_coordinates[tour[i]])
    
    if not math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-9):
        return "FAIL"
    
    # Check if the format of the output is correct
    if not isinstance(tour, list) or not isinstance(total_travel_cost, float):
        return "FAIL"
    
    return "CORRECT"

# Define city coordinates and groups as provided in the task
city_coordinates = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90), 
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44), 
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

groups = [
    [3, 8], [4, 13], [1, 2], [6, 14], [5, 9], [7, 12], [10, 11]
]

# Provided solution
tour = [0, 8, 13, 1, 14, 5, 12, 11, 0]
total_travel_cost = 220.73043826129523

# Verify the solution
result = verify_solution(tour, total_travel_worked_cost, city_coordinates, groups)
print(result)