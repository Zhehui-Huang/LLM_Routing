import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, total_cost, cities):
    # Verify the robot starts and ends its tour at the depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Verify the robot visits exactly 5 cities including the depot city
    if len(tour) != 6:
        return "FAIL"
    
    # Verify all visited cities are distinct and within the valid range of [0, 9]
    if len(set(tour)) != len(tour) or any(city < 0 or city > 9 for city in tour):
        return "FAIL"
    
    # Calculate the travel cost based on Euclidean distance and compare with the given cost
    calculated_cost = 0.0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"


# Define available cities with their coordinates
cities = {
    0: (53, 68), 1: (75, 11), 2: (91, 95), 3: (22, 80), 4: (18, 63), 
    5: (54, 91), 6: (70, 14), 7: (97, 44), 8: (17, 69), 9: (95, 89)
}

# Solution given
tour = [0, 4, 8, 3, 5, 0]
total_cost = 110.38

# Verify the solution
result = verify_solution(tour, total_cost, cities)
print(result)