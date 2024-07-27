import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y1 - y2)**2)

def verify_solution(tour, total_travel_cost):
    # City coordinates by indices
    coordinates = {
        0: (50, 42),
        1: (41, 1),
        2: (18, 46),
        3: (40, 98),
        4: (51, 69),
        5: (47, 39),
        6: (62, 26),
        7: (79, 31),
        8: (61, 90),
        9: (42, 49)
    }
    
    # Verify starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Verify exactly 4 cities are visited including the depot
    if len(tour) != 5:
        return "FAIL"
    
    # Calculate the travel cost and compare with given total_travel_cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        calculated_cost += calculate_euclidean_distance(coordinates[city1][0], coordinates[city1][1], coordinates[city2][0], coordinates[city2][1])
    
    # Comparing calculated travel cost with provided total_travel_cost
    if not math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Provided solution details
tour = [0, 5, 6, 9, 0]
total_travel_cost = 65.20172104938949

# Check if the provided solution satisfies all the requirements
result = verify_solution(tour, total_travel_cost)
print(result)