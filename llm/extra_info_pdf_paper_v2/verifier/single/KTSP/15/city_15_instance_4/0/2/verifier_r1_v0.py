import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, cost, all_cities):
    # Requirement 1: Start and end at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Must visit exactly 12 out of the 15 given cities
    if len(set(tour)) != 12:
        return "FAIL"
    
    # Requirement 4: The solution output must include the tour as a list of city indices and the calculated total travel cost
    calculated_cost = 0
    for i in range(len(tour)-1):
        calculated_cost += calculate_distance(all_cities[tour[i]], all_cities[tour[i+1]])

    if abs(calculated_cost - cost) > 1e-6:
        return "FAIL"

    # Passed all checks
    return "CORRECT"

# Given all cities coordinates, including the depot city
cities_coordinates = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50),
    4: (72, 90), 5: (54, 46), 6: (8, 70), 7: (97, 62),
    8: (14, 41), 9: (70, 44), 10: (27, 47), 11: (41, 74),
    12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Provided solution tour and cost
solution_tour = [0, 10, 8, 14, 3, 12, 11, 4, 7, 2, 9, 5, 0]
solution_cost = 272.88822510830244

# Verify the solution
print(verify_solution(solution_tour, solution_cost, cities_coordinates))