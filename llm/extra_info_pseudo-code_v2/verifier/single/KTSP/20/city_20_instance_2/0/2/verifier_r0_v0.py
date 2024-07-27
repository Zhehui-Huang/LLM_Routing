import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_tour(tour, cost):
    # City coordinates
    coordinates = [
        (3, 26),  # Depot
        (85, 72), (67, 0), (50, 99), (61, 89), 
        (91, 56), (2, 65), (38, 68), (3, 92), 
        (59, 8), (30, 88), (30, 53), (11, 14), 
        (52, 49), (18, 49), (64, 41), (28, 49), 
        (91, 94), (51, 58), (30, 48)
    ]
    
    # Check the number of cities visited including depot
    if len(tour) != 10:
        return "FAIL"
    
    # Check if tour starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Calculate the total travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = coordinates[tour[i]]
        x2, y2 = coordinates[tour[i + 1]]
        calculated_cost += calculate_euclidean_distance(x1, y1, x2, y2)
    
    # Check if the calculated cost matches the given cost (rounded to 2 decimal places)
    if not (abs(calculated_cost - cost) < 0.01):
        return "FAIL"

    return "CORRECT"

# Given solution
tour = [0, 16, 19, 1, 17, 10, 7, 2, 12, 0]
total_travel_cost = 347.92

# Check the solution
result = verify_tour(tour, total_travel_cost)
print(result)