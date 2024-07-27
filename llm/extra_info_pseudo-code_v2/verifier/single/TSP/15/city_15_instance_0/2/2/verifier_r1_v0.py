import math

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def check_solution(tour, total_cost, city_coordinates):
    # Check if the first and last city are the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if the robot visits each city exactly once, excluding the depot
    if sorted(tour) != sorted(list(range(15))):
        return "FAIL"

    # Calculate the travel cost and compare it with given cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])

    if abs(calculated_cost - total_cost) > 1e-5:
        return "FAIL"

    return "CORRECT"

# City coordinates as given in the problem description
city_coordinates = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), (79, 77), 
    (63, 23), (19, 76), (21, 38), (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)
]

# Tour and total cost as provided
given_tour = [0, 8, 10, 1, 11, 14, 12, 4, 9, 7, 3, 5, 6, 2, 13, 0]
given_total_cost = 359.53718629646994

# Check the solution
result = check_solution(given_tour, given_total_cost, city_coordinates)
print(result)