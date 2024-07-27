import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_cost, city_coordinates):
    # Requirement: The robot must start and end its journey at the depot city, which is city 0
    if not (tour[0] == 0 and tour[-1] == 0):
        return "FAIL"
    
    # Requirement: The robot has to visit exactly 6 cities, including the depot city
    if len(set(tour)) != 6:
        return "FAIL"
    
    # Requirement: Output should have the tour starting and ending at depot city 0 and include the total travel cost
    # Calculating the travel cost from the tour
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(
            city_coordinates[tour[i]], 
            city_coordinates[tour[i+1]]
        )
    
    # Requirement: Travel cost is calculated using the Euclidean distance formula and matches the provided total cost
    if not math.isclose(calculated_cost, total_cost):
        return "FAIL"
    
    # Requirement: Check if number of cities visited (including repetitions) equals the expected number including two visit for depot
    if len(tour) != 7: 
        return "FAIL"
        
    return "CORRECT"

# City coordinates including the depot as the first item (index 0)
city_coordinates = [
    (90, 3),   # Depot city 0
    (11, 17),  # City 1
    (7, 27),   # City 2
    (95, 81),  # City 3
    (41, 54),  # City 4
    (31, 35),  # City 5
    (23, 95),  # City 6
    (20, 56),  # City 7
    (49, 29),  # City 8
    (13, 17)   # City 9
]

# Provided solution to test
solution_tour = [0, 0, 0, 0, 0, 0, 0]
solution_total_cost = 0.0

# Checking if the provided solution satisfies all the requirements
output = verify_solution(solution_tour, solution_total_cost, city_coordinates)
print(output)