import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_tour(tour, total_travel_cost):
    cities = [
        (50, 42), # Depot city 0
        (41, 1),  # City 1
        (18, 46), # City 2
        (40, 98), # City 3
        (51, 69), # City 4
        (47, 39), # City 5
        (62, 26), # City 6
        (79, 31), # City 7
        (61, 90), # City 8
        (42, 49)  # City 9
    ]
    
    # Check if the robot starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if the robot visits all cities exactly once, except for the depot city
    visited_cities = set(tour[1:-1])
    if len(visited_cities) != 9 or not all(city in visited_cities for city in range(1, 10)):
        return "FAIL"

    # Calculate the travel cost and check with the provided total_travel_cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city1_index = tour[i]
        city2_index = tour[i + 1]
        city1 = cities[city1_index]
        city2 = cities[city2_index]
        calculated_cost += euclidean_distance(city1[0], city1[1], city2[0], city2[1])
    
    if not math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Provided solution
tour = [0, 5, 9, 4, 8, 3, 2, 6, 7, 1, 0]
total_travel_cost = 295.9919678938414

# Testing the solution
result = verify_tour(tour, total_travel_cost)
print(result)