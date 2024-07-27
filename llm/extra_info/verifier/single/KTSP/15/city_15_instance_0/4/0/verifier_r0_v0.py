import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, total_cost):
    coordinates = {
        0: (9, 93), 1: (8, 51), 10: (19, 65), 8: (19, 76)
    }
    
    if len(tour) != 5:
        return "FAIL"  # Tour does not have exactly 5 entries (4 cities + 1 return to depot)

    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"  # Start or end city is not the depot
    
    if len(set(tour[1:-1])) != 3:
        return "FAIL"  # Not exactly three other cities visited
    
    if set(tour) - set(coordinates.keys()):
        return "FAIL"  # Tour includes cities not in the list
    
    calculated_cost = 0
    for i in range(1, len(tour)):
        calculated_cost += calculate_distance(coordinates[tour[i-1]], coordinates[tour[i]])
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-5):
        return "FAIL"  # Provided total cost does not match calculated cost

    return "CORRECT"

# Provided solution
tour = [0, 1, 10, 8, 0]
total_cost = 90.54

# Verifying the solution
result = verify_solution(tour, total_cost)
print(result)