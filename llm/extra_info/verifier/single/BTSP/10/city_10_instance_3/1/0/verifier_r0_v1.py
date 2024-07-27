import math

def euclidean_distance(pt1, pt2):
    return math.sqrt((pt1[0] - pt2[0])**2 + (pt1[1] - pt2[1])**2)

def verify_solution(tour, total_travel_cost, max_distance):
    cities = {
        0: (84, 67),
        1: (74, 40),
        2: (71, 13),
        3: (74, 82),
        4: (97, 28),
        5: (0, 31),
        6: (8, 62),
        7: (74, 56),
        8: (85, 71),
        9: (6, 76)
    }
    
    # [There are 10 cities including the depot city 0.]
    if len(cities) != 10:
        return "FAIL"
    
    # [The robot must start and end its journey at the depot city 0.]
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [The robot must visit each city exactly once.]
    if sorted(tour) != sorted(cities.keys()):
        return "FAIL"
    
    # Calculate the tour cost and check max distance
    calculated_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        distance = euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
        calculated_cost += distance
        if distance > calculated_max_distance:
            calculated_max_distance = distance
    
    # [Output should include the tour as a list of city indices.]
    # [Output should include the total travel cost of the complete tour.]
    # [Output should include the maximum distance between any two consecutive cities in the tour.]
    if abs(calculated_cost - total_travel_cost) > 0.01:
        return "FAIL"
    if abs(calculated_max_distance - max_distance) > 0.01:
        return "FAIL"
    
    return "CORRECT"

# Provided solution details
tour = [0, 8, 3, 9, 5, 6, 7, 1, 2, 4, 0]
total_travel_cost = 345.92
max_distance = 68.26

# Verify the solution
print(verify_solution(tour, total_travel_cost, max_distance))