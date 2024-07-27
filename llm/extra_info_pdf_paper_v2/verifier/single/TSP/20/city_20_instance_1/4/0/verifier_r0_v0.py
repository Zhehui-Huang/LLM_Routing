import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_cost, city_locations):
    # Verify the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Verify all cities are visited exactly once, besides the depot which should be visited twice (start/end)
    if sorted(tour) != sorted([0] * 2 + list(range(1, 20))):
        return "FAIL"

    # Calculate the travel cost from the tour using Euclidean distance
    computed_cost = 0
    for i in range(len(tour) - 1):
        computed_cost += calculate_distance(city_locations[tour[i]], city_locations[tour[i+1]])

    # Compare the calculated cost with the provided total cost, allowing a small tolerance for floating point comparison
    if not math.isclose(computed_cost, total_cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Locations of cities (index corresponds to city number)
city_locations = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56),
    (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29),
    (21, 79), (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

# Provided tour and total travel cost
tour = [0, 3, 14, 5, 7, 4, 10, 11, 16, 17, 19, 15, 18, 8, 1, 13, 12, 2, 9, 6, 0]
total_cost = 376.93

# Run verification
result = verify_solution(tour, total_cost, city_locations)
print(result)