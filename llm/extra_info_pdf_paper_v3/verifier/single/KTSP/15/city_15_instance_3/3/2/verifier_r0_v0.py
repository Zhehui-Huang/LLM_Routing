import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_tsp_solution(tour, cost):
    # Coordinates of each city (index corresponds to city ID)
    coordinates = [
        (16, 90),  # City 0 - Depot
        (43, 99),  # City 1
        (80, 21),  # City 2
        (86, 92),  # City 3
        (54, 93),  # City 4
        (34, 73),  # City 5
        (6, 61),   # City 6
        (86, 69),  # City 7
        (30, 50),  # City 8
        (35, 73),  # City 9
        (42, 64),  # City 10
        (64, 30),  # City 11
        (70, 95),  # City 12
        (29, 64),  # City 13
        (32, 79)   # City 14
    ]
    
    # Requirement checks
    # Check the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check the robot visits exactly 10 cities, including the depot
    if len(set(tour)) != 10:
        return "FAIL"
    
    # Calculating the travel cost based on Euclidean distance
    calculated_cost = 0
    for i in range(len(tour)-1):
        calculated_cost += calculate_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    
    # Compare the calculated cost with the given cost
    if round(calculated_cost, 2) != round(cost, 2):
        return "FAIL"
    
    return "CORRECT"
    
# Provided solution details
tour = [0, 0, 14, 5, 9, 13, 10, 4, 3, 12, 1, 0]
cost = 185.99

# Verify the solution
result = verify_tsp_solution(tour, cost)
print(result)