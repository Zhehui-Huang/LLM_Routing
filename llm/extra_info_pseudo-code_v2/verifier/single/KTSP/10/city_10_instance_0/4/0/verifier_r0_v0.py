import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_cost, city_coordinates):
    # Check if the robot starts and ends at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if exactly 4 cities are visited
    if len(tour) != 5:  # includes the returning city
        return "FAIL"

    # Check if the tour travels between exactly the cities in tour, and the cost is correct
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
    
    if round(calculated_cost, 2) != total_cost:
        return "FAIL"

    return "CORRECT"  # If all checks pass, the solution is correct

# Robot's tour and calculated total cost
robot_tour = [0, 9, 4, 7, 0]
total_travel_cost = 110.78

# City coordinates as provided
city_coords = {
    0: (50, 42),
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

# Testing the solution
result = verify_solution(robot_tour, total_travel_cost, city_coords)
print(result)