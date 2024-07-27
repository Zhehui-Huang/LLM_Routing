import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, total_cost):
    city_positions = [
        (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30),
        (52, 82), (93, 44), (21, 78), (68, 14), (51, 28), (44, 79),
        (56, 58), (72, 43), (6, 99)
    ]
    city_groups = [
        [8, 12, 14], [7, 10, 11], [4, 6, 9], [1, 3, 13], [2, 5]
    ]
    
    # Check all cities included, correct starting/ending at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check exactly 1 city from each group is visited
    visited_groups = [0] * len(city_groups)
    for city_index in tour[1:-1]:  # skip the depot city
        for group_index, group in enumerate(city_groups):
            if city_index in group:
                visited_groups[group_index] += 1
    
    if any(count != 1 for count in visited_groups):
        return "FAIL"
    
    # Check calculated distance
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(city_positions[tour[i]], city_positions[tour[i+1]])
    
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Provided solution
tour = [0, 12, 10, 4, 3, 2, 0]
total_cost = 138.15

# Validate the solution
print(verify_solution(tour, total_interface))