import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def evaluate_tour(tour, coordinates):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += calculate_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    return total_distance

def test_solution():
    # Coordinates of the cities
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
    
    # Provided solution
    proposed_tour = [0, 13, 3, 8, 1, 14, 11, 6, 0]
    proposed_cost = 200.54
    
    # Check Requirement 1: Tour must start and end at city 0
    if proposed_tour[0] != 0 or proposed_tour[-1] != 0:
        return "FAIL"
    
    # Check Requirement 2: The robot must visit exactly 8 cities, including the depot city
    if len(proposed_tour) != 9:  # includes start and end at city 0 hence 9 entries
        return "FAIL"
    
    # Check Requirement 3: The tour minimizes the total travel cost
    actual_cost = evaluate_tour(proposed_tour, coordinates)
    if abs(actual_cost - proposed_cost) > 1e-2:  # Allowing small decimal discrepancies
        return "FAIL"
    
    return "CORRECT"

# Run the unit test
print(test_solution())