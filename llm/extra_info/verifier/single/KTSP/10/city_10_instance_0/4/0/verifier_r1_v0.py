import math

# Define a function to calculate Euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Define the cities' coordinates
cities = {
    0: (50, 42), # Depot city
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Function to check the solution based on given requirements
def check_solution(tour, claimed_cost):
    if len(tour) != 5:
        return "FAIL"
    
    # Check if tour starts and ends at depot (Requirement 1)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if exactly four cities are visited (Requirement 2)
    if len(set(tour)) != 4:
        return "FAIL"
    
    # Calculate the total travel cost using Euclidean distance (Requirement 4)
    total_cost = 0
    for i in range(len(tour) - 1):
        city1 = cities[tour[i]]
        city2 = cities[tour[i+1]]
        total_cost += euclidean_distance(city1, city2)
    
    # Check if calculated cost matches the claimed cost 
    if not math.isclose(total_cost, claimed_cost, rel_tol=1e-4):
        return "FAIL"
    
    # If all conditions passed
    return "CORRECT"

# Provided solution details
tour_provided = [0, 9, 5, 6, 0]
total_travel_cost_provided = 61.66

# Verify the solution
result = check_solution(tour_provided, total_travel_cost_provided)
print(result)