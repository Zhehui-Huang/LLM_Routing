import numpy as np

def calculate_euclidean_distance(point1, point2):
    return np.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def verify_solution(tour, total_cost, city_positions, city_groups):
    # Verify the tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Verify each city group is visited exactly once
    visited_groups = []
    for city in tour[1:-1]:  # Skip the depot at the start and the end
        for index, group in enumerate(city_groups):
            if city in group:
                if index in visited_groups:
                    return "FAIL"
                visited_groups.append(index)
                break
    if len(visited_groups) != len(city_groups):
        return "FAIL"

    # Calculate the total travel cost from the tour
    computed_cost = 0
    for i in range(len(tour)-1):
        computed_cost += calculate_euclidean_distance(city_positions[tour[i]], city_positions[tour[i+1]])
    
    # Verify the total travel cost is as expected
    if not np.isclose(computed_cost, total_cost, atol=0.1):
        return "FAIL"
    
    return "CORRECT"

# City positions and groups
city_positions = {
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

city_groups = {
    0: [1, 4],
    1: [2, 6],
    2: [7],
    3: [5],
    4: [9],
    5: [8],
    6: [3]
}

# Tour and total cost from the candidate solution
tour = [0, 4, 6, 7, 5, 9, 8, 3, 0]
total_cost_of_tour = 371.19

# Verify the solution
result = verify_solution(tour, total_cost_of_tour, city_positions, city_groups)
print(result)