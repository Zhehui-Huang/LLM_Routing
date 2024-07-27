import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def test_solution():
    # Coordinates for each city including the depot
    city_coords = [
        (8, 11),  # City 0 - Depot
        (40, 6),  # City 1
        (95, 33), # City 2 
        (80, 60), # City 3
        (25, 18), # City 4
        (67, 23), # City 5
        (97, 32), # City 6
        (25, 71), # City 7
        (61, 16), # City 8
        (27, 91), # City 9
        (91, 46), # City 10
        (40, 87), # City 11
        (20, 97), # City 12
        (61, 25), # City 13
        (5, 59),  # City 14
        (62, 88), # City 15
        (13, 43), # City 16
        (61, 28), # City 17
        (60, 63), # City 18
        (93, 15)  # City 19
    ]

    # Provided solution details
    tour = [0, 16, 0, 13, 5, 8, 10, 2, 18, 12, 7, 9, 15, 3, 11, 14, 4, 17, 6, 1, 19, 1, 0]
    reported_total_cost = 819.5925805386328
    reported_max_distance = 62.64982043070834
    
    # Verify the tour starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Verify each city is visited exactly once, except city 0 and city 1
    from collections import Counter
    counter = Counter(tour)
    if counter[0] != 3 or counter[1] != 3 or any(counter[city] > 1 for city in range(2, 20)):
        return "FAIL"
    
    # Calculate and verify total cost and maximum distance
    calculated_total_cost = 0
    calculated_max_distance = 0
    
    for i in range(len(tour) - 1):
        city_1 = tour[i]
        city_2 = tour[i+1]
        dist = calculate_distance(city_coords[city_1], city_coords[city_2])
        calculated_total_cost += dist
        if dist > calculated_max_distance:
            calculated_max_distance = dist
    
    # Check that reported values approximately match the calculated ones
    if not (math.isclose(reported_total_cost, calculated_total_cost, abs_tol=1e-6) and
            math.isclose(reported_max_distance, calculated_max_distance, abs_tol=1e-6)):
        return "FAIL"

    return "CORRECT"

# Run the test function
result = test_solution()
print(result)