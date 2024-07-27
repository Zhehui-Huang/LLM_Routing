import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_tour(tour, travel_cost):
    coordinates = [
        (54, 87),  # City 0
        (21, 84),  # City 1
        (69, 84),  # City 2
        (53, 40),  # City 3
        (54, 42),  # City 4
        (36, 30),  # City 5
        (52, 82),  # City 6
        (93, 44),  # City 7
        (21, 78),  # City 8
        (68, 14),  # City 9
        (51, 28),  # City 10
        (44, 79),  # City 11
        (56, 58),  # City 12
        (72, 43),  # City 13
        (6, 99)    # City 14
    ]
    
    # Check starting and ending at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check for exactly 8 cities including the depot city
    if len(set(tour)) != 8 or len(tour) != 9:  # tour includes depot city twice, hence 9 entries
        return "FAIL"
    
    # Calculate the total travel cost and compare with provided cost
    calculated_cost = sum(calculate_euclidean_distance(
        coordinates[tour[i]][0], coordinates[tour[i]][1],
        coordinates[tour[i + 1]][0], coordinates[tour[i + 1]][1]
    ) for i in range(len(tour) - 1))
    
    # Check if calculated cost is close to the reported cost within a tiny margin
    if not math.isclose(calculated_cost, travel_cost, abs_tol=0.01):
        return "FAIL"
    
    return "CORRECT"

# Given solution information
tour = [0, 2, 13, 3, 4, 12, 11, 6, 0]
total_travel_cost = 132.12

# Verify the solution with the constraints
result = verify_tour(tour, total_travel_cost)
print(result)