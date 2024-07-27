import math

def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

def verify_solution(cities, tour, reported_cost):
    # Check if the number of cities provided is correct
    if len(cities) != 10:
        return "FAIL"
    
    # Check if the robot starts at the depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if exactly 5 cities are visited, including the depot
    if len(tour) != 6:
        return "FAIL"
    
    # Calculate the total travel cost using Euclidean distance
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    
    # Check if the calculated cost matches the reported cost
    if not math.isclose(total_cost, reported_cost, rel_tol=1e-3):
        return "FAIL"
    
    return "CORRECT"

# Define cities coordinates
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Solution tour and total travel cost provided
solution_tour = [0, 4, 8, 3, 5, 0]
solution_reported_cost = 110.38

# Verify the solution
result = verify_solution(cities, solution_tour, solution_reported_cost)
print(result)