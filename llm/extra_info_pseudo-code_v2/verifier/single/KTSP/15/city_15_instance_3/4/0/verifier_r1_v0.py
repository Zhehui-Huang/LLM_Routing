import math

# Function to calculate Euclidean distance
def euclidean_distance(city_a, city_b):
    return math.sqrt((city_a[0] - city_b[0])**2 + (city_a[1] - city_b[1])**2)

# Function to verify the solution
def verify_solution(tour, total_travel_cost, city_coordinates):
    # Verify the tour starts and ends at the depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Verify the robot visits exactly 10 cities, including depot
    if len(set(tour)) != 11:
        return "FAIL"
    
    # Calculate the total travel cost using Euclidean distance and check if it matches provided cost
    calculated_cost = 0
    for i in range(len(tour)-1):
        calculated_cost += euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
    
    # Allow small floating-point discrepancies
    if not math.isclose(calculated_cost, total_travel_cost, abs_tol=0.1):
        return "FAIL"
    
    # If all checks pass, the solution is considered correct
    return "CORRECT"

# Provided city coordinates
city_coords = [(16, 90), (43, 99), (80, 21), (86, 92), (54, 93), (34, 73), (6, 61), (86, 69), (30, 50), (35, 73), 
               (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)]

# Provided tour and total travel cost
sample_tour = [0, 14, 5, 13, 8, 10, 9, 12, 4, 1, 0]
sample_total_cost = 178.37

# Call the verification function and print the result
result = verify_solution(sample_tour, sample_total_cost, city_coords)
print(result)