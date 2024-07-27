import math

# City coordinates
cities = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61), 
    5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36), 
    10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
}

# Tour from the solution
tour = [0, 5, 13, 11, 12, 2, 8, 14, 6, 1, 7, 3, 9, 10, 4, 0]
# Provided values for validation
provided_total_distance = 355.52373661497694
provided_max_distance = 50.21951811795888

def euclidean_distance(a, b):
    """Calculate the Euclidean distance between two cities."""
    x1, y1 = cities[a]
    x2, y2 = cities[b]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def check_tour(tour, provided_total_distance, provided_max_distance):
    # Check start and end at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check all cities visited exactly once
    if sorted(tour[:-1]) != sorted(set(cities.keys())):
        return "FAIL"
    
    # Calculate distances
    distances = [euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1)]
    total_distance = sum(distances)
    max_distance = max(distances)
    
    # Check against provided values
    if not math.isclose(total_distance, provided_total_distance, abs_tol=1e-4):
        return "FAIL"
    if not math.isclose(max_distance, provided_max_distance, abs_tol=1e-4):
        return "FAIL"
    
    return "CORRECT"

# Run the test
result = check_tour(tour, provided_total_distance, provided_max_distance)
print(result)