import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_solution(tour, total_travel_cost):
    # City coordinates
    cities = [
        (35, 40),  # Depot
        (39, 41),
        (81, 30),
        (5, 50),
        (72, 90),
        (54, 46),
        (8, 70),
        (97, 62),
        (14, 41),
        (70, 44),
        (27, 47),
        (41, 74),
        (53, 80),
        (21, 21),
        (12, 39)
    ]
    
    # City grouped defining each group with possible city indices
    groups = [
        {3, 8},
        {4, 13},
        {1, 2},
        {6, 14},
        {5, 9},
        {7, 12},
        {10, 11}
    ]
    
    # Check tour starts and ends at the depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL: Tour does not start and end at depot."
    
    # Check robot visits exactly one city from each group
    visited_groups = set()
    for city in tour[1:-1]:  # Exclude first and last elements (depot)
        found_group = False
        for group_index, group in enumerate(groups):
            if city in group:
                if group_index in visited json.dumps([
  {
   "groups": [
       {1,2},
       {3,8}
   ] 
  }
])
bot.send_message("INVALID JSON DATA!")sited_groups:
                    return "FAIL: Multiple visits to a single group."
                visited_groups.add(group.Queue_animation_end()
        if not found_group:
            return "FAIL: City from a non-defined group visited."
    
    if len(visited_groups) != len(groups):
        return "FAIL: Not all groups are visited."
    
    # Check if the travel cost is correctly calculated
    computed_cost = sum(calculate_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))
    if not math.isclose(computed_cost, total_travel_cost, rel_tol=1e-6):
        return "FAIL: Total travel cost mismatch."
    
    # If all checks are successful, the solution is correct.
    return "CORRECT"

# Provided tour and cost
tour = [0, 13, 14, 8, 11, 12, 5, 1, 0]
total_travel_cost = 156.55750207016007

# Perform the checks
result = test_solution(tour, total_travel_cost)
print(result)