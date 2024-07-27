import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def test_tsp_solution():
    # Cities with coordinates
    cities = [
        (90, 3),  # Depot city 0
        (11, 17),
        (7, 27),
        (95, 81),
        (41, 54),
        (31, 35),
        (23, 95),
        (20, 56),
        (49, 29),
        (13, 17)
    ]
    
    # Proposed solution
    tour = [0, 5, 1, 2, 9, 7, 6, 4, 3, 8, 0]
    reported_total_cost = 418.32
    reported_max_dist = 69.43
    
    # Check if all cities are visited exactly once and return to depot
    if sorted(tour[:-1]) != list(range(1, len(cities))) + [0]:  # Include depot
        print("FAIL")
        return
    
    # Calculate the travel cost and max distance between consecutive cities
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        city1 = cities[tour[i]]
        city2 = cities[tour[i + 1]]
        distance = calculate_euclidean_distance(city1[0], city1[1], city2[0], city2[1])
        total_cost += distance
        if distance > max_distance:
            max_distance = distance
    
    # Check if the total travel cost and max distance match reported values
    if not (math.isclose(total_cost, reported_total_cost, rel_tol=1e-2) and
            math.isclose(max_distance, reported_max_dist, rel_tol=1e-2)):
        print("FAIL")
        return
    
    # If all tests pass
    print("CORRECT")

# Run the test function
test_tsp_solution()