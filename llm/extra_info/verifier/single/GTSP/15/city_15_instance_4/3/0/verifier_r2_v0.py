import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_cost_calculated):
    cities = [
        (35, 40),  # Depot 0
        (39, 41),  # 1
        (81, 30),  # 2
        (5, 50),  # 3
        (72, 90),  # 4
        (54, 46),  # 5
        (8, 70),  # 6
        (97, 62),  # 7
        (14, 41),  # 8
        (70, 44),  # 9
        (27, 47),  # 10
        (41, 74),  # 11
        (53, 80),  # 12
        (21, 21),  # 13
        (12, 39)   # 14
    ]

    # Verify if the robot starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Groups definition
    groups = [[3, 8], [4, 13], [1, 2], [6, 14], [5, 9], [7, 12], [10, 11]]
    visited_groups = []

    # Verify if exactly one city from each group is visited
    for group in groups:
        if sum(city in tour for city in group) != 1:
            return "FAIL"
        else:
            visited_groups.append([city for city in group if city in tour][0])

    # Calculate actual total cost
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])

    # Mathematically comparing float values
    if not math.isclose(total_cost, total_cost_calculated, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Input the solution tour and cost
tour = [0, 8, 13, 1, 14, 5, 12, 11, 0]
total_cost = 220.73

# Checking the solution
result = verify_solution(tour, total_data)
print(result)  # Output should be "CORRECT" if everything is verified, otherwise "FAIL"