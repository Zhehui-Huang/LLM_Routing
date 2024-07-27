import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def check_tour(tour, total_travel_cost):
    cities = [
        (26, 60), (73, 84), (89, 36), (15, 0), (11, 10),
        (69, 22), (28, 11), (70, 2), (47, 50), (60, 29),
        (29, 26), (85, 68), (60, 1), (71, 73), (82, 47),
        (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
    ]

    # Check if starts and ends at the depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if the route includes exactly 16 cities.
    if len(set(tour)) != 16:
        return "FAIL"
    
    # Check if cities indices are valid
    if any(x not in range(len(cities)) for x in tour):
        return "FAIL"
    
    # Calculate the travel cost and compare with the given total_travel_cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = cities[tour[i]]
        x2, y2 = cities[tour[i+1]]
        calculated_cost += calculate_euclidean_distance(x1, y1, x2, y2)

    if not math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Tour and cost provided as part of the solution
provided_tour = [0, 15, 10, 6, 4, 3, 12, 9, 5, 2, 14, 11, 1, 18, 8, 19, 0]
provided_total_travel_cost = 376.9293543426522

# Test the solution
result = check_tour(provided_tour, provided_total_travel_cost)
print(result)