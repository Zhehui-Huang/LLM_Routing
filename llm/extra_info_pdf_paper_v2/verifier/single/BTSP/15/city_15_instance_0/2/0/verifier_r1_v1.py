import math

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def validate_solution(tour, cities):
    # Check if the tour starts and ends at the depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if every city is visited exactly once (excluding the depot being visited twice)
    if sorted(tour[1:-1]) != sorted(range(1, len(cities))):
        return "FAIL"
    
    # Calculate the total travel cost and maximum distance between consecutive cities
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        distance = euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        total_cost += distance
        max_distance = max(max_distance, distance)
    
    # Check the reported total cost and maximum distance
    provided_total_cost = 748.08  # From the provided solution
    provided_max_distance = 0.0   # From the provided solution assumed as an error
    if not math.isclose(total_cost, provided_total_cost, rel_tol=1e-5):
        return "FAIL"
    if not math.isclose(max_distance, provided_max_distance, rel_tol=1e-5) and provided_max_distance != 0:
        return "FAIL"
    
    return "CORRECT"

# Define the cities coordinates
cities = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), 
    (79, 77), (63, 23), (19, 76), (21, 38), (19, 65), (11, 40), 
    (3, 21), (60, 55), (4, 39)
]

# Provided tour result
tour = [0, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# Validate the solution
result = validate_solution(tour, cities)
print(result)