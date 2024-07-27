import numpy as np

def calculate_distance(city1, city2):
    return np.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tour(cities_coords, tour, expected_max_distance):
    # Check Requirement 1: Tour starts and ends at depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check Requirement 2: Each city is visited exactly once, except depot
    if sorted(tour) != sorted([0] + list(range(1, len(cities_coords)))):
        return "FAIL"
    
    # Check Requirement 3: Verify the maximum distance does not exceed expected
    max_distance = 0
    for i in range(1, len(tour)):
        dist = calculate_distance(cities_coords[tour[i-1]], cities_coords[tour[i]])
        if dist > max_distance:
            max_distance = dist
            
    if max_distance > expected_max_distance:
        return "FAIL"
    
    return "CORRECT"

# Define city coordinates
cities_coords = [
    (53, 68),  # City 0 (Depot)
    (75, 11),  # City 1
    (91, 95),  # City 2
    (22, 80),  # City 3
    (18, 63),  # City 4
    (54, 91),  # City 5
    (70, 14),  # City 6
    (97, 44),  # City 7
    (17, 69),  # City 8
    (95, 89)   # City 9
]

# Solution given
solution_tour = [0, 3, 8, 4, 5, 2, 9, 7, 1, 6, 0]
expected_max_distance = 56.61271941887264

# Perform verification
result = verify_tour(cities_coords, solution_tour, expected_max_distance)
print(result)  # Should output "CORRECT" if the solution meets all requirements.