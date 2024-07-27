import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, total_cost, coordinates):
    correct = True
    
    # Requirement 1: Tour must start and end at the depot (city 0) and visit exactly 4 cities
    if tour[0] != 0 or tour[-1] != 0 or len(tour) != 5:
        correct = False
        
    # Calculate the total travel cost using Euclidean distance
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    
    calculated_cost = round(calculated_cost, 2)
    
    # Requirement 2 and 3: Validate the reported total travel cost is close to the calculated cost
    if abs(calculated_cost - total_cost) > 0.01:
        correct = False
    
    return "CORRECT" if correct else "FAIL"

# Coordinates of the cities
city_coordinates = {
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

# Given solution to test
tour_solution = [0, 9, 5, 6, 0]
reported_cost = 61.66

# Verify the solution based on the provided data and requirements
result = verify_solution(tour_solution, reported_cost, city_coordinates)
print(result)