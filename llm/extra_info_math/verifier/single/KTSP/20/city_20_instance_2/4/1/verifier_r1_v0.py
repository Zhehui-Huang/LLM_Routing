import math

def calculate_distance(city1, city2):
    # Calculate Euclidean distance between two cities
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, total_travel_cost, city_coordinates):
    # Check if the tour starts and ends at the depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if exactly 10 cities are visited including the depot
    if len(set(tour)) != 10:
        return "FAIL"
    
    # Check to calculate the total travel distance
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
    
    # Compare the calculated cost with the provided total travel cost
    if not math.isclose(calculated_data_given_cost, total_travel_cost, rel_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Coordinates of the cities in the specific task
city_coordinates = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65),
    (38, 68), (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49),
    (18, 49), (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# Provided solution details
tour = [0, 19, 16, 3, 8, 14, 6, 7, 18, 0]
total_travel_cost = 317.59

# Verify the solution
result = verify_solution(tour, total_travel_cost, city_coordinates)
print(result)