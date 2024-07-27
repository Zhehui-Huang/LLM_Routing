import math

# Function to calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Function to check the tour and total cost against provided requirements
def verify_solution(tour, total_cost):
    # Coordinates of the cities
    coordinates = [(79, 15), (79, 55), (4, 80), (65, 26), (92, 9),
                   (83, 61), (22, 21), (97, 70), (20, 99), (66, 62)]

    # [Requirement 1] Check start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 2] Check if all cities are visited exactly once, except depot
    if sorted(tour[1:-1]) != list(range(1, 10)):
        return "FAIL"

    # [Requirement 3 & 5] Calculate total cost and compare
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    
    if round(calculated_cost, 2) != round(total_cost, 2):
        return "FAIL"

    # [Requirement 4] Check if tour sequence is valid (redundant with 2, kept for protocol)
    if len(tour) != 11:  # Includes the return to depot city, which must total 10 + 1
        return "FAIL"

    return "CORRECT"

# Provided solution
tour = [0, 4, 6, 2, 8, 9, 7, 5, 1, 3, 0]
total_cost = 336.77

# Verify the solution
print(verify_solution(tour, total

_cost))