import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def test_solution():
    cities = [
        (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), 
        (4, 56), (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), 
        (6, 19), (26, 29), (21, 79), (49, 23), (78, 76), (68, 45), 
        (50, 28), (69, 9)
    ]
    tour = [0, 14, 9, 2, 13, 8, 1, 0]
    reported_total_cost = 143.83

    # Check Requirement 1: Start and end at depot city (city index 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check Requirement 2: Exactly 7 cities visited, including the depot
    if len(set(tour)) != 7:
        return "FAIL"

    # Check Requirement 3: Verify the travel cost
    calculated_total_cost = 0
    for i in range(len(tour) - 1):
        calculated_total_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    calculated_total_cost = round(calculated_total_cost, 2)
    
    if calculated_total_cost != reported_total_cost:
        return "FAIL"

    return "CORRECT"

# Running the test
result = test_solution()
print(result)