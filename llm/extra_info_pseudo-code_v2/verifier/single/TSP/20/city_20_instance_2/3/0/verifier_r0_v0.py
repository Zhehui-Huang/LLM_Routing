import math

# Function to calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Cities' coordinates
cities = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), 
    (38, 68), (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), 
    (18, 49), (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# Given solution
tour = [0, 12, 14, 16, 19, 11, 7, 18, 13, 15, 5, 1, 17, 4, 3, 10, 8, 6, 9, 2, 0]
calculated_cost = 478.4306776278287

# Validate the solution
def validate_solution(tour, calculated_cost, cities):
    # Check start and end at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check all cities visited once (excluding depot)
    unique_cities = set(tour[1:-1])
    if len(unique_cities) != len(cities) - 1:
        return "FAIL"
    
    # Check calculated tour cost
    total_cost = 0
    for i in range(len(tour)-1):
        total_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    
    # Check if the calculated total cost matches the provided cost
    if not math.isclose(total_cost, calculated_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Execute validation
result = validate_solution(tour, calculated_cost, cities)
print(result)