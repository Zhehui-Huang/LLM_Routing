import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_tour(cities, tour, given_total_cost, given_max_distance):
    # Check if tour starts and ends at the depot (city index 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if all cities are visited exactly once (excluding the return to the depot)
    if sorted(tour[1:-1]) != list(range(1, len(cities))):
        return "FAIL"
    
    # Calculate total travel cost and maximum distance between consecutive cities
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        x1, y1 = cities[tour[i]]
        x2, y2 = cities[tour[i + 1]]
        distance = euclidean_distance(x1, y1, x2, y2)
        total_cost += distance
        if distance > max_distance:
            max_distance = distance
    
    # Compare calculated cost and maximum distance with given values
    if not math.isclose(total_cost, given_total_cost, abs_tol=1e-2) or not math.isclose(max_distance, given_max_distance, abs_tol=1e-2):
        return "FAIL"
    
    # If all checks pass, the solution is correct
    return "CORRECT"

# Coordinates for the cities including the depot city 0
cities = [
    (84, 67), # city 0
    (74, 40), # city 1
    (71, 13), # city 2
    (74, 82), # city 3
    (97, 28), # city 4
    (0, 31),  # city 5
    (8, 62),  # city 6
    (74, 56), # city 7
    (85, 71), # city 8
    (6, 76)   # city 9
]

# Proposed solution tour and its metrics
tour = [0, 8, 3, 9, 5, 6, 7, 1, 4, 2, 0]
total_travel_cost = 359.13
maximum_distance = 68.26

# Verify the solution
result = verify_tour(cities, tour, total_travel_cost, maximum_convex_distance)
print(result)