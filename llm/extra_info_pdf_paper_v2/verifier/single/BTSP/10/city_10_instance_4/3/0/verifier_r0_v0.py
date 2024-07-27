import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def verify_solution(tour, total_cost, max_distance):
    # City coordinates
    cities = {
        0: (79, 15), 
        1: (79, 55), 
        2: (4, 80), 
        3: (65, 26), 
        4: (92, 9), 
        5: (83, 61), 
        6: (22, 21), 
        7: (97, 70), 
        8: (20, 99), 
        9: (66, 62)
    }

    # Check if the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if the robot visits each city exactly once (excluding the depot city 0)
    visited_cities = sorted(tour[1:-1])
    unique_cities = sorted(set(visited_cities))
    if visited_citites != unique_cities or len(tour[1:-1]) != len(unique_cities):
        return "FAIL"

    # Calculate the total travel cost and max distance
    calculated_total_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        distance = calculate_distance(cities[tour[i]], cities[tour[i+1]])
        calculated_total_cost += distance
        if distance > calculated_max_distance:
            calculated_max_distance = distance

    # Verify the calculations
    if not math.isclose(calculated_total_cost, total_cost, rel_tol=1e-5) or not math.isclose(calculated_max_distance, max_distance, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Test the solution
tour = [0, 4, 3, 6, 0]
total_cost = 146.8285744978191
max_distance = 57.3149195236284

result = verify_solution(tour, total_cost, max_distance)
print(result)