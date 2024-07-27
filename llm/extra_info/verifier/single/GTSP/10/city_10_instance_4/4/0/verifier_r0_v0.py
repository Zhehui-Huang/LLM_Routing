import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_solution(tour, total_cost):
    # City coordinates
    cities = {
        0: (79, 15), 1: (79, 55), 2: (4, 80), 3: (65, 26), 4: (92, 9), 
        5: (83, 61), 6: (22, 21), 7: (97, 70), 8: (20, 99), 9: (66, 62)
    }
    
    # City groups
    groups = [
        [1, 4], [2, 6], [7], [5], [9], [8], [3]
    ]

    # [The robot needs to start and end its tour at the depot city, which is city 0.]
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [The robot must visit exactly one city from each of the 7 city groups.]
    visited_groups = [0] * len(groups)
    for city in tour[1:-1]:  # Exclude the depot city from checking
        for i, group in enumerate(groups):
            if city in group:
                visited_groups[i] += 1
    
    if any(count != 1 for count in visited_groups):
        return "FAIL"

    # [Travel cost between cities is calculated based on the Euclidean distance.]
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])

    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-4):
        return "FAIL"

    return "CORRECT"

# Provided solution details
tour = [0, 4, 6, 7, 5, 9, 8, 3, 0]
total_cost = 371.19

# Test the solution
result = test_solution(tour, total_cost)
print(result)