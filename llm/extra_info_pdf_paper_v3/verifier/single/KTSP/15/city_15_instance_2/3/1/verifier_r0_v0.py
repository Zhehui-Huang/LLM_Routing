import math

def calculate_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_solution(tour, total_travel_cost):
    # city coordinates (city index corresponds to position in the list)
    city_coords = [
        (54, 87),  # City 0 (depot)
        (21, 84),  # City 1
        (69, 84),  # City 2
        (53, 40),  # City 3
        (54, 42),  # City 4
        (36, 30),  # City 5
        (52, 82),  # City 6
        (93, 44),  # City 7
        (21, 78),  # City 8
        (68, 14),  # City 9
        (51, 28),  # City 10
        (44, 79),  # City 11
        (56, 58),  # City 12
        (72, 43),  # City 13
        (6, 99)    # City 14
    ]
    
    # Check if the tour starts and ends at the depot city, city 0.
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if the tour includes exactly 8 cities.
    if len(set(tour)) != 9:  # includes the depot twice but should be considered once
        return "FAIL"
    
    # Check the calculated total distance.
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_euclidean_distance(city_coords[tour[i]], city_coords[tour[i + 1]])
    
    # Compare with provided total travel cost (allowing for small floating point precision issues)
    if abs(calculated_cost - total_travel_cost) > 0.01:
        return "FAIL"
    
    # If all checks are passed
    return "CORRECT"

# Solution given
solution_tour = [0, 6, 2, 3, 4, 5, 10, 12, 0]
solution_total_cost = 171.58

# Validate the solution
result = verify_solution(solution_tour, solution_total_cost)
print(result)