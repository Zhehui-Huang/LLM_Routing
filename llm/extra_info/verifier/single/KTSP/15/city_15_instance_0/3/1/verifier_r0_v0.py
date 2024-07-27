import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_tour(tour, cities):
    # Verify tour starts and ends at the depot, and has exactly 5 cities (including depot twice)
    if tour[0] != 0 or tour[-1] != 0 or len(tour) != 5:
        return False, 0
    
    # Verify it visits exactly 4 cities including the depot
    if len(set(tour)) != 4:
        return False, 0
    
    # Calculate total travel cost
    total_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        x1, y1 = cities[city1]
        x2, y2 = cities[city2]
        total_cost += calculate_euclidean_distance(x1, y1, x2, y2)
    
    return True, total_cost

# Cities coordinates (indexed as mentioned in the problem)
cities = [(9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), 
          (79, 77), (63, 23), (19, 76), (21, 38), (19, 65), (11, 40), 
          (3, 21), (60, 55), (4, 39)]

# Given solution
tour = [0, 8, 10, 11, 0]
total_cost_reported = 110.01

# Verification process
is_valid, calculated_cost = verify_tour(tour, cities)

# Check if the reported total cost and calculated cost are close enough (float comparison)
if is_valid and math.isclose(total_cost_reported, calculated_cost, abs_tol=0.01):
    print("CORRECT")
else:
    print("FAIL")