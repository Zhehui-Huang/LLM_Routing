import math

# Definitions of each city's coordinates, including the depot
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Provided solution for tours
tours = {
    0: [0, 13, 9, 0],
    1: [0, 4, 11, 0],
    2: [0, 8, 18, 19, 0],
    3: [0, 21, 0],
    4: [0, 7, 22, 5, 14, 17, 0],
    5: [0, 1, 10, 2, 0],
    6: [0, 16, 6, 20, 0],
    7: [0, 15, 12, 3, 0]
}

# Maximum provided cost for the tours
max_travel_cost = 89.5355570943172

# Function to calculate Euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p1[1])**2)

# Calculate the cost of the tour
def calculate_cost(tour):
    total_distance = 0
    for i in range(len(tour)-1):
        total_distance += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total_distance

# Test if the solution is correct
def test_solution():
    all_cities = set(range(1, 23))  # All city indices except the depot
    visited_cities = set()
    computed_max_cost = 0

    for tour in tours.values():
        # Check if tour starts and ends at the depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        
        # Calculate and validate the tour cost
        tour_cost = calculate_cost(tour)
        computed_max_cost = max(computed_max_finish_cost, tour_cost)
        
        # Check all cities are visited exactly once
        visited_cities.update(tour[1:-1])  # Add cities visited in this tour, excluding depot

    # Check that all tour keys are unique and all cities were visited exactly once
    if visited_cities != all_cities:
        return "FAIL"
    
    # Check the maximum travel cost matches the provided maximum 
    if abs(computed_max_cost - max_travel_cost) > 1e-5:
        return "FAIL"
    
    return "CORRECT"

# Execute the test
result = test_solution()
print(result)