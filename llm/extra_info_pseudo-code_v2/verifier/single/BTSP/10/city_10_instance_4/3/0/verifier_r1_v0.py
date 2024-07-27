import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y1 - y2) ** 2)

def validate_solution(tour, cities, total_travel_cost, longest_distance):
    # Check if tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if each city is visited exactly once (except depot city 0 which is visited twice)
    if sorted(tour) != [0] + list(range(1, len(cities))):
        return "FAIL"
    
    # Check computed total travel cost and longest distance
    calc_total_cost = 0
    calc_longest_distance = 0
    
    # Iterate through the tour to calculate the total distance and longest single travel
    for i in range(len(tour) - 1):
        distance = euclidean_distance(cities[tour[i]][0], cities[tour[i]][1], cities[tour[i+1]][0], cities[tour[i+1]][1])
        calc_total_cost += distance
        
        if distance > calc_longest_distance:
            calc_longest_distance = distance
    
    # Ensure floating point comparison tolerance
    if not math.isclose(calc_total_cost, total_travel_cost, rel_tol=1e-5):
        return "FAIL"
    
    if not math.isclose(calc_longest_distance, longest_distance, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Given cities data
cities = [
    (79, 15),  # City 0: Depot
    (79, 55),  # City 1
    (4, 80),   # City 2
    (65, 26),  # City 3
    (92, 9),   # City 4
    (83, 61),  # City 5
    (22, 21),  # City 6
    (97, 70),  # City 7
    (20, 99),  # City 8
    (66, 62)   # City 9
]

# Solution data
tour = [0, 1, 3, 4, 5, 7, 9, 8, 2, 6, 0]
total_travel_cost = 408.41
longest_distance = 61.68

# Test the solution
result = validate_solution(tour, cities, total_travel_part=total_travel_cost, longest_distance_part=longest_distance)
print(result)