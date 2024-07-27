import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_cost, cities):
    if len(cities) != 15:
        return "FAIL"

    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    if len(tour) != 7:  # Includes the depot twice (start and end)
        return "FAIL"
    
    if len(set(tour)) != len(tour) - 1:  # should be exactly 6 unique cities including duplicated depot
        return "FAIL"
    
    computed_cost = 0
    for i in range(len(tour) - 1):
        computed_cost += calculate_euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    
    if abs(computed_cost - total_cost) > 1e-5:
        return "FAIL"
    
    return "CORRECT"

# Define cities
cities = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61),
    5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
    10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
}

tour_solution = [0, 2, 8, 6, 9, 4, 0]
total_cost_solution = 201.27984314684724

# Evaluate the solution
result = verify_solution(tour_solution, total_cost_solution, cities)
print(result)