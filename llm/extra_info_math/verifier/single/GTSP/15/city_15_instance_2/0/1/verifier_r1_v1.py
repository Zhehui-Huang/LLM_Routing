def euclidean_distance(city1, city2):
    return ((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2) ** 0.5

def validate_solution(tour, costs, cities, groups):
    # Requirement 1: Start and end at the depot (city 0).
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Visit exactly one city from each group.
    # Capture the actual visited cities excluding the first and last since they are the depot
    actual_visits = set(tour[1:-1])
    # Check if one city from each group is visited
    for group in groups.values():
        if len(actual_visits.intersection(set(group))) != 1:
            return "FAIL"
    
    # Requirement 3: Check the total travel cost.
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city_from = cities[tour[i]]
        city_to = cities[tour[i + 1]]
        calculated_cost += euclidean_distance(city_from, city_to)
    
    # Allow for a small floating point calculation difference
    if abs(calculated_cost - costs) > 0.01:
        return "FAIL"
    
    return "CORRECT"

# Define the city coordinates and the groups from the problem description.
cities_index = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42), 
    5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14), 
    10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}

groups = {
    0: [8, 12, 14],
    1: [7, 10, 11],
    2: [4, 6, 9],
    3: [1, 3, 13],
    4: [2, 5]
}

# Tour and costs obtained from solver output
tour = [0, 6, 0, 6, 0, 6, 0]
total_travel_cost = 32.31

# Output the verification result
print(validate_solution(tour, total_travel_cost, cities_index, groups))