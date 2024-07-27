import math

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord2[0] - coord1[0])**2 + (coord2[1] - coord1[1])**2)

def verify_solution(tour, total_cost):
    # City coordinates defined as per the problem statement
    city_coordinates = [
        (50, 42),  # depot city 0
        (41, 1),   # city 1
        (18, 46),  # city 2
        (40, 98),  # city 3
        (51, 69),  # city 4
        (47, 39),  # city 5
        (62, 26),  # city 6
        (79, 31),  # city 7
        (61, 90),  # city 8
        (42, 49)   # city 9
    ]
    
    # Check the tour starts and ends at the depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check the tour visits exactly 4 cities
    if len(tour) != 5:  # Considering start and end cities (both are city 0)
        return "FAIL"
    
    # Calculate the cost using Euclidean distance
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city1 = city_coordinates[tour[i]]
        city2 = city_coordinates[tour[i + 1]]
        calculated_cost += euclidean_distance(city1, city2)
    
    # Compare the calculated cost with the given total cost
    if round(calculated_cost, 2) != round(total_cost, 2):
        return "FAIL"
    
    return "CORRECT"

# Given tour and cost solution to validate
given_tour = [0, 9, 5, 6, 0]
given_total_cost = 61.66

# Verify the solution
result = verify_solution(given_tour, given_total_cost)
print("Validation Result:", result)