import math

# Define the positions of all cities, including the depot (city 0)
city_positions = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61),
    5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
    10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
}

# Define groups of cities
city_groups = {
    0: [1, 2, 5, 6],
    1: [8, 9, 10, 13],
    2: [3, 4, 7],
    3: [11, 12, 14]
}

# Given tour and its total travel cost
tour = [0, 4, 11, 13, 5, 0]
reported_cost = 148.87

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def calculate_total_travel_cost(tour, city_positions):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(city_positions[tour[i]], city_positions[tour[i+1]])
    return round(total_cost, 2)

def verify_tour(tour, city_groups, city_positions, reported_cost):
    # Check the tour starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check tour includes exactly one city from each group
    visited_groups = set()
    for city in tour[1:-1]:  # exclude the starting and ending depot city
        for group in city_groups:
            if city in city_groups[group]:
                if group in visited_groups:
                    return "FAIL"
                visited_groups.add(group)
    if len(visited_groups) != len(city_groups):
        return "FAIL"
    
    # Check the reported distance matches the calculated distance
    calculated_cost = calculate_total_travel and_cost(tour, city_positions)
    if abs(calculated_cost - reported_cost) > 0.01:  # allow for slight rounding differences
        return "FAIL"
    
    # All checks passed
    return "CORRECT"

# Output verification result
verification_result = verify_tour(tour, city.Groups, city_positions, reported_cost)
print(verification_result)