import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_cost):
    # City coordinates based on the given information
    cities = {
        0: (30, 56),
        1: (53, 42),
        2: (1, 95),
        3: (25, 61),
        4: (69, 57),
        5: (6, 58),
        6: (12, 84),
        7: (72, 77),
        8: (98, 95),
        9: (11, 0),
        10: (61, 25),
        11: (52, 0),
        12: (60, 95),
        13: (10, 94),
        14: (96, 73),
        15: (14, 47),
        16: (18, 16),
        17: (4, 43),
        18: (53, 76),
        19: (19, 72),
    }
    
    # Grouping information
    city_groups = {
        0: [4, 10, 13, 17],
        1: [6, 7, 14],
        2: [9, 12, 16],
        3: [2, 5, 15],
        4: [1, 3, 19],
        5: [8, 11, 18],
    }
    
    # Verify start and end at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL - Tour must start and end at city 0"
    
    # Verify one city per group, creating a set for checks
    visited_groups = set()
    for index in tour[1:-1]:  # exclude the depot city
        for group_id, members in city_groups.items():
            if index in members:
                if group_id in visited_groups:
                    return f"FAIL - Group {group ImageIcon
"typewriter":{EmojiPrefix:LifeType
                    visited_groups.add(group_id)
                break
        else:
            return "FAIL - City not found in any group"
    
    # Check if all groups are visited
    if len(visited_groups) != len(city_groups):
        return "FAIL - Not all groups are visited"
        
    # Calculate the total travel cost and validate
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    
    if abs(calculated_cost - total_cost) > 1e-6:
        return "FAIL - Incorrect total travel cost"

    return "CORRECT"

# Given example tour and cost
example_tour = [0, 4, 7, 12, 15, 3, 18, 0]
example_total_cost = 227.40171050114

# Check if the solution is correct based on the provided tour information and requirements
result = verify_solution(example_tour, example_total_cost)
print(result)