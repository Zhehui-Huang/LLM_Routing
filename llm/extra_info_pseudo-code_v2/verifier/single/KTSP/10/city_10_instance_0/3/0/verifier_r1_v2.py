import math

def euclidean_distance(city1, city2):
    # Calculate Euclidean distance between two points with coordinates (x1, y1) and (x2, y2)
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_travel_cost, city_coordinates):
    # Check if the robot starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Ensure exactly 4 unique cities are visited including the depot
    if len(set(tour)) != 5:  # Including the last city as the starting city again
        return "FAIL"
    
    # Calculate the total distance based on Euclidean distance
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
    
    # Check if calculated cost is close to the provided total cost
    if not math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Example city coordinates mapping
city_coordinates = [
    (50, 42),  # City 0 (depot)
    (41, 1),   # City 1
    (18, 46),  # City 2
    (40, 98),  # City 3
    (51, 69),  # City 4
    (47, 39),  # City 5
    (62, 26),  # City 6
    (79, 31),  # City 7
    (61, 90),  # City 8
    (42, 49)   # City 9
]

# Tour solution based on the data provided previosuly
tour = [0, 1, 2, 9, 0]
total_travel_cost = 127.33021785523412

# Perform the validation
result = verify_solution(tour, total_travel_cost, city_coordinates)
print("Test Result:", result)