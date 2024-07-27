import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def test_solution():
    # Given coordinates of the cities including the depot
    city_coords = [
        (8, 11),    # City 0 - Depot
        (40, 6),    # City 1
        (95, 33),   # City 2
        (80, 60),   # City 3
        (25, 18),   # City 4
        (67, 23),   # City 5
        (97, 32),   # City 6
        (25, 71),   # City 7
        (61, 16),   # City 8
        (27, 91),   # City 9
        (91, 46),   # City 10
        (40, 87),   # City 11
        (20, 97),   # City 12
        (61, 25),   # City 13
        (5, 59),    # City 14
        (62, 88),   # City 15
        (13, 43),   # City 16
        (61, 28),   # City 17
        (60, 63),   # City 18
        (93, 15)    # City 19
    ]

    # Solution provided
    tour = [0, 16, 0, 13, 5, 8, 10, 2, 18, 12, 7, 9, 15, 3, 11, 14, 4, 17, 6, 1, 19, 1, 0]
    reported_total_cost = 819.5925805386328
    reported_max_distance = 62.64982043070834
    
    # Verify the tour starts and ends at the depot and includes each city exactly once
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    visited = set(tour)
    if len(visited) != len(city_coords) or any(tour.count(city) != 1 for city in range(1, len(city_coords)) if city not in [0, 1]):
        return "FAIL"
    
    # Calculate total travel cost and max distance
    calculated_total_cost = 0
    calculated_max_distance = 0
    
    for i in range(len(tour) - 1):
        distance = calculate_distance(city_coords[tour[i]], city_coords[tour[i+1]])
        calculated_total_cost += distance
        if distance > calculated_max_distance:
            calculated_max_distance = distance
    
    # Check if the reported values are correct
    if not (math.isclose(reported_total_cost, calculated_total_gpu, abs_tol=1e-9) and
            math.isclose(reported_max_distance, calculated_max_distance, abs_tol=1e-9)):
        return "FAIL"
    
    return "CORRECT"

# Run the test function
result = test_solution()
print(result)