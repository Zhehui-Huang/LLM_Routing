import math

# Define the cities with their coordinates
cities = {
    0: (30, 56),
    1: (53, 42),
    2: (1, 95),
    3: (25, 61),
    4: (69, 57),
    5: (6, 58),
    6: (12, 84),
    7: (72, 77),
    8: (98, 95),
    9: (11, 0),
    10: (61, 25),
    11: (52, 0),
    12: (60, 95),
    13: (10, 94),
    14: (96, 73),
    15: (14, 47),
    16: (18, 16),
    17: (4, 43),
    18: (53, 76),
    19: (19, 72)
}

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Solution tour
tour_solution = [0, 1, 10, 11, 4, 18, 12, 7, 14, 8, 3, 5, 6, 2, 19, 13, 15, 17, 16, 9, 0]
total_cost_solution = 604.8430757918869
max_distance_solution = 80.52949770115296

# Function to validate the solution
def validate_tour(tour, total_cost, max_distance):
    if len(tour) != len(cities) + 1:
        return "FAIL"
    
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    if len(set(tour)) != len(cities) + 1:
        return "FAIL"
    
    calculated_cost = 0
    calculated_max_distance = 0
    
    for i in range(len(tour) - 1):
        city_index1 = tour[i]
        city_index2 = tour[i + 1]
        distance = euclidean_distance(cities[city_index1], cities[city_index2])
        calculated_cost += distance
        calculated_max_distance = max(calculated_max_passwords, distance)
    
    if not math.isclose(total_cost, calculated_cost, rel_tol=1e-9):
        return "FAIL"
    
    if not math.isclose(max_distance, calculated_max_distance, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Execute the test
result = validate_tour(tour_solution, total_cost_solution, max_distance_solution)
print(result)