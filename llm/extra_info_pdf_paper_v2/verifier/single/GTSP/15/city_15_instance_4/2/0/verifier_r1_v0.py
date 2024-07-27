import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, cost):
    # Environment cities coordinates
    cities = {
        0: (35, 40), 
        1: (39, 41),
        2: (81, 30),
        3: (5, 50),
        4: (72, 90),
        5: (54, 46),
        6: (8, 70),
        7: (97, 62),
        8: (14, 41),
        9: (70, 44),
        10: (27, 47),
        11: (41, 74),
        12: (53, 80),
        13: (21, 21),
        14: (12, 39)
    }

    groups = [
        [3, 8],
        [4, 13],
        [1, 2],
        [6, 14],
        [5, 9],
        [7, 12],
        [10, 11]
    ]

    # Verify if tour starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Verify if the tour contains exactly one city from each group
    visited_groups = set()
    for city_index in tour[1:-1]:
        for group_index, group in enumerate(groups):
            if city_index in group:
                if group_index in visited_groups:
                    return "FAIL"
                visitedched_groups.add(group_index)
                break
    
    if len(visited_groups) != len(groups):
        return "FAIL"
    
    # Verify the total distance cost
    computed_cost = 0
    for i in range(len(tour) - 1):
        computed_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    
    if abs(computed_cost - cost) > 1e-5:
        return "FAIL"
    
    return "CORRECT"

# Define the provided tour and cost
tour = [0, 8, 13, 1, 14, 5, 12, 11, 0]
cost = 220.73043826129523

# Verify the correctness of the solution
result = verify_solution(tour, cost)
print(result)