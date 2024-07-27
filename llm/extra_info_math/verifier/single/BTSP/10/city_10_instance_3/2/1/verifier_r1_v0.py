import math

# Define cities and their coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Sample solution from the solver
tour = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# Assuming this is the max distance calculated by solver
max_distance_from_solver = 68.26419266 

def compute_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def validate_tour(tour, cities):
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL", "Tour does not start and end at depot city 0"
    
    visited = set(tour)
    if len(visited) != len(cities) or len(tour) != len(cities) + 1:
        return "FAIL", "Tour does not visit each city exactly once"
    
    # Check maximum distance between consecutive cities
    actual_max_distance = max(
        compute_euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) 
        for i in range(len(tour) - 1)
    )
    
    if abs(actual_max_distance - max_distance_from_solver) > 1e-5:
        return "FAIL", "Calculated maximum distance does not match the optimal solution"

    return "CORRECT", None

# Perform validation
result, error = validate_tour(tour, cities)
print("Validation Result:", result)
if error:
    print("Error:", error)