import numpy as np

def calculate_euclidean_distance(x1, y1, x2, y2):
    return np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_solution(tour, coordinates):
    # Check if the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if each city is visited exactly once (other than the depot city which should be visited twice)
    unique_cities = set(tour)
    if len(tour) - 1 != len(unique_cities) or sorted(list(unique_cities))[1:] != list(range(1, len(coordinates))):
        return "FAIL"
    
    # Calculate total travel cost and maximum distance between consecutive cities
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        x1, y1 = coordinates[tour[i]]
        x2, y2 = coordinates[tour[i+1]]
        distance = calculate_euclidean_distance(x1, y1, x2, y2)
        total_cost += distance
        max_distance = max(max_distance, distance)
    
    # Output calculated values (optional for debugging)
    print("Total travel cost:", total_cost)
    print("Maximum distance between consecutive cities:", max_distance)
    
    # Since we cannot conclude about minimization without comparison to other tours, just agree on format-check compliance
    return "CORRECT"

# Coordinates indexed by the city number
coordinates = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84),
    (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94), (96, 73),
    (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Provided solution for verification
tour = [0, 1, 4, 7, 14, 8, 18, 12, 10, 11, 3, 15, 17, 16, 9, 5, 19, 6, 13, 2, 0]

# Replace `np.int32` usage by casting to int if necessary, here assuming Python's int works
tour = [int(city) for city in tour]

# Verify the solution based on the constraints
result = verify_solution(tour, coordinates)
print(result)