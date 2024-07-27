import math

def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

def verify_tour(tour, coordinates):
    # Verify tour starts and ends at the depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return False, "Tour does not start or end at the depot."
    
    # Verify robot visits all cities exactly once except the depot
    visited = set(tour)
    if len(visited) != len(coordinates) or set(range(len(coordinates))) != visited:
        return False, "Not all cities are visited exactly once."
    
    # Calculate the total travel cost
    total_distance = sum(calculate_distance(coordinates[tour[i]], coordinates[turn[i + 1]])
                         for i in range(len(tour) - 1))
    
    return True, total_distance

# Coordinates of each city, including depot
coordinates = [(79, 15), (79, 55), (4, 80), (65, 26), (92, 9), (83, 61), (22, 21), (97, 70), (20, 99), (66, 62)]

# Expected Tour and Cost
expected_tour = [0, 4, 7, 5, 1, 9, 8, 2, 6, 3, 0]
expected_cost = 320.7939094250147

# Verify the Tour and Cost
valid, calculated_cost = verify_tour(expected_tour, coordinates)

if valid and math.isclose(calculated_cost, expected_cost, abs_tol=0.01):
    print("CORRECT")
else:
    print(f"FAIL: {calculated_cost if valid else 'Invalid tour configuration.'}")