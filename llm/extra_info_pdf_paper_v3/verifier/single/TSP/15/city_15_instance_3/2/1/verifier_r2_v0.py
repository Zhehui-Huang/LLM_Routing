import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y1 - y2) ** 2)

def verify_tour(tour, total_calculated_cost):
    coordinates = [
        (16, 90),  #city 0
        (43, 99),  #city 1
        (80, 21),  #city 2
        (86, 92),  #city 3
        (54, 93),  #city 4
        (34, 73),  #city 5
        (6, 61),   #city 6
        (86, 69),  #city 7
        (30, 50),  #city 8
        (35, 73),  #city 9
        (42, 64),  #city 10
        (64, 30),  #city 11
        (70, 95),  #city 12
        (29, 64),  #city 13
        (32, 79)   #city 14
    ]
    
    # Check Requirement 1: Start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check Requirement 2: Visit all other cities exactly once
    cities_visited = sorted(tour[1:-1])
    if cities_visited != list(range(1, 15)):
        return "FAIL"
    
    # Check Requirement 4: Output tour should start and end at depot city 0
    if not (tour[0] == 0 and tour[-1] == 0):
        return "FAIL"

    # Check Requirement 5: Correct calculation of tour cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        c1 = tour[i]
        c2 = tour[i + 1]
        calculated_cost += calculate_euclidean_distance(coordinates[c1][0], coordinates[c1][1],
                                                        coordinates[c2][0], coordinates[c2][1])

    if not math.isclose(calculated_cost, total_calculated_cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Given solution
tour = [0, 14, 5, 9, 1, 13, 6, 10, 4, 8, 12, 3, 7, 11, 2, 0]
total_travel_cost = 738.0588945493764

# Run the verification
result = verify_tour(tour, total_travel_cost)
print(result)