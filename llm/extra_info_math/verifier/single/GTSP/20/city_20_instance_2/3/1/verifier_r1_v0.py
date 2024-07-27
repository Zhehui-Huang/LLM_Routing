def test_tour_solution(tour, travel_cost):
    # Define groups and cities
    cities = {
        0: (3, 26),   # Depot
        1: (85, 72), 
        2: (67, 0), 
        3: (50, 99), 
        4: (61, 89), 
        5: (91, 56), 
        6: (2, 65), 
        7: (38, 68), 
        8: (3, 92), 
        9: (59, 8), 
        10: (30, 88), 
        11: (30, 53), 
        12: (11, 14), 
        13: (52, 49), 
        14: (18, 49), 
        15: (64, 41), 
        16: (28, 49), 
        17: (91, 94), 
        18: (51, 58), 
        19: (30, 48) 
    }
    groups = {
        0: [7, 10, 11, 12],
        1: [3, 8, 13, 16],
        2: [2, 4, 15, 18],
        3: [1, 9, 14, 19],
        4: [5, 6, 17]
    }
    
    # Check if the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if one city per group is visited
    visited_groups = set()
    for city in tour[1:-1]:  # Exclude the depot (start and end)
        for group_index, group_cities in groups.items():
            if city in group_cities:
                if group_index in visited_groups:
                    return "FAIL"  # City from the same group visited more than once
                visited_groups.add(group_index)
    if len(visited_groups) != 5:
        return "FAIL"  # Not all groups are visited

    # Calculate the total travel cost and compare with provided
    calculated_cost = 0
    for i in range(len(tour) - 1):
        source = cities[tour[i]]
        dest = cities[tour[i + 1]]
        calculated_cost += ((dest[0] - source[0])**2 + (dest[1] - source[1])**2)**0.5
    
    if round(calculated_cost, 2) != round(travel_cost, 2):
        return "FAIL"  # Provided cost does not match calculated cost
    
    return "CORRECT"

# Example tour and cost to test - Assume these values are from a proposed solution
tour = [0, 7, 3, 2, 1, 5, 0]
travel_cost = 432.4  # Assumed calculated total travel cost for this tour (Modify as needed)

# Test the solution
print(test_tour_solution(tour, travel_cost))