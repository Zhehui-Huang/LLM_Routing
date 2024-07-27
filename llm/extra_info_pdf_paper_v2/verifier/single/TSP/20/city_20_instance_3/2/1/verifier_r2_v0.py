import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def validate_tour_and_cost(tour, cost, cities):
    # Check if tour starts and ends at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check that all cities are visited exactly once
    if sorted(tour) != sorted(list(range(len(cities)))):
        return "FAIL"

    # Calculate the total travel cost
    calculated_cost = 0
    for i in range(1, len(tour)):
        x1, y1 = cities[tour[i - 1]]
        x2, y2 = cities[tour[i]]
        calculated_cost += euclidean_distance(x1, y1, x2, y2)

    # Compare the provided cost with the calculated cost
    if not math.isclose(cost, calculated_cost, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Coordinates of cities including the depot
cities_coordinates = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), (72, 77),
    (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94), (96, 73), (14, 47),
    (18, 16), (4, 43), (53, 76), (19, 72)
]

# Given solution
tour = [0, 3, 19, 6, 13, 2, 5, 15, 17, 16, 9, 11, 10, 1, 4, 7, 18, 12, 8, 14, 0]
total_travel_cost = 458.36719998557066

# Validate the given solution
result = validate_tour_and_cost(tour, total_travel_cost, cities_coordinates)
print(result)  # Expected output: "CORRECT" or "FAIL"