import math

# City coordinates
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Solution Tour and Cost
tour = [0, 9, 8, 7, 6, 5, 4, 3, 0]
cost = float('inf')

def calculate_euclidean_distance(city_a, city_b):
    return math.sqrt((cities[city_a][0] - cities[city_b][0])**2 + (cities[city_a][1] - cities[city_b][1])**2)

def verify_solution(cities, tour, cost):
    # Verify the tour starts and ends at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Verify exactly 8 cities are visited (including depot)
    if len(set(tour)) != 8:
        return "FAIL"
    
    # Verify all cities in tour are from the 0-9 range
    if any(city not in cities for city in tour):
        return "FAIL"
    
    # Calculate travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_euclidean_distance(tour[i], tour[i + 1])
    
    # Verify calculated cost matches the given cost
    if calculated_cost != cost:
        return "FAIL"
    
    return "CORRECT"

# Run the verification
result = verify_solution(cities, tour, cost)
print(result)