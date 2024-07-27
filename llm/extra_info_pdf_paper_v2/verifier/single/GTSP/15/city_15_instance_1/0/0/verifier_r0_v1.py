import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, total_travel_cost):
    cities = {
        0: (29, 51), 
        1: (49, 20), 
        2: (79, 69), 
        3: (17, 20), 
        4: (18, 61), 
        5: (40, 57), 
        6: (57, 30), 
        7: (36, 12), 
        8: (93, 43), 
        9: (17, 36), 
        10: (4, 60), 
        11: (78, 82), 
        12: (83, 96), 
        13: (60, 50), 
        14: (98, 1)
    }
    
    city_groups = [
        [1, 2, 5, 6],
        [8, 9, 10, 13],
        [3, 4, 7],
        [11, 12, 14]
    ]
    
    # Check if the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if the robot visits exactly one city from each group
    visited_groups = [0] * len(city_groups)
    for city in tour[1:-1]:  # exclude the initial and final depot city
        for group_index, group in enumerate(city_groups):
            if city in group:
                visited_groups[groupIndex] += 1
    
    if any(count != 1 for count in visited_groups):
        return "FAIL"

    # Calculate the total travel distance
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])

    # Check if the provided travel cost matches the calculated one
    if not math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-2):
        return "FAIL"

    return "CORRECT"

# Provided tour and total travel cost
tour = [0, 4, 11, 13, 5, 0]
total_travel_cost = 148.87

# Verification of the solution
result = verify_solution(tour, total_travel_cost)
print(result)