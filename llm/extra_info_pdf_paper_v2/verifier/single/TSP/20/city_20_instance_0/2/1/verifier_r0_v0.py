import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y1 - y2) ** 2)

def verify_tour(tour, total_travel_cost):
    # Coordinates of the cities
    coordinates = [
        (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32),
        (25, 71), (61, 16), (27, 91), (91, 46), (40, 87), (20, 97), (61, 25), 
        (5, 59), (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
    ]
    
    # Check Requirement 1
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check Requirement 2
    if len(set(tour)) != len(tour) or len(tour) != 21:
        return "FAIL"
    if sorted(tour) != list(range(20)):
        return "FAIL"
    
    # Check Requirement 3
    computed_cost = 0
    for i in range(len(tour) - 1):
        city1 = coordinates[tour[i]]
        city2 = coordinates[tour[i+1]]
        computed_cost += calculate_distance(city1[0], city1[1], city2[0], city2[1])
    
    if abs(total_travel_cost - computed_cost) > 1e-5:
        return "FAIL"
    
    # Requirements 4 & 5 are implicit in the input and computation of cost
    return "CORRECT"

# Provided solution to verify
tour_solution = [0, 4, 1, 8, 13, 17, 5, 19, 6, 2, 10, 3, 18, 15, 11, 9, 12, 7, 14, 16, 0]
total_travel_cost_solution = 349.1974047195548

# Verify the solution
result = verify_tour(tour_solution, total_travel_cost_solution)
print(result)