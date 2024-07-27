import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tsp_solution(tour, total_cost, cities):
    # Check start and end at depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if every city is visited exactly once (except depot visited twice)
    if sorted(tour) != [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        return "FAIL"
    
    # Calculate the total distance of the provided tour
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    
    # Check if the total cost matches
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Coordinates of the cities
cities = {
    0: (84, 67), 1: (74, 40), 2: (71, 13), 3: (74, 82), 4: (97, 28), 
    5: (0, 31), 6: (8, 62), 7: (74, 56), 8: (85, 71), 9: (6, 76)
}

# Solution given
tour = [0, 1, 2, 3, 4, 5, 6, 9, 8, 7, 0]
total_cost = 439.55

# Run the verification
result = verify_tsp_solution(tour, total_cost, cities)
print(result)