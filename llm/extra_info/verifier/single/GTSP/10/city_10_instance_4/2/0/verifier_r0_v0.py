import math

# Provided tour and total cost
tour = [0, 4, 6, 7, 5, 9, 8, 3, 0]
provided_total_cost = 371.19

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

# City groups
city_groups = [
    [1, 4],
    [2, 6],
    [7],
    [5],
    [9],
    [8],
    [3]
]

def calculate_distance(p1, p2):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def validate_tour(tour, city_groups, cities):
    # Checking if the tour starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if tour covers exactly one city from each group
    visited_cities = set(tour[1:-1])  # Exclude the starting and ending depot
    for group in city_groups:
        if not visited_cities & set(group):
            return "FAIL"
    
    # Calculate the travel cost and compare with provided total cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        start_city, end_city = tour[i], tour[i + 1]
        calculated_cost += calculate_distance(cities[start_city], cities[end_city])
    
    # Checking cost with a tolerance due to floating point arithmetic considerations
    if abs(calculated_cost - provided_total_cost) > 1e-2:
        return "FAIL"
    
    return "CORRECT"

# Run the validation function
result = validate_tour(tour, city_groups, cities)
print(result)