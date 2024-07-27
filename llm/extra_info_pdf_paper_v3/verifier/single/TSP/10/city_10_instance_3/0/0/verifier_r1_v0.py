import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_total_cost(tour, coordinates):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    return total_cost

def verify_tsp_solution(tour, total_cost, coordinates):
    # Check if all cities are visited exactly once, start and end at depot 0
    if set(tour) != set(range(len(coordinates))):
        return "FAIL"
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check the correctness of the calculated total distance
    calculated_cost = calculate_total_cost(tour, coordinates)
    if abs(calculated_cost - total_cost) > 1e-5:
        return "FAIL"
    
    # Check if no other city other than depot is revisited
    if len(tour) != len(set(tour)):
        return "FAIL"
    
    return "CORRECT"

# City coordinates (with depot as city 0)
coordinates = [
    (84, 67),  # depot city 0
    (74, 40),  # city 1
    (71, 13),  # city 2
    (74, 82),  # city 3
    (97, 28),  # city 4
    (0, 31),   # city 5
    (8, 62),   # city 6
    (74, 56),  # city 7
    (85, 71),  # city 8
    (6, 76)    # city 9
]

# Assuming a hypothetical correct tour and its total cost from a solution (this needs to be replaced with actual outputs)
given_tour = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
given_total_cost = calculate_total_cost(given_tour, coordinates)

# Check if the solution is correct
result = verify_tsp_solution(given_tour, given_total_cost, coordinates)
print(result)