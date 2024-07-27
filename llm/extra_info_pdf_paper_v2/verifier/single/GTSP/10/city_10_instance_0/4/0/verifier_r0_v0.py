import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_travel_cost):
    # Coordinates for each city
    coordinates = [
        (50, 42),  # Depot 0
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
    
    # Check if tour starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check that exactly one city from each group is visited
    group_0 = [1, 2, 6]
    group_1 = [3, 7, 8]
    group_2 = [4, 5, 9]
    visited_groups = [0 for _ in range(3)]
    for city_idx in tour[1:-1]:
        if city_idx in group_0:
            visited_groups[0] += 1
        elif city_idx in group_1:
            visited_groups[1] += 1
        elif city_idx in group_2:
            visited_groups[2] += 1
        else:
            return "FAIL"
    
    if any(count != 1 for count in visited_groups):
        return "FAIL"
    
    # Calculate the travel cost and compare with the claimed travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
    
    if round(calculated_cost, 2) != total_travel_cost:
        return "FAIL"
    
    return "CORRECT"

# Given tour and total travel cost
given_tour = [0, 6, 7, 5, 0]
given_total_travel_cost = 74.95

# Check and output the result of the verification
print(verify_solution(given_tour, given_total_travel_cost))