import math

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def verify_solution(cities, tour, total_cost, max_distance):
    # Verify tour starts and ends at depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if each city is visited exactly once, excluding the repeated visit to the depot
    visited = set(tour[1:-1])
    if len(visited) != len(cities) - 1 or len(tour) != len(cities) + 1:
        return "FAIL"

    # Check total travel cost and max distance between consecutive cities
    calculated_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        distance = euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        calculated_cost += distance
        if distance > calculated_max_distance:
            calculated_max_distance = distance
    
    # Allow for a small margin of error due to floating point precision
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-2) or not math.isclose(calculated_max_distance, max_distance, rel_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Define city coordinates
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42), 5: (36, 30),
    6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14), 10: (51, 28), 11: (44, 79),
    12: (56, 58), 13: (72, 43), 14: (6, 99)
}

# Provided solution
tour = [0, 6, 11, 8, 1, 14, 12, 4, 3, 10, 5, 9, 13, 7, 2, 0]
total_cost = 322.50
max_distance = 64.66

# Run verification
result = verify_solution(cities, tour, total_cost, max_distance)
print(result)