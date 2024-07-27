import math

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def verify_solution(tour, total_cost):
    cities = {
        0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20),
        4: (18, 61), 5: (40, 57), 6: (57, 30), 7: (36, 12),
        8: (93, 43), 9: (17, 36), 10: (4, 60), 11: (78, 82),
        12: (83, 96), 13: (60, 50), 14: (98, 1)
    }
    city_groups = {
        0: [1, 2, 5, 6],
        1: [8, 9, 10, 13],
        2: [3, 4, 7],
        3: [11, 12, 14]
    }

    # [Requirement 1] Check if the tour starts and ends at the depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] Check if the tour visits exactly one city from each group
    visited_groups = [0] * 4
    for city in tour[1:-1]:  # not including the depot city at start/end
        for group in range(4):
            if city in city_groups[group]:
                visited_groups[group] += 1
                if visited_groups[group] > 1:
                    return "FAIL"
    if not all(visited == 1 for visited in visited_groups):
        return "FAIL"
    
    # [Requirement 3] Calculate the total distance and compare with given total_cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-5):
        return "FAIL"
    
    # [Requirement 4] Check format of the tour and total cost
    if not isinstance(tour, list) or not isinstance(total_cost, (int, float)):
        return "FAIL"
    if len(tour) <= 1 or any(not isinstance(city, int) for city in tour):
        return "FAIL"

    return "CORRECT"

# Example solution from the task, including provided tour and distance
solution_tour = [0, 5, 10, 4, 11, 0]
solution_total_cost = 184.24
result = verify_solution(solution_tour, solution_total_cost)
print(result)