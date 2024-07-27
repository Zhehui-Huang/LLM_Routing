import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solution(tour, total_cost, max_distance):
    coordinates = [
        (54, 87),  # depot city 0
        (21, 84),  # city 1
        (69, 84),  # city 2
        (53, 40),  # city 3
        (54, 42),  # city 4
        (36, 30),  # city 5
        (52, 82),  # city 6
        (93, 44),  # city 7
        (21, 78),  # city 8
        (68, 14),  # city 9
        (51, 28),  # city 10
        (44, 79),  # city 11
        (56, 58),  # city 12
        (72, 43),  # city 13
        (6, 99)    # city 14
    ]
    
    # Check if the tour includes all cities and starts/ends at the depot
    if set(tour) != set(range(15)) or tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check for each city visited exactly once except depot city 0
    unique_cities = set(tour[1:-1])
    if len(unique_cities) != 14:
        return "FAIL"
    
    # Validate the total and maximum travel distances
    calculated_total_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        distance = euclidean_distance(*coordinates[city1], *coordinates[city2])
        calculated_total_cost += distance
        if distance > calculated_max_distance:
            calculated_max_distance = distance
    
    # Check calculated distances with provided values rounded to 2 decimals for euclidean precision issues
    if round(calculated_total_cost, 2) != round(total_cost, 2) or round(calculated_max_distance, 2) != round(max_distance, 2):
        return "FAIL"
    
    return "CORRECT"

# Provided solution details
tour = [0, 6, 11, 8, 1, 14, 12, 4, 3, 10, 5, 9, 13, 7, 2, 0]
total_cost = 322.50
max_distance = 64.66

# Verify the solution
result = verify_solution(tour, total_cost, max_distance)
print(result)