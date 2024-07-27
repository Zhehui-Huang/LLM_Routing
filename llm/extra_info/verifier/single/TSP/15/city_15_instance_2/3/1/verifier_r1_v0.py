import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def validate_tour_and_cost(tour, total_calculated_cost, city_coordinates):
    n = len(city_coordinates)
    
    # Check if tour starts and ends at depot, and includes all cities exactly once
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    if sorted(tour[1:-1]) != list(range(1, n)):
        return "FAIL"
    
    # Calculate the total travel cost based on the tour
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city_a = city_coordinates[tour[i]]
        city_b = city_coordinates[tour[i + 1]]
        calculated_cost += calculate_distance(city_a, city_b)
    
    # Compare the calculated cost with provided cost
    if round(calculated_cost) != total_calculated_cost:
        return "FAIL"
    
    return "CORRECT"

# Provided city coordinates
city_coordinates = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), 
    (36, 30), (52, 82), (93, 44), (21, 78), (68, 14), 
    (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)
]

# Proposed solution
tour = [0, 6, 11, 8, 1, 14, 12, 4, 3, 10, 5, 9, 13, 7, 2, 0]
total_cost = 322

# Validate the solution
result = validate_tour_and_cost(tour, total_cost, city_coordinates)
print(result)