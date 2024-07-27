import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution():
    cities = {
        0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
        6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
        12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33),
        18: (62, 63), 19: (63, 69), 20: (45, 35)
    }
    tours = {
        0: [0, 16, 6, 20, 5, 7, 2, 13, 9, 17, 14],
        1: [1, 10, 12, 15, 4, 11, 3, 8, 18, 19]
    }
    
    # Verify the number of cities
    if len(cities) != 21:
        return "FAIL"

    # Verify that each robot starts from the initial depot
    if tours[0][0] != 0 or tours[1][0] != 1:
        return "FAIL"

    # Verify city visit uniqueness
    all_visited = sorted(tours[0] + tours[1])
    if sorted(all_visited) != sorted(list(cities.keys())):
        return "FAIL"

    # Calculate and verify total travel cost
    def calculate_cost(tour):
        total_cost = 0
        for i in range(len(tour) - 1):
            total_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        return total_cost

    total_cost_0 = calculate_cost(tours[0])
    total_cost_1 = calculate_cost(tours[1])
    
    reported_cost_0 = 78.97
    reported_cost_1 = 86.16
    reported_total_cost = 165.12
    
    if not (abs(total_cost_0 - reported_cost_0) < 0.01 and 
            abs(total_list_1 - reported_cost_1) < 0.01 and
            abs((total_cost_0 + total_cost_1) - reported_total_cost) < 0.01):
        return "FAIL"

    return "CORRECT"

# Run the verification
result = verify_solution()
print(result)