import math

def euclidean_distance(c1, c2):
    """Calculate the Euclidean distance between two cities given their coordinates."""
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# City coordinates
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57), 5: (6, 58), 6: (12, 84),
    7: (72, 77), 8: (98, 95), 9: (11, 0), 10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94),
    14: (96, 73), 15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# City groups
groups = {
    0: [4, 10, 13, 17], 1: [6, 7, 14], 2: [9, 12, 16], 3: [2, 5, 15],
    4: [1, 3, 19], 5: [8, 11, 18]
}

# Sample invalid tour (infeasible problem)
tour = [0, 4, 6, 9, 2, 1, 8, 0]  

def check_requirements(tour):
    # Check if tour starts and ends at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL: Tour does not start and end at depot city (City 0)."
    
    # Check if exactly one city from each group is visited
    visited_groups = {group_id: False for group_id in groups}
    for city in tour[1:-1]:
        found = False
        for group_id, cities in groups.items():
            if city in cities:
                if visited_groups[group_id]:
                    return "FAIL: Visited more than one city from a group."
                visited_groups[group_id] = True
                found = True
                break
        if not found:
            return "FAIL: Visited city not in any group."

    if not all(visited_groups.values()):
        return "FAIL: Not all groups are visited."

    # Calculate and print the total travel cost
    total_cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
    print(f"Total travel cost: {total_cost}")

    return "CORRECT"

# Execute test
result = check_requirements(tour)
print(result)