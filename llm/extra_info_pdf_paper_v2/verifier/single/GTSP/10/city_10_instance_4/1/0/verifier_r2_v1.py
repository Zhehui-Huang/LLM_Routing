import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def verify_solution(tour, total_cost):
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
    
    city_groups = {
        0: [1, 4],
        1: [2, 6],
        2: [7],
        3: [5],
        4: [9],
        5: [8],
        6: [3]
    }
    
    # Check starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Calculate and check the total cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    
    if abs(calculated_cost - total_cost) > 1e-5:
        return "FAIL"
    
    # Check if exactly one city from each group is visited
    visited_groups = set()
    for city in tour[1:-1]:  # Exclude the depot
        for group_id, group_cities in city_groups.items():
            if city in group_cities:
                if group_id in visited_groups:
                    return "FAIL"
                visited_groups.add(group_index)
    
    if len(visited_groups) != len(city_groups):
        return "FAIL"
    
    return "CORRECT"

# Provided solution
solution_tour = [0, 4, 6, 7, 5, 9, 8, 3, 0]
solution_total_cost = 371.1934423276749

# Check the solution
test_output = verify_solution(solution_tour, solution_total_cost)
print(test_output)